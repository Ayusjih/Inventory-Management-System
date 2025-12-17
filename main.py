import mysql.connector
from mysql.connector import Error
from tabulate import tabulate #pretty tables
import sys


DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',         
    'password': '1234', 
    'database': 'inventory_db'
}



def get_connection():
    """Establishes connection to MySQL database."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_db():
    """Flowchart Step: Connect / Initialize Database & Create Table."""
    try:
    
        temp_config = DB_CONFIG.copy()
        del temp_config['database']
        conn = mysql.connector.connect(**temp_config)
        cursor = conn.cursor()
        
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
        conn.close()

    
        conn = get_connection()
        cursor = conn.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            category VARCHAR(50),
            quantity INT,
            price DECIMAL(10,2),
            added_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print(">> Database and Table initialized successfully.")
    except Error as e:
        print(f"Initialization Error: {e}")



def add_product():
    """Logic: Validate ID, Qty > 0, Price valid -> Insert."""
    conn = get_connection()
    cursor = conn.cursor()
    
    print("\n--- ADD PRODUCT ---")
    try:
        p_id = int(input("Enter Product ID (Unique Integer): "))
        name = input("Enter Name: ")
        category = input("Enter Category: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))

        # Validation Logic
        if qty < 0:
            print("Error: Quantity cannot be negative.")
            return
        if price < 0:
            print("Error: Price cannot be negative.")
            return

        query = "INSERT INTO products (product_id, name, category, quantity, price) VALUES (%s, %s, %s, %s, %s)"
        values = (p_id, name, category, qty, price)
        
        cursor.execute(query, values)
        conn.commit()
        print(">> Product Added Successfully!")
        
    except mysql.connector.IntegrityError:
        print("Error: Product ID already exists!")
    except ValueError:
        print("Error: Invalid input type (expected numbers for ID/Qty/Price).")
    except Error as e:
        print(f"Database Error: {e}")
    finally:
        if conn: conn.close()

def update_product():
    """Logic: Fetch -> Display -> Modify -> Update."""
    conn = get_connection()
    cursor = conn.cursor()
    
    print("\n--- UPDATE PRODUCT ---")
    p_id = input("Enter Product ID to update: ")
    
    # Check if exists
    cursor.execute("SELECT * FROM products WHERE product_id = %s", (p_id,))
    product = cursor.fetchone()
    
    if not product:
        print("Product not found.")
        conn.close()
        return

    print(f"Current Data: Name={product[1]}, Qty={product[3]}, Price={product[4]}")
    

    new_qty = input("Enter new Quantity (Press Enter to skip): ")
    new_price = input("Enter new Price (Press Enter to skip): ")
    
    try:
        if new_qty:
            cursor.execute("UPDATE products SET quantity = %s WHERE product_id = %s", (int(new_qty), p_id))
        if new_price:
            cursor.execute("UPDATE products SET price = %s WHERE product_id = %s", (float(new_price), p_id))
        
        conn.commit()
        print(">> Product Updated Successfully.")
    except Error as e:
        print(f"Update Error: {e}")
    finally:
        if conn: conn.close()

def delete_product():
    """Logic not explicitly detailed in flowchart bottom boxes but present in menu."""
    conn = get_connection()
    cursor = conn.cursor()
    
    print("\n--- DELETE PRODUCT ---")
    p_id = input("Enter Product ID to delete: ")
    
    try:
        cursor.execute("DELETE FROM products WHERE product_id = %s", (p_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print(">> Product Deleted.")
        else:
            print("Product ID not found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn: conn.close()

def view_inventory():
    """Logic: Fetch all -> Show table."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT product_id, name, category, quantity, price, added_on FROM products")
    rows = cursor.fetchall()
    
    if not rows:
        print("Inventory is empty.")
    else:

        headers = ["ID", "Name", "Category", "Qty", "Price", "Added On"]
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    
    conn.close()

def generate_reports():
    """Logic: Generate low-stock items & product count."""
    conn = get_connection()
    cursor = conn.cursor()
    
    print("\n--- REPORTS ---")
    

    cursor.execute("SELECT COUNT(*) FROM products")
    total_products = cursor.fetchone()[0]
    print(f"Total Products in Inventory: {total_products}")
    

    threshold = 5
    print(f"\nLow Stock Alert (Quantity < {threshold}):")
    cursor.execute("SELECT product_id, name, quantity FROM products WHERE quantity < %s", (threshold,))
    low_stock_items = cursor.fetchall()
    
    if low_stock_items:
        print(tabulate(low_stock_items, headers=["ID", "Name", "Qty"], tablefmt="simple"))
    else:
        print(">> No items are low on stock.")
        
    conn.close()



def main():
    init_db()
    
    while True:
        print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Inventory")
        print("5. Reports (Low-stock)")
        print("6. Bulk Update (Placeholder)")
        print("7. EXIT")
        
        choice = input("Enter Choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            delete_product()
        elif choice == '4':
            view_inventory()
        elif choice == '5':
            generate_reports()
        elif choice == '6':
            print(">> Bulk Update feature coming soon!")
        elif choice == '7':
            print("Exiting System... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()