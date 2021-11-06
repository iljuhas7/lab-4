def input_to_int(message: str = "", msgIsTip: bool = False) -> int:
    if msgIsTip:
        msg_tip = " (integer)"
    else:
        msg_tip = ""

    while True:
        try:
            return int(input(message + msg_tip + ": "))

        except ValueError:
            print("[Error]: It's not an integer!")


print("Area of a triangle given three sides.")
a = input_to_int("a", True)
b = input_to_int("b", True)
c = input_to_int("c", True)
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f"a = {a}, b = {b}, c = {c}")
print(f"p = ({a} + {b} + {c}) / 2 = {p:.1f}")
print(f"s = ({p:.1f} * ({p:.1f} - {a}) * ({p:.1f} - {b}) * ({p:.1f} - {c})) ** 0.5 = {s:.1f}")
print(f"The area of the triangle is equal to {s:.1f}")