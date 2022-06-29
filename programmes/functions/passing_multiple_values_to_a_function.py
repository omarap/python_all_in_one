#passing multiple values to a function
def hello (fname, lname, datestring):
    """A docstring describing the function"""
    msg = 'Hello '+ fname + ' '+ lname
    msg += ' you mentioned '+ datestring
    print(msg)


hello('Alan', 'Simpson', '2022/06/28')

#Example2
def message(fname, lname, datestring = ''):
    msg = 'Hello ' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
    print(msg)

message('Allan', 'Simpson', '12/31/2021')
message('Sammy', 'Schmeedledorp')