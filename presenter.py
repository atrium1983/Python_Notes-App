import model
import view

    
def add_note():
    title = view.ask_info('Введите название заметки: ')
    body = view.ask_info('Введите текст заметки: ')
    model.add_note(title, body)
    
def print_data():
    model.print_data()
    
def search_note():
    index = view.create_request('Выберите вариант поиска')
    to_search = view.ask_info('Введите данные для поиска: ')
    model.search_note(index, to_search)
    
def change_note():
    to_search = view.ask_info('Введите id или название заметки: ')
    index = view.create_request('Выберите что вы хотите изменить')
    new_info = view.ask_info('Введите новые данные: ')
    model.change_note(to_search, new_info, index)
    
def delete_note():
    to_search = view.ask_info('Введите id или название заметки: ')
    choose = view.yes_no('Вы хотите удалить всю информацию из заметки?')
    if(choose == 2):
        index = view.create_request('Выберите что вы хотите удалить')
    else:
        index = None
    model.delete_note(to_search, choose, index)