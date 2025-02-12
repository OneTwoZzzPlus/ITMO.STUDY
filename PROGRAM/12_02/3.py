from Input import Input


class Coffee:
    def __init__(self, ingredient=''):
        self.ingredient = ingredient

    def show_my_drink(self):
        if self.ingredient == '':
            print('Черный кофе')
        else:
            print(f'Кофе и {self.ingredient}')


def main():
    ing = Input('Добавка').str()
    coffee = Coffee(ing)
    coffee.show_my_drink()


if __name__ == "__main__":
    main()
