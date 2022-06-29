#passing information to a function
def hello(x): #practice function
    """a doctstring describing the function """
    print('Hello ' + x)

hello('patrick')
hello('Cabs')
hello('betty')
hello('christiana')
hello('clever')

def user(username): #practice function
    print("Hello  " + username)

user('Cabela')
user('Marvieux')

#passing data to a function via a variable
def person(username):
    """A docstring describing the variable """
    print("Hello " + username)

#put a string in a variable called this_person
this_person = "Allan"
person(this_person)

