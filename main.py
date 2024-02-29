from src.products import Product
from src.products import Smartphone
from src.products import LawnGrass


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
        # print(cat.products)
        for prd in cat.products:
            print(prd)
            print("   " + prd.description)
            print("   " + str(prd.price))
            print("   " + str(prd.quantity))

    prod = Product("Слон серый", "КУПИ! СЛОНАААА!!!!1111адыадын", 300000.0, 1)
    prod.price = 1000.0

    print(f"Цена по итогу: {prod}")

    sm = Smartphone('Xiaomi Redmi Note 11 (Pro)', '1024GB, Синий', 31000.0, 14,
                          'high', 'Xiaomi Redmi Note 11', '1024GB', 'Синий')

    lg = LawnGrass('Трава газонная голландская', 'Можно любоваться, можно курить', 7000.0,
                    22, 'Голландия', '2 недели', 'Темно-зеленый')


    print(f"\nSmartphone\n{sm}")
    print(f"\nLawnGrass\n{lg}")


if __name__ == '__main__':
    main()
