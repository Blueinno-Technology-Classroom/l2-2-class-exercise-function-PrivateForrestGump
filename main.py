##################################################
'''
Q1: 
'''

# TODO: Write your code here
def greet(e):
   print(f'Hi, {e}!')

greet(e='Alice')
greet(e='Bob')
##################################################
'''
Q2:
'''

# TODO: Write your code here
def greet(e, f):
   print(f'Hi, {e} and {f}!')

greet(e='Bob', f='Alex')
##################################################
'''
Q3:
'''

# TODO: Write your code here
def find_rect_area(width, height):
    print(width*height , "cm^2")
find_rect_area(width=12.3, height=45.6)
##################################################
'''
Q4:
'''

# TODO: Write your code here
def bought(animal):
    print(f'Bought me a {animal} and the {animal} pleased me, I fed my {animal} under yonder tree.')

def cat():
    print("Cat goes fiddle-i-fee.")

def hen():
    print("Hen goes chimmy-chuck, chimmy-chuck,")
    cat()

def duck():
    print("Duck goes quack, quack,")
    hen()

def goose():
    print("Goose goes hissy, hissy,")
    duck()

def first_verse():
    bought('cat')
    cat()

def second_verse():
    bought('hen')
    hen()

def third_verse():
    bought('duck')
    duck()

def fourth_verse():
    bought('goose')
    goose()

first_verse()
second_verse()
third_verse()
fourth_verse()
##################################################
