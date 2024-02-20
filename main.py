from src.products import Product

from src.json_parser import file_exist
from src.json_parser import load_json
from src.json_parser import json_parse


def main():
    json_data = []
    if file_exist('products.json'):
        json_data = load_json(file_exist('products.json'))

    if json_data is None:
        quit(1)

    print(json_data)

    category_list = json_parse(json_data)

    for cat in category_list:
        print(cat.title)
        print(cat.description)
        print(cat.products)
        for prd in cat.products:
            print("   " + prd.title)
            print("   " + prd.description)
            print("   " + str(prd.price))
            print("   " + str(prd.quantity))

    prod = Product("Слон серый", "КУПИ! СЛОНАААА!!!!1111адыадын", 300000.0, 1)
    prod.price = 1000.0

    print(f"Цена по итогу: {prod}")


if __name__ == '__main__':
    main()
