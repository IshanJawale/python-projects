from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Update Record...")
root.iconbitmap('gojo.ico')
root.geometry("400x600")

# Create a database or connect to one
conn = sqlite3.connect("address_book.db")

# Create a cursor
cur = conn.cursor()

# Create a table
'''
cur.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )
""")
'''

# Create a function to update a record
def save_record():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create a cursor
    cur = conn.cursor()
    record_id = select_entry.get()
    cur.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                WHERE oid = :oid""",
                {
                    'first':f_name_editor.get(),
                    'last':l_name_editor.get(),
                    'address':address_editor.get(),
                    'city':city_editor.get(),
                    'state':state_editor.get(),
                    'zipcode':zipcode_editor.get(),
                    'oid':record_id
                }
                )

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()
    editor.destroy()

def update():
    global editor
    editor = Toplevel()
    editor.title("Update Record Window")
    editor.iconbitmap('gojo.ico')
    editor.geometry("350x250")

    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create a cursor
    cur = conn.cursor()

    record_id = select_entry.get()
    # Query the database
    cur.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cur.fetchall()

    # Create editor entries global
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
 

    # Enter the data
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(5, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1, padx=20)

    
    # Create the label for the entries
    Label(editor, text="Enter the first name: ").grid(row=0, column=0, pady=(5, 0), sticky=W)
    Label(editor, text="Enter the last name: ").grid(row=1, column=0, sticky=W)
    Label(editor, text="Enter the address: ").grid(row=2, column=0, sticky=W)
    Label(editor, text="Enter the city: ").grid(row=3, column=0, sticky=W)
    Label(editor, text="Enter the state: ").grid(row=4, column=0, sticky=W)
    Label(editor, text="Enter the zipcode: ").grid(row=5, column=0, sticky=W)
    
    # have the old data in entry box
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    
    save_button = Button(editor, text="Save", command=save_record)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

# Create function to delete a record
def delete():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create a cursor
    cur = conn.cursor()
    
    # Delete a record
    cur.execute("DELETE from addresses WHERE oid=" + select_entry.get())

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

# Create Submit Function
def Submit():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create a cursor
    cur = conn.cursor()
    
    # Insert into table
    cur.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    'f_name':f_name.get(),
                    'l_name':l_name.get(),
                    'address':address.get(),
                    'city':city.get(),
                    'state':state.get(),
                    'zipcode':zipcode.get()
                }
    )

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()


    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Query Function
def Query():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("address_book.db")
    # Create a cursor
    cur = conn.cursor()

    # Query the database
    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    # print(records)

    print_record = ''
    for record in records:
        print_record += str(record[0]) + " " + str(record[1]) + " " + str(record[6]) + '\n'  

    Label(root, text=print_record).grid(row=8, column=0, columnspan=2)
    # commit changes to database
    conn.commit()
    # close connection
    conn.close()
    

# Enter the data
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(5, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

select_entry = Entry(root, width=30)
select_entry.grid(row=9, column=1, padx=20)

# Create the label for the entries
Label(root, text="Enter the first name: ").grid(row=0, column=0, pady=(5, 0), sticky=W)
Label(root, text="Enter the last name: ").grid(row=1, column=0, sticky=W)
Label(root, text="Enter the address: ").grid(row=2, column=0, sticky=W)
Label(root, text="Enter the city: ").grid(row=3, column=0, sticky=W)
Label(root, text="Enter the state: ").grid(row=4, column=0, sticky=W)
Label(root, text="Enter the zipcode: ").grid(row=5, column=0, sticky=W)
Label(root, text="Select ID: ").grid(row=9, column=0, sticky=W)

# Create Submit button  
submit_button = Button(root, text="Add record to Database", command=Submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query button
query_button = Button(root, text="Show records", command=Query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create a Delete button
delete_button = Button(root, text="Delete a record", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# Create an Update button
edit_button = Button(root, text="Update a record", command=update)
edit_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# commit changes to database
conn.commit()

# close connection
conn.close()

root.mainloop()