import mysql.connector

class BookListCreateRetrieveUpdateDelete:

    def __init__(self):
        self.connection=mysql.connector.connect(user='root',password='sandra',database='library1_db')

        print(self.connection)
        self.cursor=self.connection.cursor()
        print("sucessfully connected")
    def list(self):

        # reading all records from db table
        query="select* from book"
        # a=[]
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        
        if records:
            # for row in records:
            #     print(row)
            return records
        else:
            print("no records found")
    def create(self,title,author,language,price,pages):

        # creating a new record
        query="insert into book(title,author,language,price,pages)values(%s,%s,%s,%s,%s)"
        data=(title,author,language,price,pages)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("inserted data sucessfully")

    def retrieve(self,id):

        # read single record"
        query="select * from  book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            # print(record)
            return record
        else:
            print("no record found")

    def update(self,id,title,author,language,price,pages):
        query= "update book set title=%s,author=%s,language=%s,price=%s,pages=%s where id=%s"
        data=(title,author,language,price,pages,id)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
        #     print("updated sucessfully")
            return True
        else:
            # print("no record")
            return False

    def delete(self,id):
        query="delete from book where id= %s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            # print("deleted sucessfully")
            return True
        else:
            # print("no record found")
            return False

b=BookListCreateRetrieveUpdateDelete()

b.list()
# b.create(1,'ABC','john',300,500,'english')
# b.create(2,'XYZ','james',344,600,'english')
# b.retrieve(1)
# b.delete(4)
# b.update(2,'kMR','kein','hindi',789,546)
b.retrieve(2)