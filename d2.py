file = "data.txt"
#file = "sample.txt"
f = open(file)
lines = f.readlines()

data ={}
for line in lines:
    words = line.split()
    game = words[1][:-1]
    data[game] = {"red": 0, "green": 0, "blue": 0}
    for i in range(2, len(words), 2):
        count = int(words[i])
        colour = words[i+1]
        if colour[-1] in [",", ";"]:
            colour = words[i+1][:-1]
        data[game][colour] = max(data[game][colour], count)

sum = 0
for game in data:
    if data[game]["red"] <= 12 and data[game]["green"] <= 13 and data[game]["blue"] <= 14:
        sum += int(game)
#        print(game)
print(sum)

