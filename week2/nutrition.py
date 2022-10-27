#implementation of nutrition exercise
def main():
    fruit = input("Item: ")
    print(nutrition(fruit.lower()))

#list of fruit with calories
def nutrition(fruit):
    if fruit == "apple":
        return 130
    elif fruit == "plums":
        return 70
    elif fruit == "lemon":
        return 15
    elif fruit == "lime":
        return 20
    elif fruit == "banana":
        return 110
    elif fruit == "grapes" or fruit == "kiwifruit":
        print(fruit)
        return 90
    elif fruit == "orange" or fruit == "watermelon":
        return 80
    elif fruit == "pear" or fruit == "sweet cherries":
        return 100
    elif fruit == "grapefruit" or fruit == "nectarine" or fruit == "peach":
        return 60
    elif fruit == "avocado" or fruit == "cantaloupe" or fruit == "honeydew melon" or fruit == "pineapple" or fruit == "strawberries" or fruit == "tangerine":
        return 50
    else:
        exit()
    
main()