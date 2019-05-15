from datetime import datetime

class NLPQuery:
    """NLPQuery is generic class to add queries

    Attributes:
        cm: Connection Manger for accessing DB function.    
    """

    def __init__(self,dbconn):
        """Constructor
        Args:
           dbconn: dbconnection after opening the DB.

        """
        self.cm = dbconn

    def add_query(self,params):
        """INSERT function
        Creates the table first if it does not exists.    
        Args:
           params: insert values in tuple format

        """
        self.createTable('query')

        sql = ''' INSERT INTO query(txt,post_date)
                VALUES(?,?) '''
        return self.cm.insertOrUpdate(sql,params)

    def createTable(self,tablename):
        """Create Table function
        Creates the table if it does not exists.    
        Args:
           tablename: name of the table

        """

        if not self.cm.ifExists(tablename):
            sql_create_table = """ CREATE TABLE IF NOT EXISTS query (
                                id integer PRIMARY KEY,
                                txt text NOT NULL,
                                post_date text
                            ); """
            return self.cm.query(sql_create_table)
            
    
    def selectAll(self):
        """Select * from table 
        Returns:
            All the rows in the table in list format

        """
        sql = ''' SELECT * from query '''
        result =  self.cm.query(sql).fetchall()
        return result

    def selectAllDict(self):
        """Select * from table 
        Returns:
            All the rows in the table in dict format with keys as 
            column name

        """
        
        sql = ''' SELECT * from query '''
        result =  self.cm.queryAsDict(sql)
        return result

    def resetAll(self):
        """Clear table 
        
        """
        
        sql = ''' Delete from query '''
        result =  self.cm.execute(sql)
        return result