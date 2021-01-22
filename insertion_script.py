import fdb

conn1 = fdb.connect(
    host="host1", database='database1.fdb', user='user', password='pasw')
cur1 = conn_eg.cursor()

conn2 = fdb.connect(
    host='host2', database='database2.fdb', user='user', password='pass')
# Cursor
cur2 = conn_sc.cursor()

cur_eg.execute("""SELECT column1,column2, 
        FROM table1 t1 
        JOIN table2 t2 ON t1.id=t2.id;""")
records = cur_eg.fetchall()

for r in records:
    if str(r[2]) == '':
        pass
    else:
        r1 = str(r[2])
        cur_sc.execute("""SELECT * FROM table2 WHERE column1 = ?""", (r1[4:], ))
        entry = cur_sc.fetchone()

        if entry is None:
            cur_sc.execute("""UPDATE OR INSERT INTO table3 (column1,column2)
                        VALUES (?,?) MATCHING (column1,column2);""",
                           (r1[4:], r[3]))
            print("Added")
        else:
            print("Found entry")
    if str(r[2]) == '':
        r1 = str(r[2])
        cur_sc.execute("""SELECT * FROM table3 WHERE object = ?""", (r[0],))
        entry = cur_sc.fetchone()

        if entry is None:
            cur_sc.execute("""UPDATE OR INSERT INTO table3 (column1,column2)
                                VALUES (?,?) MATCHING (column1,column2);""",
                           (r1[4:], r[3]))
            print("Added 1")
        else:
            print("Found entry 1")


conn1.commit()
conn2.commit()

conn1.close()
conn2.close()
