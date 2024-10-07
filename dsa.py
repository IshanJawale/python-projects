import sqlite3
from tkinter import simpledialog, messagebox
import tkinter as tk

class PhoneBook:
    def __init__(self, db_filename='phonebook.db'):
        self.db_filename = db_filename
        self.connection = sqlite3.connect(db_filename)
        self.cursor = self.connection.cursor()
        self.initialize_database()

    def initialize_database(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone_number TEXT NOT NULL
        );
        '''
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def add_contact(self, name, phone_number):
        insert_query = "INSERT INTO contacts (name, phone_number) VALUES (?, ?)"
        self.cursor.execute(insert_query, (name, phone_number))
        self.connection.commit()

    def get_contacts(self):
        select_query = "SELECT name, phone_number FROM contacts"
        self.cursor.execute(select_query)
        return self.cursor.fetchall()

    def search_contact(self, name):
        select_query = "SELECT name, phone_number FROM contacts WHERE name = ?"
        self.cursor.execute(select_query, (name,))
        return self.cursor.fetchone()

    def delete_contact(self, name):
        delete_query = "DELETE FROM contacts WHERE name = ?"
        self.cursor.execute(delete_query, (name,))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def sort_contacts(self):
        select_query = "SELECT id, name, phone_number FROM contacts ORDER BY name"
        sorted_contacts = self.cursor.execute(select_query).fetchall()
        update_query = "UPDATE contacts SET name = ?, phone_number = ? WHERE id = ?"
        for index, contact in enumerate(sorted_contacts, start=1):
            self.cursor.execute(update_query, (contact[1], contact[2], index))
        self.connection.commit()

    def __del__(self):
        self.connection.close()

class PhoneBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Phone Book App")

        self.phone_book = PhoneBook()

        self.label = tk.Label(master, text="Phone Book Operations:")
        self.label.pack()

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack()

        self.display_button = tk.Button(master, text="Display Contacts", command=self.display_contacts)
        self.display_button.pack()

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.pack()

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack()

        self.sort_button = tk.Button(master, text="Sort Contacts", command=self.sort_contacts)
        self.sort_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=self.master.destroy)
        self.exit_button.pack()

    def add_contact(self):
        name = self.get_user_input("Enter name:")
        phone_number = self.get_user_input("Enter phone number:")
        self.phone_book.add_contact(name, phone_number)
        self.show_message("Contact added successfully!")

    def display_contacts(self):
        contacts = self.phone_book.get_contacts()
        if not contacts:
            self.show_message("Phone book is empty.")
        else:
            message = "Contacts in the phone book:\n"
            for contact in contacts:
                message += f"Name: {contact[0]}\tPhone Number: {contact[1]}\n"
            self.show_message(message)

    def search_contact(self):
        name = self.get_user_input("Enter the name to search:")
        contact = self.phone_book.search_contact(name)
        if contact:
            message = f"Contact found!\nName: {contact[0]}\tPhone Number: {contact[1]}"
            self.show_message(message)
        else:
            self.show_message("Contact not found.")

    def delete_contact(self):
        name = self.get_user_input("Enter the name to delete:")
        if self.phone_book.delete_contact(name):
            self.show_message("Contact deleted successfully!")
        else:
            self.show_message("Contact not found.")

    def sort_contacts(self):
        self.phone_book.sort_contacts()
        self.show_message("Phone book sorted successfully!")

    def get_user_input(self, prompt):
        return simpledialog.askstring("Input", prompt)

    def show_message(self, message):
        messagebox.showinfo("Message", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhoneBookApp(root)
    root.mainloop()
