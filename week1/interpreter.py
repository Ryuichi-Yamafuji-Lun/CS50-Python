#interpreter exercise implementation
def main():
    equation = input("Expression: ")
    equation = equation.split()
    #see if format is correct
    if len(equation) != 3:
        print("Format: num expression num")
        return 0
    x = float(equation[0])
    y = equation[1]
    z = float(equation[2])
    answer = eq(x,y,z)
    print(answer)

#decides what y is 
def eq(x,y,z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z
    else:
        print("Input + - * /")
        exit 
        
main()