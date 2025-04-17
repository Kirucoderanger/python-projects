"""inventory and sales tracker app with:
•	Persistent database to track products and sales
•	A GUI interface to interact with inventory and sales
•	Exporting options to keep reports for analysis
"""
#Author: Kirubel Mekonen
#Date: 2025-04-16
# This code is a simple inventory and sales tracker app with a GUI interface.
#A persistent SQLite DB: store.db
#Products are added only if the table is empty (not every run)
#A basic GUI window with buttons for each main feature
#A simple database with two tables: products and sales
#The app allows users to view reports, search for products, add sales, restock products, and export reports.
#The app produces a CSV and PDF report of sales data.
#The app uses the tkinter library for the GUI and reportlab for PDF generation.
# The app is designed to be user-friendly and provides a simple interface for managing inventory and sales.
# It is a basic implementation and can be further enhanced with more features and functionalities.
#the app has a pytest test suite that tests the functionality of the app.
# The test suite includes tests for the main functions of the app, including database initialization, GUI building, and report generation.




import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
from datetime import datetime, timedelta
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# ------------------------- DATABASE INIT -------------------------
def init_db():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()

    # Create tables if not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            quantity INTEGER,
            date TEXT,
            FOREIGN KEY(product_id) REFERENCES products(id)
        )
    """)

    # Insert some starter products only if table is empty
    cursor.execute("SELECT COUNT(*) FROM products")
    if cursor.fetchone()[0] == 0:
        starter_products = [
            ("Wireless Mouse", 25.0, 15),
            ("Bluetooth Speaker", 40.0, 5),
            ("Laptop Stand", 30.0, 8),
            ("Webcam", 50.0, 12),
            ("Mechanical Keyboard", 80.0, 3)
        ]
        cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", starter_products)
        conn.commit()

    conn.close()


# ------------------------- GUI INIT -------------------------
def build_gui():
    root = Tk()
    root.title("🛒 Inventory & Sales Tracker")
    root.geometry("600x400")
    root.config(padx=20, pady=20)

    Label(root, text="📊 Dashboard", font=("Arial", 18, "bold")).pack(pady=10)

    Button(root, text="📅 View Reports by Date", width=30, command=view_by_date).pack(pady=5)
    Button(root, text="🔍 Search Product", width=30, command=search_product).pack(pady=5)
    Button(root, text="➕ Add Sale", width=30, command=add_sale).pack(pady=5)
    Button(root, text="📦 Restock Product", width=30, command=restock_product).pack(pady=5)
    Button(root, text="📤 Export Report", width=30, command=export_report).pack(pady=5)

    root.mainloop()


# ------------------------- PLACEHOLDER FUNCTIONS -------------------------
"""def view_by_date():
    messagebox.showinfo("Coming Soon", "View reports by date will be added next!")

def search_product():
    messagebox.showinfo("Coming Soon", "Search feature coming next!")

def add_sale():
    messagebox.showinfo("Coming Soon", "Add sale functionality coming soon!")

def restock_product():
    messagebox.showinfo("Coming Soon", "Restock functionality coming soon!")

