from Note import Note   

note = Note()
        
def add_note(title, body):
    new_note = Note()
    new_note.set_id()
    new_note.set_title(title)
    new_note.set_body(body)
    new_note.set_date()
    with open('notes.json', 'a', encoding='utf-8') as file:
        file.write(f'{new_note.id} {new_note.title} {new_note.body} {new_note.date}\n\n')

def print_note(item):
    print('')
    print(item)
    print('')
            
def print_data():
    with open('notes.json', 'r', encoding='utf-8') as file:
        to_print = file.read().strip().split('\n\n')
        for item in to_print:
            print_note(item)
        
def search_note(index, to_search):
    with open('notes.json', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        flag = True
        for item in data:
            new_item = item.split()
            if to_search == new_item[index]:
                print_note(item)
                flag = False
        if flag: print(f'\nИнформация не найдена\n')
                
def change_note(to_search, new_info, index):
    with open('notes.json', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    with open('notes.json', 'w', encoding='utf-8') as file:
        flag = True
        for item in data:
            new_item = item.split()
            if to_search == new_item[0] or to_search == new_item[1]:
            # if to_search in item:
                new_item[index] = new_info
                new_note = Note()
                new_note.id = new_item[0]
                new_note.title = new_item[1]
                new_note.body = new_item[2]
                new_note.set_date()
                flag = False
                file.write(f'{new_note.id} {new_note.title} {new_note.body} {new_note.date}\n\n')
            else:
                file.write(f'{new_item[0]} {new_item[1]} {new_item[2]} {new_item[3]} {new_item[4]}\n\n')
        if flag: print(f'\nИнформация не найдена\n')
        
def delete_note(to_search, choose, index):
    with open('notes.json', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    with open('notes.json', 'w', encoding='utf-8') as file:
        if choose == 1:
            flag = True
            for item in data:
                new_item = item.split()
                if to_search == new_item[0] or to_search == new_item[1]:
                    flag = False
                else:
                    item = ' '.join(new_item)
                    file.write(f'{item}\n\n')
            if flag: print(f'\nИнформация не найдена\n')
            
        if choose == 2:
            flag = True
            for item in data:
                new_item = item.split()
                if to_search == new_item[0] or to_search == new_item[1]:
                    new_item[index] = '-----'
                    print_note(' '.join(new_item))
                    flag = False
                item = ' '.join(new_item)
                file.write(f'{item}\n\n')
            if flag: print(f'\nИнформация не найдена\n')