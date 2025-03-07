
import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for generating random data
fake = Faker()

# MySQL Database Connection Details
DB_CONFIG = {
    "host": "ENTER YOUR HOST",
    "user": "ENTER YOUR USER NAME",
    "password": "ENTER YOUR PASSWORD",
    "database": "crop_management"
}

# List of sample crop names
crop_names = ["Wheat", "Rice", "Corn", "Soybean", "Barley", "Sugarcane", "Cotton", "Potato", "Tomato", "Lettuce"]

# List of possible growth stages
growth_stages = ["Seedling", "Vegetative", "Flowering", "Fruiting", "Maturity"]

# List of sample pest control measures
pest_control_measures_list = [
    "Use of organic pesticides",
    "Crop rotation",
    "Neem oil application",
    "Biological pest control",
    "Chemical pesticides",
    "Regular field monitoring",
]

# Database Connection Function
def connect_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        return None

# Function to Insert Manual Crop Record
def insert_manual_record():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        crop_name = crop_name_entry.get()
        planting_date = planting_date_entry.get()
        harvest_date = harvest_date_entry.get()
        growth_stage = growth_stage_entry.get()
        pest_control = pest_control_entry.get()
        yield_prediction = yield_entry.get()

        if not crop_name or not planting_date or not harvest_date or not growth_stage or not pest_control or not yield_prediction:
            messagebox.showwarning("Input Error", "All fields must be filled!")
            return

        try:
            cursor.execute("""
                INSERT INTO crops (crop_name, planting_date, harvest_date, growth_stage, pest_control_measures, yield_prediction)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (crop_name, planting_date, harvest_date, growth_stage, pest_control, yield_prediction))
            conn.commit()
            messagebox.showinfo("Success", "Crop record inserted successfully!")
            conn.close()
            display_records()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error inserting record: {e}")

# Function to Generate Random Data for Bulk Insert
def generate_data():
    crop_name = random.choice(crop_names)
    planting_date = fake.date_between(start_date="-2y", end_date="today")  # Planting in last 2 years
    harvest_date = planting_date + timedelta(days=random.randint(60, 180))  # Harvest after 2-6 months
    growth_stage = random.choice(growth_stages)
    pest_control = random.choice(pest_control_measures_list)
    yield_prediction = random.randint(500, 5000)  # Yield in kg
    return (crop_name, planting_date, harvest_date, growth_stage, pest_control, yield_prediction)

# Function to Insert 100,000 Random Records
def insert_bulk_records():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        batch_size = 10000
        total_records = 100000

        for i in range(0, total_records, batch_size):
            data_batch = [generate_data() for _ in range(batch_size)]
            cursor.executemany("""
                INSERT INTO crops (crop_name, planting_date, harvest_date, growth_stage, pest_control_measures, yield_prediction)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, data_batch)
            conn.commit()
            progress_label.config(text=f"{i + batch_size} records inserted...")

        messagebox.showinfo("Success", "100,000 records inserted successfully!")
        conn.close()
        display_records()

# Function to Display Records
def display_records():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM crops ORDER BY id DESC LIMIT 20")  # Show last 20 records
        rows = cursor.fetchall()
        conn.close()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert("", "end", values=row)

# GUI Setup
root = tk.Tk()
root.title("Crop Management System")
root.geometry("800x600")

# Input Fields
tk.Label(root, text="Crop Name").grid(row=0, column=0)
crop_name_entry = tk.Entry(root)
crop_name_entry.grid(row=0, column=1)

tk.Label(root, text="Planting Date (YYYY-MM-DD)").grid(row=1, column=0)
planting_date_entry = tk.Entry(root)
planting_date_entry.grid(row=1, column=1)

tk.Label(root, text="Harvest Date (YYYY-MM-DD)").grid(row=2, column=0)
harvest_date_entry = tk.Entry(root)
harvest_date_entry.grid(row=2, column=1)

tk.Label(root, text="Growth Stage").grid(row=3, column=0)
growth_stage_entry = tk.Entry(root)
growth_stage_entry.grid(row=3, column=1)

tk.Label(root, text="Pest Control Measures").grid(row=4, column=0)
pest_control_entry = tk.Entry(root)
pest_control_entry.grid(row=4, column=1)

tk.Label(root, text="Yield Prediction (kg)").grid(row=5, column=0)
yield_entry = tk.Entry(root)
yield_entry.grid(row=5, column=1)

# Buttons
insert_button = tk.Button(root, text="Insert Record", command=insert_manual_record)
insert_button.grid(row=6, column=0, columnspan=2)

bulk_insert_button = tk.Button(root, text="Insert 100,000 Random Records", command=insert_bulk_records)
bulk_insert_button.grid(row=7, column=0, columnspan=2)

progress_label = tk.Label(root, text="")
progress_label.grid(row=8, column=0, columnspan=2)

# Table to Display Records
columns = ("ID", "Crop Name", "Planting Date", "Harvest Date", "Growth Stage", "Pest Control", "Yield Prediction")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.grid(row=9, column=0, columnspan=2)

# Load initial records
display_records()

# Run the GUI
root.mainloop()
 
 
