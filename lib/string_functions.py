def return_string():
    return ''

def interpolate_string(s):
    return f'Hello, {s}!'
    

def interpolate_welcome(name):
    return f'Welcome, {name}!'

assert interpolate_welcome('Guido') == 'Welcome, Guido!'