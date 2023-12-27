from datetime import datetime
import json
import uuid

class Note:
    def __init__(self, id = str(uuid.uuid1())[0:2], 
                 title = "text", body = "text", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
    
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_body(self):
        return self.body
    
    def get_date(self):
        return self.date
    
    def set_id(self):
        self.id = str(uuid.uuid1())[0:2]
        
    def set_title(self, title):
        self.title = title
    
    def set_body(self, body):
        self.body = body
    
    def set_date(self):
        self.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
        
    def __str__(self):
        return '\n Заголовок: ' + self.title + '\n Заметка: ' + self.body + '\n Дата создания или изменения: ' + self.date