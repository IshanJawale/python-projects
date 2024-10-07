from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import sqlite3
import os

root = Tk()
root.title("Update Record...")
root.iconbitmap('gojo.ico')
root.geometry("400x600")

# Create a database or connect to one
conn = sqlite3.connect("expense.db")

# Create a cursor
cur = conn.cursor()

# Create a table

def file_exists(file_name):
    return os.path.exists(file_name)

file_name = "expense.db"

if not file_exists(file_name):
    cur.execute("""CREATE TABLE expense (
            day integer,
            month integer,
            year integer,
            cost float
        )
    """)



# Create a function to update a record
def save_record():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("expense.db")
    # Create a cursor
    cur = conn.cursor()
    record_id = select_entry.get()
    cur.execute("""UPDATE expense SET
                day = :day,
                month = :month,
                year = :year,
                cost = :cost
                WHERE oid = :oid""",
                {
                    'day':day_editor.get(),
                    'month':month_editor.get(),
                    'year':year_editor.get(),
                    'cost':cost_editor.get(),
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
    conn = sqlite3.connect("expense.db")
    # Create a cursor
    cur = conn.cursor()

    record_id = select_entry.get()
    # Query the database
    cur.execute("SELECT * FROM expense WHERE oid = " + record_id)
    records = cur.fetchall()

    

    # Create editor entries global
    global day_editor
    global month_editor
    global year_editor
    global cost_editor
    
 

    # Enter the data
    day_editor= Entry(editor, width=30)
    day_editor.grid(row=0, column=1, padx=20, pady=(5, 0))

    month_editor = Entry(editor, width=30)
    month_editor.grid(row=1, column=1, padx=20)

    year_editor = Entry(editor, width=30)
    year_editor.grid(row=2, column=1, padx=20)

    cost_editor = Entry(editor, width=30)
    cost_editor.grid(row=3, column=1, padx=20)


    
    # Create the label for the entries
    Label(root, text="Enter the day: ").grid(row=0, column=0, pady=(5, 0), sticky=W)
    Label(root, text="Enter the month: ").grid(row=1, column=0, sticky=W)
    Label(root, text="Enter the year: ").grid(row=2, column=0, sticky=W)
    Label(root, text="Enter the expenditure: ").grid(row=3, column=0, sticky=W)
    
    # have the old data in entry box
    for record in records:
        day_editor.insert(0, record[0])
        month_editor.insert(0, record[1])
        year_editor.insert(0, record[2])
        cost_editor.insert(0, record[3])

    
    save_button = Button(editor, text="Save", command=save_record)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=130)

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

    # Clear existing label content
    record_label.config(text=" ")
    total_label.config(text=" ")
    

# Create function to delete a record
def delete():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("expense.db")
    # Create a cursor
    cur = conn.cursor()
    
    record_id = select_entry.get()
    # Query the database
    cur.execute("SELECT * FROM expense WHERE oid = " + record_id)
    records = cur.fetchall()

    

    # Delete a record
    cur.execute("DELETE from expense WHERE oid=" + select_entry.get())

    

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

    # Clear existing label content
    record_label.config(text=" ")
    total_label.config(text=" ")

# Create Submit Function
def Submit():
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("expense.db")
    # Create a cursor
    cur = conn.cursor()
    
    # Insert into table
    cur.execute("INSERT INTO expense VALUES (:day, :month, :year, :cost)",
                {
                    'day':day.get(),
                    'month':month.get(),
                    'year':year.get(),
                    'cost':cost.get()
                }
    )


    # commit changes to database
    conn.commit()
    # close connection
    conn.close()


    # Clear text boxes
    day.delete(0, END)
    month.delete(0, END)
    year.delete(0, END)
    cost.delete(0, END)

    total_label.config(text=" ")


# Create Query Function
def Query():
    global record_label
    
    # We've to always connect the database and create a cursor in the function
    # Create a database or connect to one
    conn = sqlite3.connect("expense.db")
    # Create a cursor
    cur = conn.cursor()

    # Query the database
    cur.execute("SELECT *, oid FROM expense")
    records = cur.fetchall()
    # print(records)

    print_record = ''
    for record in records:
        print_record += (str(record[0]) + "/" + str(record[1]) + "/" + str(record[2]) + " | expenditure: " + str(record[3]) + " | ID: " + str(record[4])) + '\n'  


    
    record_label = Label(root, text=print_record)
    record_label.grid(row=8, column=0, columnspan=2)
    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

total_cost = StringVar


def total(): 
    global total_label
    # Create a database or connect to one
    conn = sqlite3.connect("expense.db")
    # Create a cursor
    cur = conn.cursor()
    
    cur.execute("SELECT *, oid FROM expense")
    records = cur.fetchall()
    total_cost = 0
    for record in records:
        total_cost+= record[3]
    
    total_label = Label(root, text=total_cost)
    total_label.grid(row=14, column=0, columnspan=2)

    # commit changes to database
    conn.commit()
    # close connection
    conn.close()

# Enter the data
day = Entry(root, width=30)
day.grid(row=0, column=1, padx=20, pady=(5, 0))

month = Entry(root, width=30)
month.grid(row=1, column=1, padx=20)

year = Entry(root, width=30)
year.grid(row=2, column=1, padx=20)

cost = Entry(root, width=30)
cost.grid(row=3, column=1, padx=20)


select_entry = Entry(root, width=30)
select_entry.grid(row=9, column=1, padx=20)

# Create the label for the entries
Label(root, text="Enter the day: ").grid(row=0, column=0, pady=(5, 0), sticky=W)
Label(root, text="Enter the month: ").grid(row=1, column=0, sticky=W)
Label(root, text="Enter the year: ").grid(row=2, column=0, sticky=W)
Label(root, text="Enter the expenditure: ").grid(row=3, column=0, sticky=W)

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

total_cost_button = Button(root, text="Total Expenditure", command=total)
total_cost_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10, ipadx=140)
# commit changes to database
conn.commit()

# close connection
conn.close()

root.mainloop()