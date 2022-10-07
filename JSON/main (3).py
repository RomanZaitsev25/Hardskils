import json

#
# class OpenFile:
#     def __init__(self, file_name, mode):
#         self.file_obj = open(file_name, mode)
#
#     def __enter__(self):
#         return self.file_obj
#
#     def __exit__(self, type, value, traceback):
#         self.file_obj.close()


if __name__ == '__main__':
    with open("10products.json", "r") as file:
        products = file.read()
        products = json.loads(products)

        new_list = []
        i = 0
        for product in products:
            if product['action'] == 'insert-update':
                new_list.append(product)
            i += 1

        print(new_list)

    #     with open("text.txt", "w+") as file_wr:
    #         file_wr.write(json.dumps(products[0]['action']))
    #
    # with open("text.txt", "r+") as file_wr:
    #     print((file_wr.read()))
    #
    # with open("10products.json", "r+") as file:
    #     products = file.read()
    #     products = json.loads(products)
    #     with open("text.txt", "a+") as file_1:
    #         file_1.write(json.dumps(products[1]['action']))
    #
    # with open("text.txt", "r+") as file_1:
    #     print((file_1.read()))
    #
    # with open("10products.json", "r+") as file:
    #     products = file.read()
    #     products = json.loads(products)
    #     with open("text.txt", "a+") as file_1:
    #         file_1.write(json.dumps(products[3]['action']))
    #
    # with open("text.txt", "r+") as file_1:
    #     print((file_1.read()))