import pytest
from unittest.mock import patch

from pytest import fixture
from inventory_sales_tracker import init_db, view_by_date, search_product, add_sale\
    ,restock_product,export_report 
import sqlite3
import os





"""def test_init_db():
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    # Check if the products table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    assert cursor.fetchone() is not None, "Products table should exist."
    # Check if the sales table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales'")
    assert conn is not None, "Database connection should not be None."
    conn.close()"""
#     ("Product A", 10.0, 100),
@pytest.fixture
def setup_db():
    # Set up the database connection and cursor
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Create tables if they don't exist
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
    
    yield cursor
    
    
def test_init_db():
    # Test the database initialization function
    init_db()
    
    # Check if the database file exists
    assert os.path.exists("store.db"), "Database file should exist."
    
    # Connect to the database and check if tables are created
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Check if the products table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='products'")
    assert cursor.fetchone() is not None, "Products table should exist."
    
    # Check if the sales table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sales'")
    assert cursor.fetchone() is not None, "Sales table should exist."
    
    conn.close()
    # Clean up the database file after the test
    
def test_view_by_date():
    # Test the view_by_date function
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Insert test data into the products table
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ("Test Product", 10.0, 100))
    product_id = cursor.lastrowid
    
    # Insert test data into the sales table
    cursor.execute("INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)", (product_id, 5, "2023-10-01"))
    
    # Commit the changes to the database
    conn.commit()
    
    # Call the view_by_date function with a specific date
    result = view_by_date("2023-10-01")
    
    # Check if the result contains the expected data
    assert len(result) == 1, "Should return one record for the given date."
    assert result[0][1] == "Test Product", "Product name should match."
    
    # Clean up the database after the test
    cursor.execute("DELETE FROM sales WHERE product_id = ?", (product_id,))
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    
def test_view_by_date(mocker):
    mocker.patch('builtins.input', return_value='2023-10-01')  # Mock user input
    result = view_by_date()  # Call the view_by_date function
    assert result, "View by date should return results."
    assert isinstance(result, list), "View by date result should be a list."
    assert len(result) > 0, "View by date result should not be empty."
    assert all(isinstance(item, tuple) for item in result), "Each item in the result should be a tuple."
    assert all(len(item) == 4 for item in result), "Each tuple should have 4 elements."
    
def test_search_product(mocker):
    mocker.patch('builtins.input', return_value='Keyboard')  # Mock user input
    result = search_product()  # perform_search should return the results
    assert result, "Search should return results."
    assert isinstance(result, list), "Search result should be a list."
    assert len(result) > 0, "Search result should not be empty."
    assert all(isinstance(item, tuple) for item in result), "Each item in the result should be a tuple."
    assert all(len(item) == 4 for item in result), "Each tuple should have 4 elements."
    
def test_restock_product(mocker):
    mocker.patch('builtins.input', return_value='1')  # Mock user input for product ID
    mocker.patch('builtins.input', return_value='50')  # Mock user input for restock quantity
    result = restock_product()  # Call the restock_product function
    assert result, "Restock should be successful."
    assert isinstance(result, tuple), "Result should be a tuple."
    assert len(result) == 2, "Result should have 2 elements."
    assert result[0] == 1, "Product ID should match."
    assert result[1] == 50, "Restock quantity should match."
    
def test_restock_product(mocker):
    mocker.patch('builtins.input', side_effect=["D083", "5"])  # Mock product and quantity
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    initial_stock = cur.execute("SELECT stock FROM products WHERE id = 1").fetchone()[0]

    restock_product()  # Call the restock function

    updated_stock = cur.execute("SELECT stock FROM products WHERE id = 1").fetchone()[0]
    assert updated_stock == initial_stock + 5, "Stock should be updated correctly after restocking."
    conn.close()

def test_save_csv():
    try:
        export_report()  # Execute CSV export function
        assert os.path.exists("sales_report.csv"), "CSV file should be saved."
    except Exception as e:
        pytest.fail(f"Exporting CSV failed: {e}")

    
