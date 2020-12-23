### Day 21: Allergen Assessment ###

import re

all_ingredients = []
suspect_ingredients = {}
with open('input.txt', 'r') as input:
    for i, line in enumerate(input):
        line = line.rstrip()
        ingr_list = re.match(r'^(.*)\s\(contains (.*)\)$', line)
        ingredients, allergens = ingr_list.group(1), ingr_list.group(2)
        ingredients = ingredients.split(' ')
        allergens = allergens.split(', ')

        for ingr in ingredients:
            all_ingredients.append(ingr)
            for al in allergens:
                if al in suspect_ingredients and ingr in suspect_ingredients[al]:
                    suspect_ingredients[al][ingr] += 1
                elif al in suspect_ingredients:
                    suspect_ingredients[al][ingr] = 1
                else:
                    suspect_ingredients[al] = {ingr: 1}
                
# print(suspect_ingredients)

max_suspect_list = []
for al, ingr_counts in suspect_ingredients.items():
    max_count = 0
    for ingr, count in ingr_counts.items():
        if count > max_count:
            max_count = count

    max_ingrs = []
    for ingr, count in ingr_counts.items():
        if count == max_count:
            max_ingrs.append(ingr)
        
    max_suspect_list.append((al, max_ingrs))

ingredients_have_allergen = {}
i = 0
while i < len(max_suspect_list):
    max_suspect_list = sorted(max_suspect_list, key=lambda x: len(x[1]))
    for al, ingrs in max_suspect_list:
        if len(ingrs) == 1:
            ingredients_have_allergen[ingrs[0]] = al
            i = len(ingredients_have_allergen)
            break
    for al, ingrs in max_suspect_list:
        for _ingr, _al in ingredients_have_allergen.items():
            try:
                ingrs.remove(_ingr)
            except ValueError:
                pass
    

# print(ingredients_have_allergen)
    
safe_ingr_count = 0
for ingr in all_ingredients:
    if ingr not in ingredients_have_allergen:
        safe_ingr_count += 1

print(safe_ingr_count)
# part 1 solution: 2280

ia_list = []
for i, a in ingredients_have_allergen.items():
    ia_list.append((i, a))

ia_list = sorted(ia_list, key=lambda x: x[1])

print(','.join([i[0] for i in ia_list]))
# part 2 solution: vfvvnm,bvgm,rdksxt,xknb,hxntcz,bktzrz,srzqtccv,gbtmdb