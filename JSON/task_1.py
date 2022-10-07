# Дан джейсон файл, распарсить его и вывести все ключи
# со значением insert-update

import json


class File:
    def __init__(self, file_name, mode):
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        print('File opened')
        return self.file_obj

    def __exit__(self, type, value, traceback):
        print('File closed')
        self.file_obj.close()


if __name__ == '__main__':
    with File('10products.json', 'r') as file:
        products = file.read()
        products = json.loads(products)
        new_list = []
        i = 0
        for product in products:
            if product['action'] == 'insert-update':
                new_list.append(product)
            i += 1
        print(f'New_list: {new_list}')
        with open('text.txt', 'w+') as file_2t:
            file_2t.write(json.dumps(new_list))
    with open('text.txt', 'r') as file_2t:
        print(file_2t.read())
