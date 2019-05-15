import sqlite3

class SQLiteDB:
    """SQLiteDB is sqlite specific class for inetarcting with SQLite. 

    Attributes:
        conn: DB Connection
        cursor: cursor for the database access.    
    """

    def __init__(self,dbfile):
        """Constructor
        Args:
           dbfile: name of sqlite db file

        """
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()

    def query(self, query):
        """Query function
        Args:
           query: Select query

        Returns:
           The result in list format.     
        """
        try:
            result = self.cursor.execute(query)
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return result
    
    def insertOrUpdate(self,query,params):
        """Modify function 
        Args:
           query: Insert or Update
           params: insert values in tuple format

        Returns:
           The last updated row-id.     
        """
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        else:
            return self.cursor.lastrowid

    def execute(self,query):
        """General Execute function for DDL 
        Args:
           query: DDL queries
     
        """
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as error:
            print('error execting query "{}", error: {}'.format(query, error))
            return None
        
    

    def ifExists(self, tname):
        """Checks for table exists 
        Args:
           tname: table name

        Returns:
           None if table does not exists 
        """
        stmt =  "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(tname)
        self.cursor.execute(stmt)
        return self.cursor.fetchone()

    def queryAsDict(self, query):
        """Query function
        Args:
           query: Select query

        Returns:
           The result in dictionay format with keys as column of the table.     
        """
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
        """Destructor closes the cursor and connection. 
        """
        
        self.cursor.close()
        self.conn.close()
        
        