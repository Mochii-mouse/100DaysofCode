row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

Column = int(position[1]) - 1
Row = int(position[0]) - 1

map[Column][Row] = "X"

print(f"{row1}\n{row2}\n{row3}")

