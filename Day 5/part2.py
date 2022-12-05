f = open("Day 5\input.txt", "r")

lines = f.readlines()

table = [
    ["F", "T", "C", "L", "R", "P", "G", "Q"],
    ["N", "Q", "H", "W", "R", "F", "S", "J"],
    ["F", "B", "H", "W", "P", "M", "Q"],
    ["V", "S", "T", "D", "F"],
    ["Q", "L", "D", "W", "V", "F", "Z"],
    ["Z", "C", "L", "S"],
    ["Z", "B", "M", "V", "D", "F"],
    ["T", "J", "B"],
    ["Q", "N", "B", "G", "L", "S", "P", "H"]
]

for line in lines:
    if "move" in line:
        row = line.split(" ")

        count = int(row[1])
        source = int(row[3]) - 1
        to = int(row[5]) - 1

        table[to] += table[source][-count:]
        del table[source][-count:]

        
finalWord = ""

for c in table:
    finalWord += c[-1]

print(finalWord)
