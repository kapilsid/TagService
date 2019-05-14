from datetime import datetime

class NLPQuery:
    
    def __init__(self,dbconn):
        self.cm = dbconn

    def add_query(self,params):
        self.createTable('query')

        sql = ''' INSERT INTO query(txt,post_date)
                VALUES(?,?) '''
        return self.cm.insertOrUpdate(sql,params)

    def createTable(self,tablename):
        if not self.cm.ifExists(tablename):
            sql_create_table = """ CREATE TABLE IF NOT EXISTS query (
                                id integer PRIMARY KEY,
                                txt text NOT NULL,
                                post_date text
                            ); """
            return self.cm.query(sql_create_table)
            
    
    def selectAll(self):
        sql = ''' SELECT * from query '''
        result =  self.cm.query(sql).fetchall()
        return result

    def selectAllDict(self):
        sql = ''' SELECT * from query '''
        result =  self.cm.queryAsDict(sql)
        return result

    def resetAll(self):
        sql = ''' Delete from query '''
        result =  self.cm.execute(sql)
        return result