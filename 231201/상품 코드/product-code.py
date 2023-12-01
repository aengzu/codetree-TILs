class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

name, code = tuple(input().split())
code = int(code)

product1 = Product("codetree",50)
product2 = Product(name, code)

print(f"product {product1.code} is {product1.name}")
print(f"product {product2.code} is {product2.name}")