from application import mysql, session

class. Table():
    def __init__(self, table_name, *args):
        self.table = table_name
        self.columns = "(%s)" %",".join(args)

        if isnewtable(table_name):
            cur = mysql.connection.cursor()
            cur.execute("CREATE TABLE %s%s" %(self.table, self.columns))
            cur.close()

    def isnewtable(tableName):
        cur = mysql.connection.cursor()

        try:
            result = cur.execute("SELECT * from %s" %istablename)
            cur.close()
        except:
            return True
