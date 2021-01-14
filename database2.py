from tkinter import *
from tkinter import ttk
import fdb


class Database:
    def __init__(self, master):
        top_frame = Frame(master)
        top_frame.pack()
        bottom_frame = Frame(master)
        bottom_frame.pack()
        self.tree = ttk.Treeview(bottom_frame)
        self.tree.pack()

        self.simnumber_label = Label(top_frame, text='СИМ Номер')
        self.simnumber_label.grid(row=0, column=0)
        self.simnumber = Entry(top_frame, width=30)
        self.simnumber.grid(row=0, column=1, padx=20, pady=5)

        self.cardnumber_label = Label(top_frame, text='Карта Номер')
        self.cardnumber_label.grid(row=0, column=2)
        self.cardnumber = Entry(top_frame, width=30)
        self.cardnumber.grid(row=0, column=3, padx=20, pady=5)

        self.operator_label = Label(top_frame, text='Оператор')
        self.operator_label.grid(row=1, column=0)
        self.operator = Entry(top_frame, width=30)
        self.operator.grid(row=1, column=1, padx=20, pady=5)

        self.type_label = Label(top_frame, text='Вид')
        self.type_label.grid(row=1, column=2)
        self.type = Entry(top_frame, width=30)
        self.type.grid(row=1, column=3, padx=20, pady=5)

        self.tariff_label = Label(top_frame, text='План')
        self.tariff_label.grid(row=2, column=0)
        self.tariff = Entry(top_frame, width=30)
        self.tariff.grid(row=2, column=1, padx=20, pady=5)

        self.data_label = Label(top_frame, text='Потребление')
        self.data_label.grid(row=2, column=2)
        self.data = Entry(top_frame, width=30)
        self.data.grid(row=2, column=3, padx=20, pady=5)

        self.status_label = Label(top_frame, text='Статус')
        self.status_label.grid(row=3, column=0)
        self.status = Entry(top_frame, width=30)
        self.status.grid(row=3, column=1, padx=20, pady=5)

        #  Buttons
        self.submit_btn = Button(top_frame, text="Нова Карта", command=self.submit)
        self.submit_btn.grid(row=4, column=0, columnspan=1, pady=10, padx=10, ipadx=20)

        self.select_btn = Button(top_frame, text="Виж Всички", command=self.select)
        self.select_btn.grid(row=4, column=1, columnspan=1, pady=10, padx=10, ipadx=20)

        self.quit_btn = Button(top_frame, text="Изход", command=top_frame.quit)
        self.quit_btn.grid(row=4, column=3, columnspan=1, pady=10, padx=10, ipadx=40)

        self.search_btn = Button(top_frame, text="Търсене", command=self.search)
        self.search_btn.grid(row=4, column=2, columnspan=1, pady=10, padx=10, ipadx=30)

        #  Treeview Columns
        self.tree['columns'] = ("СИМ Номер", "Карта Номер", "Оператор", "Вид", "План", "Потребление", "Статус")
        #  Format Columns
        self.tree.column("#0", width=0)
        self.tree.column("СИМ Номер", anchor=CENTER, width=120, minwidth=20)
        self.tree.column("Карта Номер", anchor=CENTER, width=150, minwidth=20)
        self.tree.column("Оператор", anchor=CENTER, width=120, minwidth=20)
        self.tree.column("Вид", anchor=CENTER, width=120, minwidth=20)
        self.tree.column("План", anchor=CENTER, width=120, minwidth=20)
        self.tree.column("Потребление", anchor=CENTER, width=120, minwidth=20)
        self.tree.column("Статус", anchor=CENTER, width=120, minwidth=20)
        #  Headings
        self.tree.heading("#0", text="")
        self.tree.heading("СИМ Номер", text="СИМ Номер", anchor=CENTER)
        self.tree.heading("Карта Номер", text="Карта Номер", anchor=CENTER)
        self.tree.heading("Оператор", text="Оператор", anchor=CENTER)
        self.tree.heading("Вид", text="Вид", anchor=CENTER)
        self.tree.heading("План", text="План", anchor=CENTER)
        self.tree.heading("Потребление", text="Потребление", anchor=CENTER)
        self.tree.heading("Статус", text="Статус", anchor=CENTER)

    #  Create Submit Function
    def submit(self):
        #  Database connection in the function
        conn = fdb.connect(
            host='localhost', database='database.fdb', user='user', password='password')
        # Cursor
        cur = conn.cursor()

        # Insert Into table
        cur.execute(
            """INSERT INTO cards (number,"SIM NUMBER",OPERATOR,TYPE,TARIFF,DATA,STATUS) VALUES (?,?,?,?,?,?,?);""",
            (
                self.simnumber.get(), self.cardnumber.get(), self.operator.get(), self.type.get(), self.tariff.get(), self.data.get(),
                self.status.get()))
        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

        # Clear Textboxes
        self.simnumber.delete(0, END)
        self.cardnumber.delete(0, END)
        self.operator.delete(0, END)
        self.type.delete(0, END)
        self.tariff.delete(0, END)
        self.data.delete(0, END)
        self.status.delete(0, END)

    #  Create Select Function

    def select(self):
        #  Database connection in the function
        conn = fdb.connect(
            host='localhost', database='database.fdb', user='user', password='password')
        # Cursor
        cur = conn.cursor()

        cur.execute("""SELECT number, "SIM NUMBER", operator FROM cards;""")
        #  cur.fetchall -- показва всички
        #  cur.fetchone -- показва един запис
        #  cur.fetchmany() -- показва записи на брой в скобите
        records = cur.fetchmany(20)

        # Loop through results
        print_records = ''
        for record in records:
            print_records += str(record) + "\n"
            self.tree.insert("", END, values=record)

        #  select_label = Label(root, text=print_records)
        #  select_label.grid(row=9, column=0, columnspan=2)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    def search(self):
        conn = fdb.connect(
            host='localhost', database='database.fdb', user='user', password='password')
        # Cursor
        cur = conn.cursor()
        cur.execute("""SELECT number, "SIM NUMBER", operator 
                    FROM cards WHERE number LIKE (?);""", (self.simnumber.get(),))

        records2 = cur.fetchall()

        print_records2 = ''
        for record2 in records2:
            print_records2 += str(record2) + "\n"
            self.tree.insert("", END, values=record2)
        conn.commit()
        conn.close()


root = Tk()
root.title('Database Management')
#  Connect to Database
conn = fdb.connect(
    host="localhost", database='database.fdb', user='user', password='password')
#  Create cursor
cur = conn.cursor()

d = Database(root)

#  Commit changes
conn.commit()
# Close connection
conn.close()
root.mainloop()
