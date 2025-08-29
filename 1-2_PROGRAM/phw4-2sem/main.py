from abc import ABC, abstractmethod
from enum import Enum


class CallType(Enum):
    # CITY = 1
    MOBILE = 2
    ...


# Абстрактный тариф
class Tariff(ABC):
    @abstractmethod
    # НАЗНАЧАЕМ расчёт по тарифу наследникам Tariff
    def calculate_cost(self, call_type: CallType, minutes: int) -> float:
        # Расчёт по-умолчанию
        if call_type is CallType.CITY:
            return minutes * 5
        elif call_type is CallType.MOBILE:
            return minutes * 1
        return 0

# Тариф повременный, работает "по-умолчанию"
class TimeBasedTariff(Tariff):
    def calculate_cost(self, call_type: CallType, minutes: int):
        return super().calculate_cost(call_type, minutes)

# Конкретные тарифы
class After10Tariff(Tariff):
    def calculate_cost(self, call_type: str, minutes: int) -> float:
        if call_type is not CallType.CITY or minutes <= 10:
            return super().calculate_cost(call_type, minutes)
        free_minutes = (minutes - 10) // 2
        return super().calculate_cost(call_type, minutes - free_minutes)

class PayLess5Tariff(Tariff):
    def calculate_cost(self, call_type: str, minutes: int) -> float:
        if minutes <= 5:
            return super().calculate_cost(call_type, minutes) / 2
        return super().calculate_cost(call_type, 5) / 2 + super().calculate_cost(call_type, minutes - 5) * 2
            

# Пользователь
class Customer:
    _name: str
    _balance: float
    _tariff: Tariff
    
    def __init__(self, name: str, tariff: Tariff=TimeBasedTariff(), balance: float = 0):
        self._name = name
        self._balance = balance
        self._tariff = tariff

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def balance(self) -> float:
        return self._balance
    
    def record_payment(self, money: float):
        self._balance += money

    def record_call(self, call_type: CallType, minutes: int):
        # УБИРАЕМ расчёт по тарифу, переназначаем его на тарифы
        self._balance -= self._tariff.calculate_cost(call_type, minutes) 
        
        
if __name__ == "__main__":
    # Я просто иногда звоню
    user1 = Customer("Иван")
    # Семён не любит долгих разговоров
    user2 = Customer("Семён", PayLess5Tariff())
    # Артём положил деньги при оформлении симкарты
    user3 = Customer("Артём", After10Tariff(), 1000)
    print("Баланс Артёма до звонка", user3.balance)
    user3.record_call(CallType.CITY, 15)
    print("Баланс Артёма после звонка", user3.balance)