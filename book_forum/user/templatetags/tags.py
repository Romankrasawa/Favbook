from django import template

register = template.Library()


@register.simple_tag()
def num_to_short(num):
    try:
        if int(num) >= 1000000000:
            str_num = str(num // 1000000000) + "млрд"
        elif int(num) >= 1000000:
            str_num = str(num // 1000000) + "млн"
        elif int(num) >= 1000:
            str_num = str(num // 1000) + "к"
        else:
            str_num = str(num)
    except:
        str_num = "0"
    return str_num


@register.simple_tag
def query_transform(request, **kwargs):
    updated = request.GET.copy()
    for k, v in kwargs.items():
        if v is not None:
            updated[k] = v
        else:
            updated.pop(k, 0)

    return updated.urlencode()
