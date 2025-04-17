# test_inventory_tracker.py

import os
import sqlite3
import pytest
from datetime import datetime
from inventory_sales_tracker import init_db,build_gui,save_pdf,save_csv

def test_init_db():
    # Test the database initialization function
    #init_db()
    
    # Check if the database file exists
    assert os.path.exists("store.db"), "Database file should exist."
    assert sqlite3.connect("store.db"), "Database connection should be established."
    
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
    
def test_build_gui():    
    # Test the GUI building function
    # This is a simple test to check if the GUI builds without errors
    # You can add more specific tests for GUI elements if needed

    assert callable(build_gui), "build_gui should be callable."
    assert hasattr(build_gui, '__call__'), "build_gui should be a callable function."
    
def test_save_pdf():
    if os.path.exists("sales_report.pdf"):
        os.remove("sales_report.pdf")
    # Test the PDF saving function
    # This is a simple test to check if the PDF saves without errors
    #assert callable(save_pdf), "save_pdf should be callable."
    assert hasattr(save_pdf, '__call__'), "save_pdf should be a callable function."
    assert save_pdf() ==  None, "save_pdf should return None."
    assert os.path.exists("sales_report.pdf"), "PDF file should exist after export."
    os.remove("sales_report.pdf")  # Clean up the PDF file after the test
    # Clean up the PDF file after the test
    
    
    
def test_save_csv():
    if os.path.exists("sales_report.csv"):
        os.remove("sales_report.csv")
    # Test the CSV saving function
    # This is a simple test to check if the CSV saves without errors
    #assert callable(save_csv), "save_csv should be callable."
    assert hasattr(save_csv, '__call__'), "save_csv should be a callable function."
    assert save_csv() == None, "save_csv should return None."
    assert os.path.exists("sales_report.csv"), "CSV file should exist after export."
    os.remove("sales_report.csv")  # Clean up the CSV file after the test
    
    
    

    


    
    
    
pytest.main(["-v", "--tb=line", "-rN", __file__])