def test_search_product():
    # Test the search_product function
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Insert test data into the products table
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ("Test Product", 10.0, 100))
    product_id = cursor.lastrowid
    
    # Call the search_product function with a specific product name
    result = search_product("Test Product")
    
    # Check if the result contains the expected data
    assert len(result) == 1, "Should return one record for the given product name."
    assert result[0][1] == "Test Product", "Product name should match."
    
    # Clean up the database after the test
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    
def test_add_sale(mocker):
    mocker.patch('builtins.input', return_value='1')  # Mock user input
    mocker.patch('builtins.input', return_value='5')  # Mock user input
    mocker.patch('builtins.input', return_value='2023-10-01')  # Mock user input
    
    result = add_sale()  # Call the add_sale function
    assert result, "Sale should be added successfully."
    assert isinstance(result, tuple), "Result should be a tuple."
    assert len(result) == 3, "Result should have 3 elements."
    assert result[0] == 1, "Product ID should match."
    
"""def test_submit_sale(mocker):
    mocker.patch('builtins.input', side_effect=["D083", "2"])  # Mock product and quantity
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    initial_stock = cur.execute("SELECT stock FROM products WHERE id = 1").fetchone()[0]

    submit_sale()  # Call the sale submission function

    updated_stock = cur.execute("SELECT stock FROM products WHERE id = 1").fetchone()[0]
    assert updated_stock == initial_stock - 2, "Stock should be updated correctly after the sale."
    conn.close()"""

    
def test_add_sale():
    # Test the add_sale function
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Insert test data into the products table
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ("Test Product", 10.0, 100))
    product_id = cursor.lastrowid
    
    # Call the add_sale function to add a sale
    add_sale(product_id, 5, "2023-10-01")
    
    # Check if the sale was added correctly
    cursor.execute("SELECT * FROM sales WHERE product_id = ? AND date = ?", (product_id, "2023-10-01"))
    result = cursor.fetchone()
    
    assert result is not None, "Sale should be added to the sales table."
    assert result[1] == product_id, "Product ID should match."
    assert result[2] == 5, "Quantity should match."
    
    # Clean up the database after the test
    cursor.execute("DELETE FROM sales WHERE product_id = ?", (product_id,))
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()
    
def test_restock_product():
    # Test the restock_product function
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Insert test data into the products table
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ("Test Product", 10.0, 100))
    product_id = cursor.lastrowid
    
    # Call the restock_product function to restock the product
    restock_product(product_id, 50)
    
    # Check if the stock was updated correctly
    cursor.execute("SELECT stock FROM products WHERE id = ?", (product_id,))
    result = cursor.fetchone()
    
    assert result is not None, "Product should exist in the products table."
    assert result[0] == 150, "Stock should be updated to 150."
    
    # Clean up the database after the test
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def test_export_report():
    # Test the export_report function
    conn = sqlite3.connect("store.db")
    cursor = conn.cursor()
    
    # Insert test data into the products table
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ("Test Product", 10.0, 100))
    product_id = cursor.lastrowid
    
    # Insert test data into the sales table
    cursor.execute("INSERT INTO sales (product_id, quantity, date) VALUES (?, ?, ?)", (product_id, 5, "2023-10-01"))
    
    # Commit the changes to the database
    conn.commit()
    
    # Call the export_report function to generate the report
    export_report("report.txt")
    
    # Check if the report file was created and contains expected data
    assert os.path.exists("report.txt"), "Report file should exist."
    
    with open("report.txt", "r") as f:
        report_content = f.read()
        assert "Test Product" in report_content, "Report should contain product name."
        assert "5" in report_content, "Report should contain sale quantity."
    
    # Clean up the database after the test
    cursor.execute("DELETE FROM sales WHERE product_id = ?", (product_id,))
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()   
    
    



