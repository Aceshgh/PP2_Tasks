import psycopg2 
import csv

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="akzhan11",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS phoneBook (
    id SERIAL PRIMARY KEY,
    username TEXT,
    phone TEXT
);
""")
conn.commit()

def console_input():
    username = input("Enter name: ")
    phone = input("Enter phone: ")

    cursor.execute("""
        INSERT INTO phoneBook (username, phone)
        VALUES (%s, %s);
    """, (username, phone))

    conn.commit()
    print("User added via console.")

def csv_input(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
                INSERT INTO phoneBook (username, phone)
                VALUES (%s, %s);
            """, (row['username'], row['phone']))
    conn.commit()
    print("Users loaded from CSV.")

def update_user():
    field = input("Update 'username' or 'phone': ").strip().lower()
    if field not in ['username', 'phone']:
        print("Invalid field.")
        return

    identifier = input("Enter username or phone to find: ")
    new_value = input(f"Enter new {field}: ")

    cursor.execute(f"""
        UPDATE phoneBook
        SET {field} = %s
        WHERE username = %s OR phone = %s;
    """, (new_value, identifier, identifier))

    conn.commit()
    print("User updated.")

def query_users():
    print("Search by:\n1. Username\n2. Phone\n3. All")
    choice = input("Enter: ").strip()

    if choice == "1":
        username = input("Username to search: ")
        cursor.execute("SELECT * FROM phoneBook WHERE username ILIKE %s;", (f"%{username}%",))
    elif choice == "2":
        phone = input("Phone to search: ")
        cursor.execute("SELECT * FROM phoneBook WHERE phone LIKE %s;", (f"%{phone}%",))
    elif choice == "3":
        cursor.execute("SELECT * FROM phoneBook;")
    else:
        print("Invalid choice.")
        return

    results = cursor.fetchall()
    for row in results:
        print(row)
def del_user():
    user = input("Enter a username or phone to delete: ")
    cursor.execute("DELETE FROM phoneBook WHERE username = %s OR phone = %s;", (user, user))
    conn.commit()
    print(f"Deleted: {user}")

while True:
    print("\nPhoneBook Menu:")
    print("1 - Add a user")
    print("2 - Query users")
    print("3 - Delete a user")
    print("4 - Exit")
    choice = input("Enter: ").strip()

    if choice == "1":
        console_input()
    elif choice == "2":
        query_users()
    elif choice == "3":
        del_user()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
cursor.close()
conn.close()