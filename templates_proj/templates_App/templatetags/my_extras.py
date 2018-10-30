from django import template

register = template.Library()

@register.filter(name='make')
def make(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
#Then we register it outside the function:

#register.filter('make', make)
#the 'make ' is what we are gonna call in the template tag and make is the name of the above function.
