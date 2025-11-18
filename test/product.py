class Product:

    def __init__(self, name, price):
        #print("Меня создали!")
        #print("Меня назвали", name)
        self.name = name
        self.price = price
        
    def print_name(self):
        return self.name
        
    def print_price(self):
        return self.price

    def print_name_price(self):
        return f"Продукт: {self.name}, {self.price}"

