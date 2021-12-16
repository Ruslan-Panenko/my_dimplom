from django.template import Library

register = Library()


@register.filter
def shop_tags(value1):
	value1 = int(value1)
	if 9999 >= value1 > 999:
		value = str(value1)[:1] + " " + str(value1)[1:]
		return value
	elif 99999 >= value1 >= 10000:
		value = str(value1)[:2] + " " + str(value1)[2:]
		return value
	elif 999999 >= value1 >= 100000:
		value = str(value1)[:3] + " " + str(value1)[3:]
		return value
	else:
		return value1
