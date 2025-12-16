import requests
print("HelloWorld")


def Say_Hello(first_name, last_name):
    print(F"{first_name} - {last_name}")


Say_Hello("Adi", "Thakker")


discount = 10


def Change_Discount(discount):
    discount = 5
    return discount


result = Change_Discount(discount)
result


def Return_Tuple():
    return "Hello", "World"


greeting1, greeting2 = Return_Tuple()
print()
