print(" ")

while True:
    num = input("Input a number: ")

    try:
        num = float(num)
        break
    except ValueError:
        print("ValueError: Must be a number")
        print(" ")
    finally:
        print(" ")

print(" ")


x=1
y=x
x+=1
print(F"X: {id(x)}, Y: {id(y)}")