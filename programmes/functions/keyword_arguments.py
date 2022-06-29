#Keyword arguments(kwargs)
def hello(fname, lname, datestring): #practice function
    """A docstring describing the function"""
    msg = "Hello " + fname + ' ' + lname
    msg += ' You have entered ' + datestring
    print(msg)

#pass in literal kwargs (identify each by a parameter name)
hello(datestring='12/31/2021', fname='Simpson', lname='Alan')

#pass in kwargs from variables (identify each by a parameter name)
appt_date = '12/31/2019'
last_name = 'Janda'
first_name = 'Kyle'
hello(datestring=appt_date, lname=last_name, fname=first_name)
