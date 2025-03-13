from django import template

register = template.Library()

@register.filter
def to_list(value):
    return MyStaticMethods.to_list(value)

class MyStaticMethods:
    @staticmethod
    def to_list(value):
        return [value] if not isinstance(value, list) else value