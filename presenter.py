from model import Model
import view

class Presenter:

    def __init__(self, file_name) -> None:
        self.file_name = file_name
        self.model = Model(file_name)
        self.view = view
    
    
    def add_note(self):
        title = self.view.View.ask_info(self, text = 'Введите название заметки: ')
        body = self.view.View.ask_info(self, text = 'Введите текст заметки: ')
        self.model.add_note(title, body)
        
    def print_data(self):
        self.model.print_data()
        
    def search_note(self):
        to_search = self.view.View.ask_info(self, text = 'Введите id или название заметки: ')
        self.model.search_note(to_search)
        
    def change_note(self):
        to_search = self.view.View.ask_info(self, text = 'Введите id или название заметки: ')
        index = self.view.View.create_request(self, 'Выберите что вы хотите изменить')
        new_info = self.view.View.ask_info(self, text = 'Введите новые данные: ')
        self.model.change_note(to_search, new_info, index)
        
    def delete_note(self):
        to_search = self.view.View.ask_info(self, text = 'Введите id или название заметки: ')
        choose = self.view.View.yes_no(self, text = 'Вы хотите удалить всю информацию из заметки?')
        if(choose == 2):
            index = self.view.View.create_request(self, 'Выберите что вы хотите удалить')
        else:
            index = None
        self.model.delete_note(to_search, choose, index)