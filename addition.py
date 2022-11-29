### creating our addition functiom

# def addition( a, b):
#     return a + b

# ### MAIN PROGRAM
# num1 = float(input('Enter your 1st number:\n'))
# num2 = float(input('Enter your 2nd number:\n'))

# ### CALLING OUR FUNCTION
# result = addition(num1, num2)
# print('The result is', result)

####### ORGANIZING our main code ###############

def addition( a, b):
    return a + b

### MAIN PROGRAM

def main():
    num1 = float(input('Enter your 1st number:\n'))
    num2 = float(input('Enter your 2nd number:\n'))

### CALLING OUR FUNCTION
    result = addition(num1, num2)
    print('The result is', result)

main()
#the main function still needs to be called after the functions are declared.