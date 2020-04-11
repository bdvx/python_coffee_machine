

interrupted = False


class CoffeeCommands:

    def __init__(self, money, water, milk, coffee, cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cups = cups

    def report(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print('$' + str(self.money), 'of money')

    def fill(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups

    def buy_commands(self, buy_command):
        if buy_command == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
                return
            elif self.coffee < 16:
                print('Sorry, not enough coffee!')
                return
            self.water = max(0, self.water - 250)
            self.coffee = max(0, self.coffee - 16)
            self.money = max(0, self.money + 4)
        elif buy_command == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
                return
            elif self.coffee < 20:
                print('Sorry, not enough coffee!')
                return
            elif self.milk < 75:
                print('Sorry, not enough milk!')
                return
            self.water = max(0, self.water - 350)
            self.milk = max(0, self.milk - 75)
            self.coffee = max(0, self.coffee - 20)
            self.money = max(0, self.money + 7)
        elif buy_command == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
                return
            elif self.coffee < 12:
                print('Sorry, not enough coffee!')
                return
            elif self.milk < 100:
                print('Sorry, not enough milk!')
                return
            self.water = max(0, self.water - 200)
            self.milk = max(0, self.milk - 100)
            self.coffee = max(0, self.coffee - 12)
            self.money = max(0, self.money + 6)
        elif buy_command == 'back':
            return
        self.cups = max(0, self.cups - 1)


coffee = CoffeeCommands(550, 400, 540, 120, 9)

while not interrupted:
    command = input('Write action (buy, fill, take, remaining, exit):\n')
    print()
    if command == 'buy':
        buy_command = input(
            'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        coffee.buy_commands(buy_command)
    elif command == 'fill':
        water_add = int(input('Write how many ml of water do you want to add:\n'))
        milk_add = int(input('Write how many ml of milk do you want to add:\n'))
        coffee_add = int(input('Write how many grams of coffee beans do you want to add:\n'))
        cups_add = int(input('Write how many disposable cups of coffee do you want to add:\n'))
        coffee.fill(water_add, milk_add, coffee_add, cups_add)
    elif command == 'take':
        print('I gave you $' + str(coffee.money))
        coffee.money = 0
    elif command == 'remaining':
        coffee.report()
    elif command == 'exit':
        interrupted = True
    print()

