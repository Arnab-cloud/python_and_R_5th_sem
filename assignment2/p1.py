

def check_color(Colors, new_color: str) -> None:
    for tuple_color in Colors:
        if new_color.lower() in tuple(color.lower() for color in tuple_color):
            print(f"{new_color} is in the tuple")
            return
    print(f"{new_color} is not in th tuple")

print("Enter 9 Colors")
Colors = tuple( tuple([input() for _ in range (3)]) for _ in range(3) )

while True:
    new_color = input("Enter a color:")
    if new_color == "":
        print("Exiting")
        break
    check_color(Colors, new_color)


