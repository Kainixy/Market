import pytest
import sys
import os

# обавляем текущую папку в пути импорта
sys.path.insert(0, os.getcwd())

# Теперь импорт должен работать
from Market import Balance, User, Thing, Basket

@pytest.fixture
def create_test_balance():
    # справлено: Balance принимает user_id, а не баланс
    test_balance = Balance(user_id=1)
    test_balance.balance = 100  # устанавливаем начальный баланс
    print(f'test balance created, info:{str(test_balance)}')
    return test_balance

def test_class_balance(create_test_balance):
    assert create_test_balance.add_money(100) == 0
    assert create_test_balance.take_money(100) == 0

@pytest.fixture
def create_test_user():
    test_user = User(
        id=1,
        name="Steve",
        age=21)
    print(test_user)
    return test_user

def test_class_user(create_test_user):
    assert create_test_user.id == 1

@pytest.fixture
def create_test_thing():
    test_thing = Thing(1, 'test_thing', 'very nice thing to test', 100, 300, 1)
    with open('test_thing.txt', 'w') as f:
        f.write('Yo, this is test file!')
    test_thing.documentation = f.name
    yield test_thing
    os.remove('test_thing.txt')

@pytest.fixture
def create_test_basket(create_test_user):
    test_basket = Basket(create_test_user.id)
    print(f'test basket created, info:{str(test_basket)}')
    return test_basket

def test_class_basket(create_test_basket, create_test_thing):
    assert create_test_basket.add_to_basket(create_test_thing) == 0
