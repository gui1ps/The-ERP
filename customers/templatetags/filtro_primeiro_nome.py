from django import template
register = template.Library()

@register.filter
def primeiro_nome(nome_completo):
    if(isinstance(nome_completo,str)):
        return nome_completo.split(' ')[0]
    else:
        return None