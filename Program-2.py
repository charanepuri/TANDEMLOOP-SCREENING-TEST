number = int(input("Enter a number: "))
for i in range(number):
    print( 2 * i + 1 , end = ", " if i < number - 1 else "" )