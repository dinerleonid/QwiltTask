class Logger:
    db_url = "url"
    db_name = "name"
    db_pass = "pass"
    db_handler = DB_SQL_DRIVER
    source = None
    def connect_to_db(self):
        db_handler.connect(db_url,db_name,db_pass)

    def log(self,msg):
        db_handler.insert(msg,"sucess")
        
    def error(self,msg):
        db_handler.insert(msg,"error")

    def __init__(self,source):
        self.source=source


