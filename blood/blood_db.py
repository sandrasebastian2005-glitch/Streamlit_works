import mysql.connector

class BloodAddUpdateRetrieveDelete:

    def __init__(self):
        self.con=mysql.connector.connect(user="root",password="sandra",host="localhost",database="blood_db")
        print(self.con)
        self.c=self.con.cursor()
        print("Successfully Connected")

    def add(self,name,bloodgroup,phone,city,last_donation):
        query="insert into donor(name,bloodgroup,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
        data=(name,bloodgroup,phone,city,last_donation)
        self.c.execute(query,data)
        self.con.commit()
        print("inserted data sucessfully")

    def list(self):
        query="select * from donor"
        self.c.execute(query)
        records=self.c.fetchall()
        if records:
            return records
        else:
            print("No records found")

    def retrieve(self,id):
        query="select * from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            return record
        else:
            print("No records found")

    def update(self,id,name,bloodgroup,phone,city,last_donation):
        query="update donor set name=%s,bloodgroup=%s,phone=%s,city=%s,last_donation=%s where id=%s"
        data=(name,bloodgroup,phone,city,last_donation,id)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.c.execute(query,data)
        self.con.commit()
        if self.c.rowcount>0:
            return True
        else:
            return False

b=BloodAddUpdateRetrieveDelete()
b.list()
# b.add("sandra","B+ve","9087456320","ekm","2026-09-20")
# b.add("fathima","O+ve","908339032","ekm","2026-08-03")
# b.add("sabana","AB-ve","8807456320","tvm","2025-10-12")
b.retrieve(2)




