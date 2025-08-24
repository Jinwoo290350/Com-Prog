class Coin:
    def __init__(self, value=1):
        self.value = value

    def __str__(self):
        return f'{self.value} Baht Coin'

class BankNote:
    def __init__(self, value=20):
        self.value = value

    def __str__(self):
        return f'{self.value} Baht Banknote'

class Application:
    def __init__(self, amount: int):
        self.__amount = amount
        self.__denominations = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
        self.__change_bag = []
        self.__calculate()

    def __calculate(self):
        remaining = self.__amount
        for value in self.__denominations:
            count = remaining // value
            if count > 0:
                for _ in range(count):
                    if value >= 20:
                        self.__change_bag.append(BankNote(value))
                    else:
                        self.__change_bag.append(Coin(value))
                remaining -= count * value

    def __str__(self):
        counted = {}
        for item in self.__change_bag:
            counted[str(item)] = counted.get(str(item), 0) + 1
        result = ""
        for value in self.__denominations:
            if value >= 20:
                key = f"{value} Baht Banknote"
            else:
                key = f"{value} Baht Coin"
            if key in counted:
                result += f"You get {counted[key]} of {key}\n"
        return result.strip()

amount = int(input("Input amount : "))
app = Application(amount)
print(app)
