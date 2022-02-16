#over60.py

score = [90,25,67,45,80]

for number in range(len(score)):
    if score[number] < 60:
        continue
    print("index of %dth student is a good student!" %(number+1))



