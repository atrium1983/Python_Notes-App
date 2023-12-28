import json
from note import Note

class Model:

    file_name: str

    def __init__ (self, file_name):
        self.file_name = file_name
            
    def add_note(self, title, body):
        new_note = Note()
        new_note.set_id()
        new_note.set_title(title)
        new_note.set_body(body)
        new_note.set_date()
        note_data = {
            'ID': new_note.id,
            'Title': new_note.title,
            'Note': new_note.body,
            'Date and time': new_note.date
            }
        try:
            self.save(note_data)
        except:
            print("Не удалось записать заметку")
           
    def save(self, note_data):
        data = self.get_notes()
        data.append(note_data)
        with open(self.file_name, 'w') as file:
            file.write(json.dumps(data, indent=4))

    def save_all(self, data):
        new_data = []
        for item in data:
            note_data = {
                'ID': item.id,
                'Title': item.title,
                'Note': item.body,
                'Date and time': item.date
                }
            new_data.append(note_data)
        with open(self.file_name, 'w') as file:
            file.write(json.dumps(new_data, indent=4))
    
    def get_notes(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
        except:
            data = []
        return data
        
    def load(self):
        try:
            with open(self.file_name, 'r') as file:
                data = json.load(file)
            notes = []
            for elem in data:
                note = Note()
                note.id = elem.get('ID')
                note.title = elem.get('Title')
                note.body = elem.get('Note')
                note.date = elem.get('Date and time')
                notes.append(note)
            return notes
        except:
            return []

    def print_data(self):
        data = self.load()
        for item in data:
            self.print_note(item)

    def print_note(self, item):
        print('')
        print(item)
        print('')
            
    def search_note(self, to_search):
        data = self.load()
        flag = True
        for item in data:
            if to_search == item.id or to_search == item.title:
                self.print_note(item)
                flag = False
        if flag: print(f'\nИнформация не найдена\n')
                    
    def change_note(self, to_search, new_info, index):
        data = self.load()
        flag = True
        for item in data:
            if to_search == item.id or to_search == item.title:
                match index:
                    case 0:
                        item.id = new_info
                    case 1:
                        item.title = new_info
                    case 2:
                        item.body = new_info
                item.set_date()
                self.print_note(item)
                flag = False
        self.save_all(data)
        if flag: print(f'\nИнформация не найдена\n')
            
    def delete_note(self, to_search, choose, index):
        data = self.load()
        if choose == 1:
            flag = True
            for item in data:
                if to_search == item.id or to_search == item.title:
                    flag = False
                    data.remove(item)
            self.save_all(data)
            if flag: print(f'\nИнформация не найдена\n')
            
        if choose == 2:
            flag = True
            for item in data:
                if to_search == item.id or to_search == item.title:
                    match index:
                        case 0:
                            item.id = '--'
                        case 1:
                            item.title = '-----'
                        case 2:
                            item.body = '-----------'
                    item.set_date()
                    flag = False
            self.save_all(data)
            if flag: print(f'\nИнформация не найдена\n')