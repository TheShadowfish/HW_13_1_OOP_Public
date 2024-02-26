**Задание 1**

Для магазина необходимо выделить две категории товаров и создать под них классы.

**Смартфон**

Помимо имеющихся свойств, необходимо добавить следующие:

- производительность,
- модель,
- объем встроенной памяти,
- цвет.
- 
**Трава газонная**

Помимо имеющихся свойств, необходимо добавить следующие:

- страна-производитель,
- срок прорастания,
- цвет.
- 
Для этих классов сделать класс **Product** из прошлых заданий базовым, 
а новые два класса должны быть наследниками.

При этом у продуктов должна оставаться категория, в которой товары, не относящиеся к двум указанным классам, должны храниться как объект класса продукта, который вы реализовали ранее.

Не забудьте проверить, что весь функционал, реализованный ранее, остался работоспособным после внесения этих правок.

 
**Задание 2**

Доработать функционал сложения таким образом, чтобы можно было складывать 
товары только из одинаковых классов продуктов. 
То есть если складывать товар класса «Смартфон» и товар класса «Продукт», 
то должна быть ошибка типа.

В данном случае попробуйте воспользоваться функцией **type()**.


**Задание 3**

Доработайте метод добавления продукта в категорию таким образом, 
чтобы не было возможности добавить вместо продукта или его наследников
любой другой объект.

* **Дополнительное задание (к заданию 3)**

На этот функционал напишите тесты.