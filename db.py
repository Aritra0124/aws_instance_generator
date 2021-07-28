import pymysql
from pymysql.err import DatabaseError

class database:
    db = None
    def connectDB(self, host, userName, password, database):
        self.db = pymysql.connect(host = host, user = userName, password = password, database = database)
        if self.db != None:
            print("Connected")
    def disconnectDB(self):
        if self.db == None:
            print("No database connected...!!!")
        else:
            self.db.close()
            print("Disconnected...!!!")

    def insertDetailsDB(self, name, age, gender):
        cursor = self.db.cursor()
        sql = "insert into user_details values(0, %s, %s, %s,NOW())"
        try:
            cursor.execute(sql, (name, age, gender))
            k = cursor.lastrowid
            self.db.commit()
            print("Succesfully inserted")
            return k
        except DatabaseError as e:
            print("Erro while insert operation\n")
            print(e)

        
    def insertHealthDB(self, id, spo2, heart_rate, ecg):
        cursor = self.db.cursor()
        sql = "insert into health_data values(0, %s, %s, %s, %s, NOW())"
        try:
            cursor.execute(sql, (id, spo2, heart_rate, ecg))
            k = cursor.lastrowid
            self.db.commit()
            print("Succesfully inserted")
            return k


        except DatabaseError as e:
            print("Erro while insert operation\n")
            print(e)


    





