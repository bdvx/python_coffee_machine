dishes = ['pasta', 'apple_pie', 'ratatouille', 'chocolate_cake', 'omelette']
dish_ingreds = {'pasta': "tomato, basil, garlic, salt, pasta, olive oil",
                'apple_pie': "apple, sugar, salt, cinnamon, flour, egg, butter",
                'ratatouille': "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt",
                'chocolate_cake': "chocolate, sugar, salt, flour, coffee, butter",
                'omelette': "egg, milk, bacon, tomato, salt, pepper"}
ingred = input()


for dish in dishes:
    if ingred in dish_ingreds[dish]:
        print('You can make', dish.replace('_', ' '))
