file = "data.txt"
#file = "sample.txt"
f = open(file)
lines = f.readlines()

data ={}
for line in lines:
    words = line.split()
    game = words[1][:-1]                                        # This is the game-id without the ending semicolon

    data[game] = {"red": 0, "green": 0, "blue": 0}
    for i in range(2, len(words), 2):
        count = int(words[i])
        colour = words[i+1]
        if colour[-1] in [",", ";"]:
            colour = colour[:-1]                                # remove the comma or semicolon
        data[game][colour] = max(data[game][colour], count)

sum = 0
for game in data:
    power = data[game]["red"] * data[game]["green"] * data[game]["blue"]
    sum += power

print(sum)

