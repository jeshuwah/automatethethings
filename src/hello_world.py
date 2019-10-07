# just a simple hello world

# introduction
print('Hi there!')
print('What is your name?')

# user inputs name
myName = input()

# app response
print('It''s great to meet you, ' + myName)

# determine & display length of name
print('The length of your name is: ' + str(len(myName)))

# request age of user
print('How old are you?')

# user inputs age
myAge = int(input())

# tease the user a bit
if myAge<30:
    print("You're a youngin'!")
else:
    print("Yep, you're getting old. It's okay though!")

