from django import template

# How to make custom filter!

register = template.Library()

# @register.filter(name=cut)
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, ' ')

register.filter('cut', cut) # @register keyword is more efficient to use