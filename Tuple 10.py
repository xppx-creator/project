class Cat:
    name = None
    age = None
    isHappy = None
    np = 4

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name,"", "age:",self.age, self.isHappy)


cat1 = Cat()
cat1.set_data("Барсик", 3, False)

cat2 = Cat()
cat2.set_data("Жопен", 2, True)

cat1.get_data()
cat2.get_data()