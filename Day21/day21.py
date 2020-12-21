def readFile():
    with open('input.txt') as file:
        foodStrs = file.read().splitlines()
        foods = []
        for line in foodStrs:
            tokens = line.strip().split(' (contains ')
            ingredients = set(tokens[0].split())
            allergens = set(tokens[1][:-1].split(", "))
            foods.append((ingredients, allergens))
        return foods 

def problem1(foods):
    foodCount = {}
    possible = {}
    for ingredients, allergens in foods:
        for ingredient in ingredients:
            if ingredient not in foodCount.keys():
                foodCount[ingredient] = 1
            else:
                foodCount[ingredient] += 1
        for allergen in allergens:
            if allergen not in possible:
                possible[allergen] = ingredients.copy()
            else:
                possible[allergen] &= ingredients

    allergic = set()
    for ingAllergens in possible.values():
        allergic.update(ingAllergens)

    return sum(foodCount[ing] for ing in (foodCount.keys() - allergic))

def problem2(foods):
    possible = {}
    for ingredients, allergens in foods:
        for allergen in allergens:
            if allergen not in possible:
                possible[allergen] = ingredients.copy()
            else:
                possible[allergen] &= ingredients

    found = set()
    allergenMap = []
    while len(allergenMap) < len(possible.keys()):
        for allergen, ingredients in possible.items():
            if len(ingredients - found) == 1:
                ing = min(ingredients - found)
                allergenMap.append((allergen, ing))
                found.add(ing)
                break
    
    return ",".join(x[1] for x in sorted(allergenMap))


def main():
    foods = readFile()
    print(f'Answer for Problem1: {problem1(foods)}')
    print(f'Answer for Problem2: {problem2(foods)}')
main()