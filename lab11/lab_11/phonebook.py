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

def search_by_pattern():
    pattern = input("enter(username or phone): ")
    cursor.execute("SELECT * FROM search_by_pattern(%s);", (pattern,))
    for row in cursor.fetchall():
        print(row)

def upsert_user():
    username = input("enter username: ")
    phone = input("enter phone: ")
    cursor.execute("CALL upsert_user(%s, %s);", (username, phone))
    conn.commit()
    print("accepted")

def bulk_insert_from_csv():
    filename = input("enter CSV filename: ")
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        names = []
        phones = []
        for row in reader:
            names.append(row['name'])
            phones.append(row['phone'])
        cursor.execute("SELECT bulk_insert_users(%s::text[], %s::text[]);", (names, phones))
        print("bulk insert executed")
        conn.commit()

def paginate():
    limit = int(input("enter limit: "))
    offset = int(input("enter offset: "))
    cursor.execute("SELECT * FROM paginate_users(%s, %s);", (limit, offset))
    for row in cursor.fetchall():
        print(row)
def delete_by_value():
    value = input("enter username or phone to delete: ")
    cursor.execute("CALL delete_by_value(%s);", (value,))
    conn.commit()
    print("deleted.")
def main():
    while True:
        print("1 - search by pattern")
        print("2 - insert or update user")
        print("3 - bulk insert from CSV")
        print("4 - paginate query")
        print("5 - delete user")
        print("6 - exit")
        choice = input("enter choice: ").strip()
        if choice == "1":
            search_by_pattern()
        elif choice == "2":
            upsert_user()
        elif choice == "3":
            bulk_insert_from_csv()
        elif choice == "4":
            paginate()
        elif choice == "5":
            delete_by_value()
        elif choice == "6":
            break
        else:
            print("Invalid")
    cursor.close()
    conn.close()
if __name__ == "__main__":
    main()