def export_report():
    messagebox.showinfo("Coming Soon", "Exporting to CSV/PDF will be added later!")"""



#show report 


def view_by_date():
    def load_report():
        filter_option = filter_var.get()
        now = datetime.now()
        
        if filter_option == "Today":
            date_from = now.strftime("%Y-%m-%d")
        elif filter_option == "Last 7 Days":
            date_from = (now - timedelta(days=7)).strftime("%Y-%m-%d")
        else:
            date_from = "0000-01-01"  # all time

        # Connect to DB
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()

        # Total revenue
        cur.execute("""
            SELECT SUM(s.quantity * p.price)
            FROM sales s
            JOIN products p ON s.product_id = p.id
            WHERE date(s.date) >= date(?)
        """, (date_from,))
        revenue = cur.fetchone()[0] or 0

        # Top 5
        cur.execute("""
            SELECT p.name, SUM(s.quantity) as total_sold
            FROM sales s
            JOIN products p ON s.product_id = p.id
            WHERE date(s.date) >= date(?)
            GROUP BY s.product_id
            ORDER BY total_sold DESC
            LIMIT 5
        """, (date_from,))
        top_sellers = cur.fetchall()

        # Low stock
        cur.execute("SELECT name, stock FROM products WHERE stock < 5")
        low_stock = cur.fetchall()

        conn.close()

        # Update text areas
        txt_total.config(text=f"💰 Total Revenue: ${revenue:.2f}")

        txt_top.delete(0, END)
        for name, qty in top_sellers:
            txt_top.insert(END, f"{name} - Sold: {qty}")

        txt_low.delete(0, END)
        if low_stock:
            for name, stock in low_stock:
                txt_low.insert(END, f"{name} - Stock: {stock}")
        else:
            txt_low.insert(END, "✅ All items well stocked!")
        return load_report

    # GUI Window
    win = Toplevel()
    win.title("📅 Sales Report by Date")
    win.geometry("500x500")
    win.config(padx=15, pady=15)

    filter_var = StringVar(value="Today")
    ttk.Label(win, text="Select Date Range:", font=("Arial", 12)).pack()
    ttk.Combobox(win, textvariable=filter_var, values=["Today", "Last 7 Days", "All Time"]).pack(pady=5)

    Button(win, text="🔍 Load Report", command=load_report).pack(pady=10)

    txt_total = Label(win, text="", font=("Arial", 14, "bold"))
    txt_total.pack(pady=10)

    Label(win, text="📈 Top 5 Best Sellers:").pack()
    txt_top = Listbox(win, height=6)
    txt_top.pack(fill="x")

    Label(win, text="⚠️ Low Stock Products:").pack(pady=(10, 0))
    txt_low = Listbox(win, height=6)
    txt_low.pack(fill="x")







#search product

def search_product():
    def perform_search():
        name_query = entry_search.get().strip()

        if not name_query:
            messagebox.showwarning("Empty Search", "Please enter a product name.")
            return

        conn = sqlite3.connect("store.db")
        cur = conn.cursor()

        # Search by partial name match
        cur.execute("SELECT id, name FROM products WHERE name LIKE ?", (f"%{name_query}%",))
        results = cur.fetchall()
        conn.close()

        listbox_results.delete(0, END)
        for pid, name in results:
            listbox_results.insert(END, f"{pid}: {name}")

    def show_details(event):
        selection = listbox_results.get(ACTIVE)
        if not selection:
            return

        product_id = int(selection.split(":")[0])
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()

        cur.execute("SELECT name, price, stock FROM products WHERE id = ?", (product_id,))
        name, price, stock = cur.fetchone()

        cur.execute("SELECT SUM(quantity) FROM sales WHERE product_id = ?", (product_id,))
        total_sold = cur.fetchone()[0] or 0
        conn.close()

        label_info.config(text=f"""
