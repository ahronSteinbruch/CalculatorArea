from Circle import Circle
from Hexagon import Hexagon
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle

def menu():
    print("\nWelcome to the Shape Factory")
    print("1. Add new shape")
    print("2. Show all shapes")
    print("3. Compare two shapes")
    print("4. Sum areas of two shapes")
    print("5. Exit")

def shapeMenu():
    print("Which shape would you like to create?")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    print("5. Hexagon")

def shapeFactory(choice):
    if choice == 1:
        radius = float(input("Enter radius: "))
        return Circle(radius)
    elif choice == 2:
        side = float(input("Enter side: "))
        return Square(side)
    elif choice == 3:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        return Rectangle(length, width)
    elif choice == 4:
        side1 = float(input("Enter side 1: "))
        side2 = float(input("Enter side 2: "))
        side3 = float(input("Enter side 3: "))
        return Triangle(side1, side2, side3)
    elif choice == 5:
        side = float(input("Enter side: "))
        return Hexagon(side)
    else:
        print("Invalid shape choice")
        return None

def main():
    shapes = []
    while True:
        menu()
        option = input("Enter your option: ")

        if option == "1":
            shapeMenu()
            try:
                choice = int(input("Your shape choice: "))
                shape = shapeFactory(choice)
                if shape:
                    shapes.append(shape)
                    print("Shape added.")
            except ValueError:
                print("Please enter a valid number.")

        elif option == "2":
            if not shapes:
                print("No shapes created yet.")
            else:
                for i, shape in enumerate(shapes):
                    print(f"{i}: {type(shape).__name__} - Area: {shape.get_area():.2f}, Perimeter: {shape.get_perimeter():.2f}")

        elif option == "3":
            if len(shapes) < 2:
                print("You need at least two shapes to compare.")
            else:
                a = int(input("Enter index of first shape: "))
                b = int(input("Enter index of second shape: "))
                if shapes[a] == shapes[b]:
                    print("Shapes are equal in area and perimeter.")
                elif shapes[a] > shapes[b]:
                    print("First shape is larger.")
                else:
                    print("Second shape is larger.")

        elif option == "4":
            if len(shapes) < 2:
                print("You need at least two shapes to add.")
            else:
                a = int(input("Enter index of first shape: "))
                b = int(input("Enter index of second shape: "))
                total_area = shapes[a] + shapes[b]
                print(f"Total area: {total_area:.2f}")

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()


