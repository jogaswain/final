from django import template
register = template.Library()

@register.filter(name='ffu')
def first_five_upper(value):
    result = value[:5].upper()
    return result

@register.filter(name='fnu')
def first_n_upper(value, args):
    m,n = [int(x) for x in args.split(',')]
    result = value[m:n].upper()
    return result

# register.filter('ffu',first_five_upper)
# register.filter('fnu',first_n_upper)