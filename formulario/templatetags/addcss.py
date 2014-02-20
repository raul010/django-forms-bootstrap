# -*- coding: utf-8 -*-
from django import template
register = template.Library()

#Não está sendo usado
@register.filter(name='addcss')
def addcss(field, css):
    return field.as_widget(attrs={"class":css})

@register.filter(name='attr')
def addTagAttr(field, data):
    datas = data.split(';')
    dict = {}
    for value in datas:
        result = value.split('=')
        attr = result[0].strip().encode("utf-8")
        value = result[1].strip().encode("utf-8")
        
        dict[attr] = value
        
    return field.as_widget(attrs=dict)