number = int(input("Enter a number: "))
if number % 2 == 0:
    number = number - 1
series = [2*i + 1 for i in range(number)]
print(", ".join(map(str, series)))
