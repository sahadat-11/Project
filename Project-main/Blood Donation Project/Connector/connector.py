import pymysql
class Connector():
    def __init__(self):
        try:
            self.con= pymysql.connect(host = "localhost", user="root", password ="Mdfahim", db="blood")
            self.cur = self.con.cursor()
            print("Connection Successful")
        except Exception as e:
            print(e)

