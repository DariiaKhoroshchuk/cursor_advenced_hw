# 1 Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
class Animals:
    """
    Parent class, should have eat, sleep
    """

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'The animal {self.name} is eating...')

    def sleep(self):
        print(f'The animal {self.name} is sleeping...')


class Bear(Animals):
    def fishing(self):
        print(f'{self.name} by the river. It starts to fishing...')


class Wolf(Animals):
    def wolf_sound(self):
        print(f'{self.name} says: Wooooo...')


class Rabbit(Animals):
    def hide(self):
        print(f'{self.name} noticed the predator. It tries to hide from him...')


class Deer(Animals):
    def attack(self):
        print(f'{self.name} noticed the enemy. He began to attack...')


class Nightingale(Animals):
    def sing(self):
        print(f'It is morning. {self.name} began to singing...')


bear1 = Bear('Brown bear')
bear1.fishing()
animal1 = isinstance(bear1, Animals)
print(f'{bear1.name} is instance of Animal class: {animal1}')

wolf1 = Wolf('Gray wolf')
wolf1.wolf_sound()
animal2 = isinstance(wolf1, Animals)
print(f'{wolf1.name} is instance of Animal class: {animal2}')

rabbit1 = Rabbit('European hare')
rabbit1.hide()
animal3 = isinstance(rabbit1, Animals)
print(f'{rabbit1.name} is instance of Animal class: {animal3}')

deer1 = Deer('True deer')
deer1.attack()
animal4 = isinstance(deer1, Animals)
print(f'{deer1.name} is instance of Animal class: {animal4}')

nightingale1 = Nightingale('Luscinia')
nightingale1.sing()
animal5 = isinstance(nightingale1, Animals)
print(f'{nightingale1.name} is instance of Animal class: {animal5}')


# output:
# Brown bear by the river. It starts to fishing...
# Brown bear is instance of Animal class: True
# Gray wolf says: Wooooo...
# Gray wolf is instance of Animal class: True
# European hare noticed the predator. It tries to hide from him...
# European hare is instance of Animal class: True
# True deer noticed the enemy. He began to attack...
# True deer is instance of Animal class: True
# It is morning. Luscinia began to singing...
# Luscinia is instance of Animal class: True


# 1.a.Create a new class Human and use multiple inheritance to create Centaur class, create an instance of Centaur class
# and call the common method of these classes and unique.

class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'The human {self.name} is eating...')

    def sleep(self):
        print(f'The human {self.name} is sleeping...')

    def study(self):
        print(f'The human {self.name} is studying...')

    def work(self):
        print(f'The human {self.name} is working...')


class Centaur(Human, Animals):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """

    def fight(self):
        print(f'{self.name} is fighting with enemy...')


centaur1 = Centaur('Centaur')
centaur1.eat()
centaur1.sleep()
centaur1.work()
centaur1.study()
centaur1.fight()


# output:
# The human Centaur is eating...
# The human Centaur is sleeping...
# The human Centaur is working...
# The human Centaur is studying...
# Centaur is fighting with enemy...

# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
# a.
class Person:
    """
    Make the class with composition.
    """

    def __init__(self):
        left_arm = Arm(f'It is a left arm and it has five fingers: thumb, index, middle, ring and pinky.')
        right_arm = Arm(f'It is a right arm and it has five fingers: thumb, index, middle, ring and pinky.')
        self.arms = [left_arm, right_arm]


class Arm:
    """
    Make the class with composition.
    """

    def __init__(self, fingers):
        self.fingers = fingers


person = Person()
for arm in person.arms:
    print(arm.fingers)

# output:
# It is a left arm and it has five fingers: thumb, index, middle, ring and pinky.
# It is a right arm and it has five fingers: thumb, index, middle, ring and pinky.


# b.
class CellPhone:
    """
    Make the class with aggregation
    """
    def __init__(self, screen):
        self.screen = screen


class Screen:
    """
    Make the class with aggregation
    """
    def __init__(self, screen_type):
        self.screen_type = screen_type


samsung = Screen('Samsung')
our_cell_phone = CellPhone(samsung)
print(our_cell_phone.screen.screen_type)

# output:
# Samsung


# 3.
class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above
    """
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'Profile({self.name}, {self.last_name}, {self.phone_number}, {self.address}, {self.email}, ' \
               f'{self.birthday}), {self.age}, {self.sex})'


Oscar = Profile('Oscar', 'Black', '+123456789', 'Gorodska, 17', 'oscar@gmail.com', '14.09.99', '21', 'male')
print(Oscar)

# output:
# Profile(Oscar, Black, +123456789, Gorodska, 17, oscar@gmail.com, 14.09.99), 21, male)

# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.
from abc import abstractmethod, ABC


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def screen(self):
        print(f'{__class__.__name__} has a IPS 15,6-inch screen.')

    def keyboard(self):
        print(f'{__class__.__name__} has Ukrainian and English keyboard layouts.')

    def touchpad(self):
        print(f'{__class__.__name__} has touchpad.')

    def webcam(self):
        print(f'{__class__.__name__} has HP webcam with two built-in digital microphones.')

    def ports(self):
        print(f'{__class__.__name__} has 1 x USB Type C 10 Gbps, 2 x USB Type A 5 Gbps, combined audio jack'
              f' for headphones and microphones, SD card reader.')

    def dynamics(self):
        print(f'{__class__.__name__} has Audio Boost Bang & Olufsen dynamics.')


laptop = HPLaptop()
laptop.screen()
laptop.keyboard()
laptop.touchpad()
laptop.webcam()
laptop.ports()
laptop.dynamics()

# output:
# HPLaptop has a IPS 15,6-inch screen.
# HPLaptop has Ukrainian and English keyboard layouts.
# HPLaptop has touchpad.
# HPLaptop has HP webcam with two built-in digital microphones.
# HPLaptop has 1 x USB Type C 10 Gbps, 2 x USB Type A 5 Gbps, combined audio jack for headphones and microphones,
# SD card reader.
# HPLaptop has Audio Boost Bang & Olufsen dynamics.
