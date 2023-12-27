import presenter
    
def user_interface():
    cmd = 0
    while cmd != '6':
        print('\nВыберите действие:\n'
            '1. Создать заметку\n'
            '2. Показать все заметки\n'
            '3. Найти заметку\n'
            '4. Редактировать заметку\n'
            '5. Удалить заметку\n'
            '6. Выход\n')
        cmd = input('Введите индекс: ')
        while cmd not in ('1','2','3','4','5','6'):
            print('Некоректный ввод')
            cmd = input('Введите индекс: ')
            
        match cmd:
            case '1': 
                presenter.add_note()
            case '2':
                presenter.print_data()
            case '3':
                presenter.search_note()
            case '4':
                presenter.change_note()
            case '5':    
                presenter.delete_note()
            case '6':    
                print('Всего доброго!')
                
def ask_info(text):
    return input(text)

def yes_no(text):
    print(f'{text} \n'
        '1. Да\n'
        '2. Нет\n')
    return int(input('=> '))

def create_request(request:str) -> int:
    print(f'{request}:\n'
        '1. ID\n'
        '2. Название заметки\n'
        '3. Текст заметки')
    index = int(input('Введите индекс: '))
    while index not in range(1,4):
        print('\nНекоректный ввод\n')
        index = int(input('Введите индекс: '))
    return index-1