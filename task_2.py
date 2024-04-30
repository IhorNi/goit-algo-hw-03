"""
Посібник, який було взято за основу
https://understanding-recursion.readthedocs.io/en/latest/13%20Koch%20Curves.html
"""

import turtle


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)


def koch_snowflake(t, order, size):
    t.begin_fill()
    for _ in range(3):
        koch(t, order, size)
        t.right(120)
    t.end_fill()


def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії: "))
            if level < 0:
                print("Рівень рекурсії має бути >= 0")
                continue
            if level > 5:
                print("Для цілей прикладу максимальний рівень рекурсії має бути <= 5")
                continue
            break
        except ValueError:
            print("Рівень рекурсії має бути >= 0")

    window = turtle.Screen()
    the_turtle = turtle.Turtle()
    the_turtle.speed(0)
    the_turtle.penup()

    # розмір за стартові координати для прикладу по центру
    size = 500
    the_turtle.goto(-250, 100)
    the_turtle.pendown()

    koch_snowflake(the_turtle, level, size)

    window.mainloop()


if __name__ == "__main__":
    main()
