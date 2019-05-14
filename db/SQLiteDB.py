import sqlite3

class SQLiteDB:
    def __init__(self,dbfile):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()

    def query(self, query):
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result
    
    def insertOrUpdate(self,query,params):
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return self.cursor.lastrowid

    def execute(self,query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        
    

    def ifExists(self, tname):
        stmt =  "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(tname)
        self.cursor.execute(stmt)
        return self.cursor.fetchone()

    def queryAsDict(self, query):
        try:
            result = self.cursor.execute(query)
            rows = result.fetchall()
            desc = self.cursor.description
            l = []
            for x,row in enumerate(rows):
                d = {}
                #print(x,row)
                for idx, col in enumerate(desc):
                    d[col[0]] = row[idx]
                l.append(d)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return l


    def __del__(self):
        self.cursor.close()
        self.conn.close()
        
        