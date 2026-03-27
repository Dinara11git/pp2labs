# phonebook.py
from connect import get_connection
import csv

# ------------------------------
# Добавление контакта вручную
# ------------------------------
def add_contact():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contacts (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
        (first_name, last_name, phone, email)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Contact added!")

# ------------------------------
# Импорт контактов из CSV
# ------------------------------
def import_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    with open("contacts.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO contacts (first_name, last_name, phone, email) VALUES (%s, %s, %s, %s)",
                (row['first_name'], row['last_name'], row['phone'], row['email'])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("✅ CSV imported!")

# ------------------------------
# Показ всех контактов
# ------------------------------
def show_contacts():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# ------------------------------
# Поиск контактов
# ------------------------------
def search_contacts():
    field = input("Search by first_name, last_name, or phone: ").strip()
    value = input("Enter value to search: ").strip()

    if field not in ['first_name', 'last_name', 'phone']:
        print("❌ Invalid field")
        return

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM contacts WHERE {field} LIKE %s", (f"%{value}%",))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found.")
    cur.close()
    conn.close()

# ------------------------------
# Обновление контакта
# ------------------------------
def update_contact():
    contact_id = input("Enter ID of contact to update: ").strip()
    field = input("Which field to update? first_name, last_name, phone, email: ").strip()
    if field not in ['first_name', 'last_name', 'phone', 'email']:
        print("❌ Invalid field")
        return
    new_value = input("Enter new value: ").strip()

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE contacts SET {field}=%s WHERE id=%s", (new_value, contact_id))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Contact updated!")

# ------------------------------
# Удаление контакта
# ------------------------------
def delete_contact():
    contact_id = input("Enter ID of contact to delete: ").strip()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=%s", (contact_id,))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Contact deleted!")

# ------------------------------
# Главное меню
# ------------------------------
def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Add contact")
        print("2. Import from CSV")
        print("3. Show all contacts")
        print("4. Search contacts")
        print("5. Update contact")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            import_from_csv()
        elif choice == "3":
            show_contacts()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice")

# ------------------------------
# Запуск программы
# ------------------------------
if __name__ == "__main__":
    menu()