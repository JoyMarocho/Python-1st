# # ##### LOCAL SCOPE ######

# def greeting(name):
#     print('Hello', name)
    
# # MAin Program
# input_name = input('Enter your name:\n')

# greeting(input_name)


# ##### GLOBAL SCOPE ######

# def greeting():
#     print('Hello', name)
    
# # MAin Program
# name = input('Enter your Name:\n')
# # name2 = input('Enter your 2nd Name:\n')
# name = name2
# greeting()

###### LOCAL SCOPE ######
####### Local scope allows us to reuse the greeting () function with different values ######
def greeting(name):
    print('Hello', name)
    
# MAin Program
name1 = input('Enter your name:\n')
greeting(name1)
name2 = input('Enter another name:\n')
greeting(name2)