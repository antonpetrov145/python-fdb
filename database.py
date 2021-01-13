from tkinter import *
import fdb

root = Tk()
root.title('Database management')

#  Databases

# Create Database or connect to one
conn = fdb.connect(
    host="localhost", database='database.fdb', user='user', password='password')

#  Create cursor
cur = conn.cursor()


#  Create table
#  cur.execute(""" CREATE TABLE users (
#  first_name VARCHAR(50),
#  last_name VARCHAR(50),
#  password VARCHAR(50)
#  )""")

#  Create Submit Function
#  simnumbber = "SIM NUMBER"


def submit():
    #  Database connection in the function
    conn = fdb.connect(
        host='localhost', database='database.fdb', user='user', password='password')
    # Cursor
    cur = conn.cursor()

    # Insert Into table
    cur.execute("""INSERT INTO cards (number,"SIM NUMBER",OPERATOR,TYPE,TARIFF,DATA,STATUS) VALUES (?,?,?,?,?,?,?);""",
                (simnumber.get(), cardnumber.get(), operator.get(), type.get(), tariff.get(), data.get(), status.get()))
    ''' '#  {
#	'number':simnumber.get(),
#	'simnumber': cardnumber.get(),
#	'operator': operator.get(),
#	'type': type.get(),
#	'tariff': tariff.get(),
#	'data': data.get(),
#	'status': status.get() 
#  }) '''

    # Commit Cahanges
    conn.commit()
    # Close connection
    conn.close()

    # Clear Textboxes
    simnumber.delete(0, END)
    cardnumber.delete(0, END)
    operator.delete(0, END)
    type.delete(0, END)
    tariff.delete(0, END)
    data.delete(0, END)
    status.delete(0, END)


#  Create Select Function

def select():
    #  Database connection in the function
    conn = fdb.connect(
        host='localhost', database='database.fdb', user='user', password='password')
    # Cursor
    cur = conn.cursor()

    cur.execute("""SELECT number, "SIM NUMBER", operator FROM cards;""")
    #  cur.fetchall -- показва всички
    #  cur.fetchone -- показва един запис
    #  cur.fetchmany() -- показва записи на брой в скобите
    records = cur.fetchmany(10)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    select_label = Label(root, text=print_records)
    select_label.grid(row=9, column=0, columnspan=2)

    # Commit Cahanges
    conn.commit()
    # Close connection
    conn.close()


#  Create Text boxes

simnumber = Entry(root, width=30)
simnumber.grid(row=0, column=1, padx=20)
cardnumber = Entry(root, width=30)
cardnumber.grid(row=1, column=1)
operator = Entry(root, width=30)
operator.grid(row=2, column=1)
type = Entry(root, width=30)
type.grid(row=3, column=1)
tariff = Entry(root, width=30)
tariff.grid(row=4, column=1)
data = Entry(root, width=30)
data.grid(row=5, column=1)
status = Entry(root, width=30)
status.grid(row=6, column=1)

#  Create labels for text boxes

simnumber_label = Label(root, text="СИМ Номер")
simnumber_label.grid(row=0, column=0)
cardnumber_label = Label(root, text="Карта Номер")
cardnumber_label.grid(row=1, column=0)
operator_label = Label(root, text="Оператор")
operator_label.grid(row=2, column=0)
type_label = Label(root, text="Вид")
type_label.grid(row=3, column=0)
tariff_label = Label(root, text="План")
tariff_label.grid(row=4, column=0)
data_label = Label(root, text="Потребление")
data_label.grid(row=5, column=0)
status_label = Label(root, text="Статус")
status_label.grid(row=6, column=0)

#  Create Submit Button

submit_btn = Button(root, text="Запиши", command=submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#  Create Select Button 
select_btn = Button(root, text="Виж Всички", command=select)
select_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#  Commit changes
conn.commit()

# Close connection
conn.close()

root.mainloop()
