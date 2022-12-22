import pymysql
import os

class Student_source:

    def __int__(self):
        pass

    #@staticmethod
    def _get_connection(self):

        #usr = os.environ.get('DBUSER')
        #pw = os.environ.get('DBPW')
        #host = os.environ.get('DBHOST')

        conn = pymysql.connect(
            user="admin",
            password="dbuserdbuser",
            host="circuits.cdlehdu4ibgc.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    #@staticmethod
    def get_student(self,uni):

        sql = "SELECT * FROM f22_databases.students where uni = '%s'" % (uni);
        print(sql)
        conn = self._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql)
        result = cur.fetchall()
        if result:
            return result
        else:
            return "Nothing Found."

    #@staticmethod
    def append_new_student(self,data):
        if self.get_student(data['uni'])!="Nothing Found.":
            return ("already exist")
        sql = "INSERT INTO f22_databases.students VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)";
        conn = self._get_connection()
        cur = conn.cursor()
        try:
            conn.begin()
            res = cur.execute(sql, (data['auto_id'],data['last_name'],data['first_name'],data['middle_name'],data['email'],data['uni'],data['address_line1'],data['address_line2'],data['city'],data['state']))
            conn.commit()
            cur.close()
            conn.close()
            return "sucessfully add"
        except Exception as e:
            conn.rollback()
            return e

    #@staticmethod
    def delete_student(self,id):
        sql = "DELETE FROM f22_databases.students where uni = %s";
        conn = self._get_connection()
        cur = conn.cursor()
        try:
            conn.begin()
            res = cur.execute(sql, (id))
            conn.commit()
            cur.close()
            conn.close()
            return "Successfully deleted"
        except Exception as e:
            conn.rollback()
            return e

    #@staticmethod
    def update_student(self,data):
        sql = "UPDATE f22_databases.students set auto_id = %s, last_name = %s,first_name = %s,middle_name = %s,email = %s,address_line1 = %s,address_line2 = %s,city = %s,state = %s where uni = %s ;"
        conn = self._get_connection()
        cur = conn.cursor()
        print(sql)
        try:
            conn.begin()
            res = cur.execute(sql, (data['auto_id'],data['last_name'],data['first_name'],data['middle_name'],data['email'],data['address_line1'],data['address_line2'],data['city'],data['state'],data['uni']))
            conn.commit()
            cur.close()
            conn.close()
            return "successfully update"
        except Exception as e:
            conn.rollback()
            return e
