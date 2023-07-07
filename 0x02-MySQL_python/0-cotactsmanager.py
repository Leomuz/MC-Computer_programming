import mysql.connector
import os

DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

database_connection = mysql.connector.connect(
    host="localhost",
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    database="contacts_manager"
)

def create_contact(name, email, phone):
    cursor = database_connection.cursor()
    query = "INSERT INTO contacts (name, email, phone) VALUES (%s, %s, %s)"
    values = (name, email, phone)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

create_contact("kemodes", "leomuz@gmail.com", "+260979807030")

def get_all_contacts():
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts"
    cursor.execute(query)
    row = cursor.fetchall()
    cursor.close()
    return row

contacts = get_all_contacts()
for contacts in contacts:
    print(contacts)

#updata the contacts
def update_contacts(contact_id, name, email, phone):
    cursor = database_connection.cursor()
    query = "UPDATE contacts SET name=%s, email=%s, phone=%s WHERE id=%s"
    values = (name, email, phone, contact_id)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()


update_contacts(1, "kemodes", "kemodesaretro@outlook.com", "+260979807030")

#Deletes a user
def delete_contacts(contact_id):
    cursor = database_connection.cursor()
    query = "DELETE FROM contacts WHERE id=%s"
    values = (contact_id,)
    cursor.execute(query, values)
    database_connection.commit()
    cursor.close()

delete_contacts(1)

# Gets a single User
def get_single_user(contact_id):
    cursor = database_connection.cursor()
    query = "SELECT * FROM contacts WHERE id=%s"
    values = (contact_id,)
    cursor.execute(query, values)
    rows = cursor.fetchone()
    cursor.close()
    return rows

contact = get_single_user(2)
print(contact)