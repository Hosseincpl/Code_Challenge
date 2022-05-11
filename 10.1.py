melons = input().split()
melons = list(map(int, melons))

mood = 0
for item in melons:
    if item >= 80:
        mood += 1

if mood < 1:
    print("Mamma mia!!!")
elif mood < 3:
    print("Mamma mia!!")
else :
    print("Mamma mia!")
