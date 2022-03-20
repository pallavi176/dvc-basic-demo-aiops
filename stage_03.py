with open('artifacts01.txt', 'r') as file:
    text = file.read()

print(text)

with open("artifacts02.txt", "w") as file:
    file.write(text+" Few lines added")

print("End of stage_03")