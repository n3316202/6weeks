#https://velog.io/@su-mmer/Python-MySQL-CRUD-%ED%95%B4%EB%B3%B4%EA%B8%B0
import pymysql

class DBControl:
    
    def create(self):
        conn = pymysql.connect(host='', user='',
                       password='', db='', charset='utf8')

        try:
            curs = self.conn.cursor()
        
            sql = '''CREATE TABLE user (
            id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
            name varchar(255),
            email varchar(255)
            )
            '''
            
            curs.execute(sql)
            self.conn.commit()

        finally:
            conn.close()

    def insert(self):
        conn = pymysql.connect(host='', user='',
                       password='', db='', charset='utf8')

        try:
            curs = conn.cursor()
            sql = "INSERT INTO user VALUES (%s, %s, %s)"
            val = (1111, "kim", "google")
            curs.execute(sql, val)
            conn.commit()  

        finally:
            conn.close()
    

class VisualEx:
    def basic_example(self):
        path = 'static/plot_ex.png'
        plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
        plt.savefig(path)
        return path
    
        
