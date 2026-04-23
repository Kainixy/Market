class Thing:
    def __init__(self
                 , id: int
                 , name: str = 'Banana'
                 , description: str = 'Very nice banana!'
                 , cost: float = 10
                 , mass: int = 1
                 , status: int = 1
                 , documentation: str = 'banana_documentation.txt'):
        self.__id = id
        self._cost = cost
        self._mass = mass
        self._status = status
        self.name = name
        self.description = description
        self.documentation = documentation

    @property
    def id(self):
        return self.__id

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        if cost < 0:
            raise ValueError(f'Cost cannot be negative, got {cost}')
        self._cost = cost

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        if mass < 0:
            raise ValueError(f'Mass cannot be negative, got {mass}')
        self._mass = mass

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status != 0 and status != 1:
                raise ValueError(f'Status can be 0 or 1, got {status}')
        self._status = status

    def get_thing_status(self):
        if self.status == 1:
            return Message.send_ok(f'Status of thing {self.name} is active!')
        elif self.status == 0:
            return Message.send_ok(f'Status of thing {self.name} is not active!')

    def get_text_from_documentation(self):
        with open(self.documentation, 'r') as file:
            file_text = file.read()
            Message.send_ok(f'File has been read!')
        return file_text

    def add_text_to_documentation(self, text:str):
        with open(self.documentation, 'w+') as file:
            file.write(text)
            file.seek(0)
            file_text = file.read()
        Message.send_ok(f'File has been written!')
        return file_text


class Basket:
    def __init__(self, user_id:int):
        self.__user_id = user_id
        self.items = list()
        Message.send_ok(f'Basket for user with id {self.__user_id} created!')

    def __str__(self):
        return f'Basket for user with id {self.__user_id} has {len(self.items)} items!'

    def add_to_basket(self, thing:Thing):
        self.items.append(thing)
        return Message.send_ok(f'Thing with id {thing.id} added to basket of user with id {self.__user_id}!')

    def del_from_basket(self, thing:Thing):
        self.items = [item for item in self.items if item != thing]
        return Message.send_ok(f'Thing with id {thing.id} deleted from basket of user with id {self.__user_id} created!')

class User:
    def __init__(self, id:int, name:str, age:int):
        self.__id = id
        self.name = name
        self.age = age
        self.basket = Basket(self.__id)
        self.balance = Balance(self.__id)
        Message.send_ok(f'User with id {self.__id} created!')

    def __str__(self):
        return f'id:{self.__id} name:{self.name} age:{self.age} balance:{self.balance.balance}'

    def get_user_id(self):
        print( f'User with id {self.__id} found!')
        return self.__id

class Balance:
    def __init__(self, user_id:int):
        self.user_id = user_id
        self.balance = 0
        Message.send_ok(f'Balance for user with id {self.user_id} created!')

    def __str__(self):
        return f'User with id {self.user_id} balance:{self.balance}'

    def add_money(self, money:int):
        self.balance += money
        return Message.send_ok(f'Balance updated on +{money}! Your balance now is {self.balance}!')

    def take_money(self, money:int):
        if money <= self.balance:
            self.balance -= money
            return Message.send_ok(f'Balance updated on -{money}! Your balance now is {self.balance}!')
        else:
            return Message.send_error(f'Error! Your balance is less than {money}!')

class Message:
    @staticmethod
    def send_error(text):
        print(text)
        return 1

    @staticmethod
    def send_ok(text):
        print(text)
        return 0
