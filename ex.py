try:
    age =  int(input("Input your age: "))
    print(age * 2)
except ValueError:
    print("Please enter a valid number.")