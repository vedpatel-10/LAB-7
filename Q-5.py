grocery_price = {"biscuit": 20,"flour":70,"chocolate":10}
grocery_quantity = {"biscuit":3,"flour":2,"chocolate":5}

lst = []
for i,(k1,v1) in enumerate(grocery_price.items()):
    for j,(k2,v2) in enumerate(grocery_quantity.items()):
        if i == j:
            lst.append(v1*v2)

print(sum(lst))            


