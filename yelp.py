# datatypes= price, type of food, weather based liklihood
# hash price = $$$, type of food = pizza, weather = sunny
# three arrays, price, food, weather

class Yelp():
    def __init__(self,name):
        self.food = []
        self.price =[]
        self.weather= []
        self.name = name

    def add_data(self):
        what_to_add = input("do you want to a")
