from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Database...")
root.iconbitmap('gojo.ico')
root.geometry("400x400")

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
        print_record += str(record) + '\n'  # can also use record[0] to access only the first name and so on...

    Label(root, text=print_record).grid(row=8, column=0, columnspan=2)
    # commit changes to database
    conn.commit()
    # close connection
    conn.close()
    

# Enter the data
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

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

# Create the label for the entries
Label(root, text="Enter the first name: ").grid(row=0, column=0, sticky=W)
Label(root, text="Enter the last name: ").grid(row=1, column=0, sticky=W)
Label(root, text="Enter the address: ").grid(row=2, column=0, sticky=W)
Label(root, text="Enter the city: ").grid(row=3, column=0, sticky=W)
Label(root, text="Enter the state: ").grid(row=4, column=0, sticky=W)
Label(root, text="Enter the zipcode: ").grid(row=5, column=0, sticky=W)

# Create Submit button  
submit_button = Button(root, text="Add record to Database", command=Submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query button
query_button = Button(root, text="Show records", command=Query)
query_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# commit changes to database
conn.commit()

# close connection
conn.close()

root.mainloop()