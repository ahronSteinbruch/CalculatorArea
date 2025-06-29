# 📊 Shape Factory

A Python console application that allows users to create geometric shapes (Circle, Square, Rectangle, Triangle, Hexagon), view their properties, compare them, and perform operations like summing areas.



## 📦 Features

* ✅ Create multiple shapes interactively
* 📐 Calculate area and perimeter
* 🔍 Compare two shapes by area and perimeter
* ➕ Add the areas of two shapes
* 🧐 Object-oriented design using inheritance and polymorphism
* 💡 Supports extension with new shapes

---

## 🚀 Getting Started

### Requirements

* Python 3.6+
* No external libraries required

### Folder Structure

```
.
├── main.py
├── Shape.py
├── Circle.py
├── Square.py
├── Rectangle.py
├── Triangle.py
├── Hexagon.py
└── README.md
```

---

## ▶️ How to Run

1. Clone this repo or copy the files
2. Run the program:

```bash
python main.py
```

3. Follow the on-screen menu to create and manage shapes

---

## 📚 Example Usage

```
Welcome to the Shape Factory
1. Add new shape
2. Show all shapes
3. Compare two shapes
4. Sum areas of two shapes
5. Exit
```

Create shapes like Circle, Square, Rectangle, etc. and compare them:

> Shape 0: Circle – Area: 28.27, Perimeter: 18.85
> Shape 1: Square – Area: 25.00, Perimeter: 20.00
> "Circle is larger."

---

## 🧱 Class Design

### `Shape` (abstract base class)

* `get_area()`
* `get_perimeter()`
* Operator overloading: `__eq__`, `__gt__`, `__lt__`, `__add__`

Each specific shape inherits from `Shape` and implements its own area and perimeter logic.

---

## 🧹 Adding Your Own Shape

1. Create a new file (e.g., `Pentagon.py`)
2. Inherit from `Shape` and implement `get_area` and `get_perimeter`
3. Add it to the `shapeFactory()` menu in `main.py`

---

## ✍️ Author

Created by **אהרן שטיינברוך**
Inspired by object-oriented design in Python.

---

## 📜 License

This project is open-source and free to use for learning or extending.

