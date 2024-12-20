items = [
    ('rifle', 'r', 3, 25),
    ('pistol', 'p', 2, 15),
    ('ammo', 'a', 2, 15),
    ('medkit', 'm', 2, 20),
    ('inhaler', 'i', 1, 5),
    ('knife', 'k', 1, 15),
    ('axe', 'x', 3, 20),
    ('talisman', 't', 1, 25),
    ('flask', 'f', 1, 15),
    ('antidot', 'd', 1, 10),
    ('supplies', 's', 2, 20),
    ('crossbow', 'c', 2, 20)
]

rukzak = [['' for _ in range(4)] for _ in range(2)]
ochki = 15  
yachenki = 8  

items.sort(key=lambda x: x[3] / x[2], reverse=True)

final_list = []
for item in items:
    name, abbr, size, points = item
    if yachenki >= size:
        final_list.extend([abbr] * size)  
        ochki += points
        yachenki -= size
    else:
        ochki -= points

inventry_order = final_list[:8]  
for i in range(2):
    for j in range(4):
        if i * 4 + j < len(inventry_order):
            rukzak[i][j] = inventry_order[i * 4 + j]

formatted_rukzak = []
for row in rukzak:
    formatted_row = ",".join([f"[{item}]" if item else "[]" for item in row])
    formatted_rukzak.append(formatted_row)

for row in formatted_rukzak:
    print(row)

print(f"Итоговые очки выживания: {ochki}")