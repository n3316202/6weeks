#https://velog.io/@su-mmer/Python-MySQL-CRUD-%ED%95%B4%EB%B3%B4%EA%B8%B0
import pymysql
import pandas as pd

class DBExample:

    def show_table(self):    
        conn = pymysql.connect(
            user="root",
            password="1234",
            host="3.37.128.156", #localhost
            port=3306,
            database="scott"    
        )

        sql = 'SHOW TABLES'

        with conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                for data in cur:
                    print(data)


    def select_customers(self): 
        conn = pymysql.connect(
            user="root",
            password="1234",
            host="3.37.128.156", #localhost
            port=3306,
            database="scott"    
        ) 
        df = pd.read_sql_query("SELECT * FROM customers", conn)
        print(df) 
        return df
    
    def insert_customers(self,name,email): 
        conn = pymysql.connect(
            user="root",
            password="1234",
            host="3.37.128.156", #localhost
            port=3306,
            database="scott"    
        )
        # 커서 객체 생성
        cursor = conn.cursor()

        print(name,email)

        sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
        val = (name, email)
        cursor.execute(sql, val)

        conn.commit()
        print(cursor.rowcount, "record inserted")
        conn.close()

    def delete_customers(self,id): 
        conn = pymysql.connect(
            user="root",
            password="1234",
            host="3.37.128.156", #localhost
            port=3306,
            database="scott"    
        )
        # 커서 객체 생성
        cursor = conn.cursor()

        print(id)

        sql = "delete from customers where id = %s"
        val = (id)
        cursor.execute(sql, val)

        conn.commit()
        print(cursor.rowcount, "record inserted")
        conn.close()

  

    
    
        