🛒 Product: {name}
💵 Price: ${price:.2f}
📦 Stock: {stock}
📈 Sold: {total_sold} units
        """.strip())

    # GUI
    win = Toplevel()
    win.title("🔍 Search Product")
    win.geometry("450x400")
    win.config(padx=15, pady=15)

    Label(win, text="Enter product name:", font=("Arial", 12)).pack()
    entry_search = Entry(win, width=30)
    entry_search.pack(pady=5)

    Button(win, text="Search", command=perform_search).pack(pady=5)

    Label(win, text="Results:").pack()
    listbox_results = Listbox(win, height=6)
    listbox_results.pack(fill="x", pady=5)
    listbox_results.bind("<<ListboxSelect>>", show_details)

    label_info = Label(win, text="", justify=LEFT, font=("Courier", 10))
    label_info.pack(pady=10)




#add product

def add_sale():
    def load_products():
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM products")
        products = cur.fetchall()
        conn.close()
        return products

    def submit_sale():
        selected = product_var.get()
        qty = entry_qty.get()

        if not selected or not qty.isdigit():
            messagebox.showerror("Error", "Select a product and enter a valid quantity.")
            return

        qty = int(qty)
        product_id = int(selected.split(":")[0])

        conn = sqlite3.connect("store.db")
        cur = conn.cursor()

        cur.execute("SELECT name, stock, price FROM products WHERE id = ?", (product_id,))
        name, stock, price = cur.fetchone()

        if qty > stock:
            messagebox.showwarning("Not enough stock", f"Only {stock} units of {name} left.")
            conn.close()
            return

        # Update stock and record sale
        new_stock = stock - qty
        cur.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
        cur.execute("INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)", (
            product_id, qty, datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"{qty} units of '{name}' sold.\nRemaining stock: {new_stock}")
        win.destroy()

    # GUI
    win = Toplevel()
    win.title("➕ Add Sale")
    win.geometry("400x250")
    win.config(padx=20, pady=20)

    Label(win, text="Select Product:", font=("Arial", 12)).pack(pady=5)

    product_var = StringVar()
    products = load_products()
    product_dropdown = ttk.Combobox(win, textvariable=product_var, width=35)
    product_dropdown["values"] = [f"{pid}: {name}" for pid, name in products]
    product_dropdown.pack(pady=5)

    Label(win, text="Quantity:").pack(pady=5)
    entry_qty = Entry(win, width=10)
    entry_qty.pack(pady=5)

    Button(win, text="➕ Submit Sale", command=submit_sale).pack(pady=15)

#restock product

def restock_product():
    def load_products():
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM products")
        products = cur.fetchall()
        conn.close()
        return products

    def submit_restock():
        selected = product_var.get()
        qty = entry_qty.get()

        if not selected or not qty.isdigit():
            messagebox.showerror("Error", "Select a product and enter a valid quantity.")
            return

        qty = int(qty)
        product_id = int(selected.split(":")[0])

        conn = sqlite3.connect("store.db")
        cur = conn.cursor()

        cur.execute("SELECT name, stock FROM products WHERE id = ?", (product_id,))
        name, stock = cur.fetchone()

        # Update stock
        new_stock = stock + qty
        cur.execute("UPDATE products SET stock = ? WHERE id = ?", (new_stock, product_id))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"{qty} units of '{name}' added.\nNew stock: {new_stock}")
        win.destroy()

    # GUI
    win = Toplevel()
    win.title("📦 Restock Product")
    win.geometry("400x250")
    win.config(padx=20, pady=20)

    Label(win, text="Select Product:", font=("Arial", 12)).pack(pady=5)

    product_var = StringVar()
    products = load_products()
    product_dropdown = ttk.Combobox(win, textvariable=product_var, width=35)
    product_dropdown["values"] = [f"{pid}: {name}" for pid, name in products]
    product_dropdown.pack(pady=5)

    Label(win, text="Quantity to Add:").pack(pady=5)
    entry_qty = Entry(win, width=10)
    entry_qty.pack(pady=5)

    Button(win, text="📦 Submit Restock", command=submit_restock).pack(pady=15)

#generate CSV PDF report



def export_report():
    def save_csv():
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT s.date, p.name, s.quantity, p.price, (s.quantity * p.price) as total
            FROM sales s
            JOIN products p ON s.product_id = p.id
        """)
        sales_data = cur.fetchall()
        conn.close()

        with open("sales_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Product Name", "Quantity", "Price", "Total"])
            writer.writerows(sales_data)

        messagebox.showinfo("CSV Export", "Sales data exported to 'sales_report.csv'.")

    def save_pdf():
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT s.date, p.name, s.quantity, p.price, (s.quantity * p.price) as total
            FROM sales s
            JOIN products p ON s.product_id = p.id
        """)
        sales_data = cur.fetchall()
        conn.close()

        pdf_file = canvas.Canvas("sales_report.pdf", pagesize=letter)
        pdf_file.setFont("Helvetica", 10)
        pdf_file.drawString(30, 750, "Sales Report")

        y_position = 730
        pdf_file.drawString(30, y_position, "Date | Product Name | Quantity | Price | Total")
        y_position -= 15

        for row in sales_data:
            date, name, qty, price, total = row
            pdf_file.drawString(30, y_position, f"{date} | {name} | {qty} | ${price:.2f} | ${total:.2f}")
            y_position -= 15

        pdf_file.save()
        messagebox.showinfo("PDF Export", "Sales data exported to 'sales_report.pdf'.")

    # GUI
    win = Toplevel()
    win.title("📤 Export Report")
    win.geometry("300x150")
    win.config(padx=20, pady=20)

    Label(win, text="Export Sales Report", font=("Arial", 14)).pack(pady=10)

    Button(win, text="💾 Export as CSV", command=save_csv).pack(pady=5)
    Button(win, text="📄 Export as PDF", command=save_pdf).pack(pady=5)
    
def save_pdf():
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT s.date, p.name, s.quantity, p.price, (s.quantity * p.price) as total
            FROM sales s
            JOIN products p ON s.product_id = p.id
        """)
        sales_data = cur.fetchall()
        conn.close()

        pdf_file = canvas.Canvas("sales_report.pdf", pagesize=letter)
        pdf_file.setFont("Helvetica", 10)
        pdf_file.drawString(30, 750, "Sales Report")

        y_position = 730
        pdf_file.drawString(30, y_position, "Date | Product Name | Quantity | Price | Total")
        y_position -= 15

        for row in sales_data:
            date, name, qty, price, total = row
            pdf_file.drawString(30, y_position, f"{date} | {name} | {qty} | ${price:.2f} | ${total:.2f}")
            y_position -= 15

        pdf_file.save()
        messagebox.showinfo("PDF Export", "Sales data exported to 'sales_report.pdf'.")
        
def save_csv():
        conn = sqlite3.connect("store.db")
        cur = conn.cursor()
        cur.execute("""
            SELECT s.date, p.name, s.quantity, p.price, (s.quantity * p.price) as total
            FROM sales s
            JOIN products p ON s.product_id = p.id
        """)
        sales_data = cur.fetchall()
        conn.close()

        with open("sales_report.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Product Name", "Quantity", "Price", "Total"])
            writer.writerows(sales_data)

        messagebox.showinfo("CSV Export", "Sales data exported to 'sales_report.csv'.")




# ------------------------- MAIN -------------------------
if __name__ == "__main__":
    init_db()
    build_gui()