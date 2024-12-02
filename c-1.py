class Customer:
    def __init__(self, first_name, family_name, age):
        self.__first_name = first_name
        self.__family_name = family_name
        self.__age = age

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def family_name(self):
        return self.__family_name

    @family_name.setter
    def family_name(self, family_name):
        self.__family_name = family_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.__age <= 3:
            return 0
        elif 3 < self.__age < 20:
            return 1000
        elif 20 <= self.__age < 65:
            return 1500
        elif 65 <= self.__age < 75:
            return 1200
        else:
            return 500

    def info_csv(self):
        return f"{self.first_name},{self.family_name},{self.age},{self.entry_fee()}"

    def info_tsv(self):
        return f"{self.first_name} {self.family_name} {self.age} {self.entry_fee()}"

    def info_vsv(self):
        return f"{self.first_name} {self.family_name}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=75)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)

print(ken.full_name())  # "Ken Tanaka" という値を出力
print(tom.full_name())  # "Tom Ford" という値を出力

print(ken.age)  # 15 という値を出力
print(tom.age)  # 57 という値を出力
print(ieyasu.age)  # 75 という値を出力

print(ken.entry_fee())  # 1000 という値を出力
print(tom.entry_fee())  # 1500 という値を出力
print(ieyasu.entry_fee())  # 1200 という値を出力
print(michelle.entry_fee())  # 0 という値を出力

print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を出力
print(tom.info_csv())  # "Tom Ford,57,1500" という値を出力
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,75,1200" という値を出力
print(michelle.info_csv())

print(ken.info_tsv())
print(tom.info_tsv())
print(ieyasu.info_tsv())
print(michelle.info_tsv())

print(ken.info_vsv())
print(tom.info_vsv())
print(ieyasu.info_vsv())
print(michelle.info_vsv())
