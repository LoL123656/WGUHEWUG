import requests
import json
import pprint


url = 'https://fakestoreapi.com/products/categories'
response = requests.get(url)
Category = response.json()
print(Category)

url2 = 'https://fakestoreapi.com/products'
response = requests.get(url2)
Products = response.json()

Choice_human = input('Товары какой категории Вы желаете посмотреть?: ')
find = False


    
for product in Products:
    if product['category'] == Choice_human:
       print(f'Айди:{product["id"]} Название:{product["title"]}')
       print(f'Цена:{product["price"]}\n Описание:{product["description"]}')
       print(f'Картинка:{product["image"]}\n Рэйтинг:{product["rating"]}')
       find = True

if not find:
    print(f'Товаров такой категории нет')



