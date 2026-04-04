from connect import get_connection

def call_upsert():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL upsert_contact(%s, %s, %s, %s)",
        ('Ali', 'Nurlanov', '87001234567', 'ali@mail.com')
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Upsert done!")


def search_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s)", ('Ali',))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def pagination():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (5, 0))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def bulk_insert():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_many_contacts(%s, %s, %s, %s)",
        (
            ['Dana', 'John'],
            ['Sadykova', 'Doe'],
            ['87001234567', 'abc123'],
            ['dana@mail.com', 'john@mail.com']
        )
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Bulk insert done!")


def delete_contact():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s)", ('Dana',))

    conn.commit()
    cur.close()
    conn.close()
    print("Delete done!")


if __name__ == "__main__":
    print("1 - Upsert")
    print("2 - Search")
    print("3 - Pagination")
    print("4 - Bulk Insert")
    print("5 - Delete")

    choice = input("Choose action: ")

    if choice == '1':
        call_upsert()
    elif choice == '2':
        search_contacts()
    elif choice == '3':
        pagination()
    elif choice == '4':
        bulk_insert()
    elif choice == '5':
        delete_contact()
    else:
        print("Invalid choice")