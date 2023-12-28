from datetime import datetime
import uuid

class Note:
        
    def __init__(self, id = str(uuid.uuid1())[0:2], 
                 title = "text", body = "text", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
    
    def set_id(self):
        self.id = str(uuid.uuid1())[0:2]
        
    def set_title(self, title):
        self.title = title
    
    def set_body(self, body):
        self.body = body
    
    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        
    def __str__(self):
        return 'ID: ' + self.id + '\nЗаголовок: ' + self.title + '\nЗаметка: ' + self.body + '\nДата создания или изменения: ' + self.date