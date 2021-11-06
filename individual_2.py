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


a1 = input_to_int("a1", True)
a2 = input_to_int("a2", True)
a3 = input_to_int("a3", True)
b1 = input_to_int("b1", True)
b2 = input_to_int("b2", True)

s1 = (a1 + b1) % 10
s2 = a2 + b2 + (a1 + b1) / 10
s3 = a3 + (a2 + b2) / 10

print(f"a1={a1}, a2={a2}, a3={a3}, b1={b1}, b2={b2}, ")
print(f"s1 = ({a1} + {b1}) % 10 = {s1}")
print(f"s2 = {a2} + {b2} + ({a1} + {b1}) / 10 = {s1}")
print(f"s3 = {a3} + ({a2} + {b2}) / 10= {s1}")
