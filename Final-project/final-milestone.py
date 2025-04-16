import sqlite3
from tkinter import *
from datetime import datetime, timedelta

# --- Step 1: Connect to SQLite Database ---
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# --- Step 2: Create Tables ---

cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER,
        date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
""")

# --- Step 3: Insert Sample Products ---
products = [
    ("Wireless Mouse", 25.0, 15),
    ("Bluetooth Speaker", 40.0, 5),
    ("Laptop Stand", 30.0, 8),
    ("Webcam", 50.0, 12),
    ("Mechanical Keyboard", 80.0, 3)
]
cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", products)

# --- Step 4: Insert Sample Sales ---
today = datetime.now()
sales = [
    (1, 3, today - timedelta(days=1)),
    (2, 1, today - timedelta(days=2)),
    (3, 2, today),
    (1, 1, today),
    (4, 1, today - timedelta(days=3)),
    (5, 1, today),
    (2, 1, today),
    (1, 2, today - timedelta(days=1)),
]
sales_data = [(product_id, quantity, dt.strftime("%Y-%m-%d")) for product_id, quantity, dt in sales]
cursor.executemany("INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)", sales_data)

conn.commit()

# --- Step 5: Retrieve Top 5 Selling Products ---
print("\n📈 Top 5 Best-Selling Products:")
cursor.execute("""
    SELECT p.name, SUM(s.quantity) AS total_sold
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY s.product_id
    ORDER BY total_sold DESC
    LIMIT 5
""")
for name, total_sold in cursor.fetchall():
    print(f"- {name:<25} Sold: {total_sold}")

# --- Step 6: Show Low Stock Products (Threshold < 5) ---
print("\n⚠️ Low Stock Alerts:")
cursor.execute("SELECT name, stock FROM products WHERE stock < 5")
for name, stock in cursor.fetchall():
    print(f"- {name:<25} Stock Left: {stock}")

# --- Step 7: Total Revenue ---
print("\n💰 Total Revenue:")
cursor.execute("""
    SELECT SUM(s.quantity * p.price)
    FROM sales s
    JOIN products p ON s.product_id = p.id
""")
revenue = cursor.fetchone()[0]
print(f"Total Revenue: ${revenue:.2f}")

# Done
conn.close()



#Display Reports in a GUI Window
#A desktop app that shows:
#1.	Top 5 Best-Selling Products
#2.	Low Stock Products
#3.	Total Revenue

import sqlite3
from tkinter import *
from datetime import datetime, timedelta

# --- SETUP DATABASE ---
conn = sqlite3.connect("store.db")
cursor = conn.cursor()

# Drop and recreate for demo purposes
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE sales (
        id INTEGER PRIMARY KEY,
        product_id INTEGER,
        quantity INTEGER,
        date TEXT,
        FOREIGN KEY(product_id) REFERENCES products(id)
    )
""")

products = [
    ("Wireless Mouse", 25.0, 15),
    ("Bluetooth Speaker", 40.0, 5),
    ("Laptop Stand", 30.0, 8),
    ("Webcam", 50.0, 12),
    ("Mechanical Keyboard", 80.0, 3)
]
cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", products)

today = datetime.now()
sales = [
    (1, 3, today - timedelta(days=1)),
    (2, 1, today - timedelta(days=2)),
    (3, 2, today),
    (1, 1, today),
    (4, 1, today - timedelta(days=3)),
    (5, 1, today),
    (2, 1, today),
    (1, 2, today - timedelta(days=1)),
]
sales_data = [(product_id, quantity, dt.strftime("%Y-%m-%d")) for product_id, quantity, dt in sales]
cursor.executemany("INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)", sales_data)

conn.commit()

# --- GUI APP STARTS HERE ---
root = Tk()
root.title("📊 Inventory & Sales Dashboard")
root.geometry("500x500")
root.config(padx=20, pady=20)

# --- Helper Function to Add Text to UI ---
def add_section(title, data):
    Label(root, text=title, font=("Arial", 14, "bold")).pack(anchor="w", pady=(10, 0))
    for line in data:
        Label(root, text=line, font=("Arial", 12), anchor="w", justify="left").pack(anchor="w")

# --- Top Sellers ---
cursor.execute("""
    SELECT p.name, SUM(s.quantity) AS total_sold
    FROM sales s
    JOIN products p ON s.product_id = p.id
    GROUP BY s.product_id
    ORDER BY total_sold DESC
    LIMIT 5
""")
top_sellers = [f"{name} — Sold: {qty}" for name, qty in cursor.fetchall()]
add_section("📈 Top 5 Best-Selling Products", top_sellers)

# --- Low Stock ---
cursor.execute("SELECT name, stock FROM products WHERE stock < 5")
low_stock = [f"{name} — Only {stock} left!" for name, stock in cursor.fetchall()]
add_section("⚠️ Low Stock Alerts", low_stock if low_stock else ["All items well stocked ✅"])

# --- Total Revenue ---
cursor.execute("""
    SELECT SUM(s.quantity * p.price)
    FROM sales s
    JOIN products p ON s.product_id = p.id
""")
revenue = cursor.fetchone()[0] or 0
add_section("💰 Total Revenue", [f"${revenue:.2f}"])

# --- Main Loop ---
root.mainloop()

conn.close()

