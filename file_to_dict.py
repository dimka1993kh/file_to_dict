with open('recipes.txt', 'r',  encoding='utf-8') as f:
    cook_book = dict() # создаем пустой словарь
    # Функция, позволяющая создать однотипные словари внутри основного
    def create_standart_dict(): 
        data = f.readline().split(' | ')
        return {'ingredient_name': data[0], 
                'quantity': int(data[1]), 
                'measure': data[2][:-1]}

    # Пока файл, с которго мы читаем информацию, не закончится, будем добавлять 
    # в словарь cook_book пары ключ-значение
    work = True
    while work:
        key = f.readline().split()
        if key == []:
            break
        value = [create_standart_dict() for i in range(int(f.readline()))]
        f.readline() # Пропускаем пустую строку
        cook_book.update({' '.join(key): value})
    
# print(cook_book)

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

# ВНИМАНИЕ. Для проверки строк 33-34 (сложение одинаковых позиций) в файле recipes.txt в омлет добавлено 10 кг картохи :)

def get_shop_list_by_dishes(dishes, person_count):
    result_dict = dict() # Создадим пустой результирующий словарь
    for dish in dishes:
        for ingr in cook_book[dish]:
            # При условии, что ингридиент повторяется => плюсуем к старому значению
            if ingr['ingredient_name'] in list(result_dict.keys()): 
                result_dict[ingr['ingredient_name']]['quantity'] += person_count * ingr['quantity']
            # Иначе, добовляем в result_dict новую пару ключ-значение
            else:
                result_dict.update({ingr['ingredient_name'] : {'measure' : ingr['measure'], 'quantity': person_count * ingr['quantity']}})
    return(result_dict)
       
print(get_shop_list_by_dishes(dishes, person_count))



