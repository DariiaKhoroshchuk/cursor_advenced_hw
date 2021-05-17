import random
import time
from abc import abstractmethod, ABC

# There is a Person whose characteristics are:
# 1. Name
# 2. Age
# 3. Availability of money
# 4. Having your own home


class Person(ABC):
    def __init__(self, name, age, money, own_home=None):
        if own_home is None:
            own_home = []
        self.name = name
        self.age = age
        self.money = money
        self.own_home = own_home

    @abstractmethod
    def info(self, realtor):
        raise NotImplementedError

    @abstractmethod
    def earn_money(self):
        raise NotImplementedError

    def buy_house(self, house, realtor):
        pass


# Human can:
# 1. Provide information about yourself
# 2. Make money
# 3. Buy a house

class Human(Person):
    def info(self, realtor):
        print(f'My name is {self.name}, and i am {self.age} years old.\n'
              f'I have {self.money}$.')
        if len(self.own_home) >= 1:
            print(f'I have such real estate: {[home.address for home in self.own_home]}\n')
            for my_home in self.own_home:
                for home in realtor.all_houses:
                    if my_home == home:
                        realtor.all_houses.remove(home)
        else:
            print('I do not have any real estate.\n')

    def earn_money(self):
        print(f'Now {self.name} has {self.money}$.')
        print(f'{self.name} starts to earn money...')
        self.money += random.randrange(100, 1000, 50)
        time.sleep(1.5)
        print(f'After work {self.name} has {self.money}$.\n')

    def buy_house(self, house, realtor):
        if realtor.steal_money is True:
            print('Realtor stole my money:(')
            self.money = 0
            return
        if house.cost <= self.money:
            print(f'{self.name} buy house at {house.address} of {house.area}sq.m costs {house.cost}.')
            self.money -= house.cost
            print(f'After the purchase, {self.name} had {self.money}$ left.\n')
            self.own_home.append(house)
            realtor.sold_house(house)
        else:
            while self.money <= house.cost:
                print(f'I do not have enough money to buy this house {house.address}.')
                print(f'I should earn {house.cost-self.money}$ to buy it.')
                print(f'Can you please wait and not sell this house {house.address} while i earn money.\n')
                self.earn_money()
            print(f'Hooray! Now I have enough money to buy house at {house.address}\n')
            self.buy_house(house, realtor)


# There is also a House, the properties of which include:
# 1. Area
# 2. Cost
class House(ABC):
    def __init__(self, address, area, cost):
        self.address = address
        self.area = area
        self.cost = cost

    @abstractmethod
    def make_discount(self):
        raise NotImplementedError


# For Home you can:
# 1. Apply a purchase discount
class Home(House):
    def make_discount(self):
        self.cost -= self.cost * (random.randint(1, 30)/100)
        print(f'If you want to buy a house {self.address}, you will have a discount and new price is: {self.cost}\n')


# e.g.: There is also a Small Typical House with a required area of 40m2.
class SmallTypicalHouse(Home):
    def __init__(self, address,  cost, area=40):
        super().__init__(address, area, cost)


# *Realtor:
# 1. Name
# 2. Houses
# 3. Discount that he/she can give you.
# *There is only one realtor who handles small houses you wanna buy. (Singleton)
class RealtorSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Realtor is only one in your city and can:
# 1. Provide information about all the Houses
# 2. Give a discount
# 3. Steal your money with 10% chance
class Realtor(metaclass=RealtorSingleton):
    def __init__(self, name, discount, all_houses=None):
        if all_houses is None:
            all_houses = []
        self.name = name
        # self.clients = clients
        self.discount = discount
        self.all_houses = all_houses

    def house_info(self):
        # for house in self.all_houses:
        #     if house in list(self.clients.own_home):
        #         self.all_houses.remove(house)
        print(f'Realtor {self.name} can offer such houses:')
        for house in self.all_houses:
            print(f'* {house.__class__.__name__} at {house.address} with {house.area}sq.m '
                  f'and the cost of this house is {house.cost}')

    def give_discount(self, house):
        if self.discount:
            house.make_discount()

    def steal_money(self):
        if random.randint(1, 100) <= 10:
            print(f'You are unlucky. Realtor {self.name} stole your money.\n')
            return True
        else:
            print(f'Some realtors steal money from their clients, but you are lucky, '
                  f'the realtor {self.name} is good.\n')
            return False

    def sold_house(self, house):
        self.all_houses.remove(house)


if __name__ == '__main__':
    house1 = Home('Shevchenka, 5', 150, 35000)
    house2 = Home('Karmelyuka, 14', 100, 30000)
    house3 = SmallTypicalHouse('Gagarina, 6', 20000)
    house4 = Home('Zelena, 34', 80, 27000)

    anna = Human('Anna', 45, 40000, [house1])
    john = Human('John', 23, 18000)

    realtor_sam = Realtor('Sam', True, all_houses=[house1, house2, house3, house4])

    anna.info(realtor_sam)
    realtor_sam.house_info()
    realtor_sam.give_discount(house2)
    realtor_sam.steal_money()
    anna.buy_house(house2, realtor_sam)

    john.info(realtor_sam)
    realtor_sam.house_info()
    realtor_sam.give_discount(house3)
    realtor_sam.steal_money()
    john.buy_house(house3, realtor_sam)

# realtor_sam.house_info()
# realtor_sam.give_discount(house4)
# realtor_sam.steal_money()
# anna.buy_house(house4, realtor_sam)

# output:
# My name is Anna, and i am 45 years old.
# I have 40000$.
# I have such real estate: ['Shevchenka, 5']
#
# Realtor Sam can offer such houses:
# * Home at Karmelyuka, 14 with 100sq.m and the cost of this house is 30000
# * SmallTypicalHouse at Gagarina, 6 with 40sq.m and the cost of this house is 20000
# * Home at Zelena, 34 with 80sq.m and the cost of this house is 27000
# If you want to buy a house Karmelyuka, 14, you will have a discount and new price is: 27000.0
#
# Some realtors steal money from their clients, but you are lucky, the realtor Sam is good.
#
# Anna buy house at Karmelyuka, 14 of 100sq.m costs 27000.0.
# After the purchase, Anna had 13000.0$ left.
#
# My name is John, and i am 23 years old.
# I have 18000$.
# I do not have any real estate.
#
# Realtor Sam can offer such houses:
# * SmallTypicalHouse at Gagarina, 6 with 40sq.m and the cost of this house is 20000
# * Home at Zelena, 34 with 80sq.m and the cost of this house is 27000
# If you want to buy a house Gagarina, 6, you will have a discount and new price is: 18600.0
#
# Some realtors steal money from their clients, but you are lucky, the realtor Sam is good.
#
# I do not have enough money to buy this house Gagarina, 6.
# I should earn 600.0$ to buy it.
# Can you please wait and not sell this house Gagarina, 6 while i earn money.
#
# Now John has 18000$.
# John starts to earn money...
# After work John has 18250$.
#
# I do not have enough money to buy this house Gagarina, 6.
# I should earn 350.0$ to buy it.
# Can you please wait and not sell this house Gagarina, 6 while i earn money.
#
# Now John has 18250$.
# John starts to earn money...
# After work John has 19150$.
#
# Hooray! Now I have enough money to buy house at Gagarina, 6
#
# John buy house at Gagarina, 6 of 40sq.m costs 18600.0.
# After the purchase, John had 550.0$ left.
