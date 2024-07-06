from django import template


register = template.Library()

@register.filter()
def currency(value):
    int_value = int(value)
    months = {'Январь': 1,
              'Февраль': 2,
              'Март': 3,
              'Апрель': 4,
              'Май': 5,
              'Июнь': 6,
              'Июль': 7,
              'Август': 8,
              'Сентябрь': 9,
              'Октябрь': 10,
              'Ноябрь': 11,
              'Декабрь': 12}

    for value in months:
        if months[value] == int_value:
            return f'"{value}-%02d"' % (int_value)


@register.filter()
def percent(value):
    return f'{value}%'





@register.filter()
def translate(text):
    translate_list2 = {'iron': 'железа',
                       'content': 'Сод.',
                       'max': 'макс. зн',
                       'min': 'мин. зн',
                       'avg': 'ср. зн',
                       'si': 'кремния',
                       'ca': 'кальция',
                       'al': 'алюминия',
                       'sulfur': 'серы'
                       }
    text = text.replace('_', ' ')
    text = text.replace('  ', ' ')
    translated = list()
    for key in text.split():
        translated.append(translate_list2[key])

    translated[0], translated[1] = translated[1], translated[0]
    return " ".join(translated)