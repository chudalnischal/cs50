user_input = input ("enter number with operator sperated by space: ")
x , y , z = user_input.split()
x = int(x)
z = int(z)
if y == "+":
    c = x + z
    print(float(c))
elif y == "-":
    c = x - z
    print(float(c))
elif y == "*":
    c = x * z
    print(float(c))
elif y == "/":
    c = x / z
    print(float(c))
