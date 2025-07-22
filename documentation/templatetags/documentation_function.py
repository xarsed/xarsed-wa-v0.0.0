from django import template

register = template.Library()

@register.filter
def replace_underscore_questionmark(value):
    
    if value[-1] == "_":
        title = value[:-1] + "?"
    else:
        title = value 

    final_title = title.replace("_", " ")
    
    return final_title