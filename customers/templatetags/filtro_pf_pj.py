from django import template
register = template.Library()

@register.filter
def filtro_pf_pj(tipo):
    if(isinstance(tipo,str)):
        if(tipo=='PF'):
            return 'CPF'
        else:
            return 'CNPJ'