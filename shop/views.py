from django.shortcuts import render, get_object_or_404
from .models import category, subcategory, item


#def category_view(request, category_slug):
#	sort1 = sort(request)
#	item_list = item.objects.filter().order_by(sort1)
#	content = {
#		'item_list': item_list,
#		'category_slug': category_slug
#	}
#	return render(request, 'category_filter.html', content)


def category_view(request, category_slug):
	sort1 = sort(request)
	item_list = item.objects.order_by(sort1)
	category_list = category.objects.all()
	get_object_or_404(category, slug=category_slug)
	content = {
		'category_slug': category_slug,
		'item_list': item_list,
		'category_list': category_list
	}
	return render(request, 'category_filter.html', content)


# def subcategory_view(request, category_slug, subcategory_slug):
#	subcategory_list = item.objects.filter()
#	content = {
#		'subcategory_list': subcategory_list,
#	}
#	return render(request, 'subcategory_filter.html', content)


def subcategory_view(request, category_slug, subcategory_slug):
	sort1 = sort(request)
	item_list = item.objects.order_by(sort1)
	category_list = category.objects.all()
	get_object_or_404(category, slug=subcategory_slug)
	content = {
		'subcategory_slug': subcategory_slug,
		'category_slug': category_slug,
		'item_list': item_list,
		'category_list': category_list,
	}
	return render(request, 'subcategory_filter.html', content)


def item_view(request, category_slug, subcategory_slug, item_slug):
	subcategory_item = subcategory.objects.filter(slug=subcategory_slug).first()
	get_object_or_404(item, slug=item_slug, category=subcategory_item)
	content = {
		'category_slug': category_slug,
		'subcategory_slug': subcategory_slug,
		'item_slug': item_slug
	}
	return render(request, 'catalog-item.html', content)


def order_view(request):
	sort1 = sort(request)
	item_list = item.objects.order_by(sort1)
	category_list = category.objects.all()
	subcategory_list = subcategory.objects.all()
	return render(request, 'catalog.html', {'item_list': item_list,
											'category_list': category_list,
											'subcategory_list': subcategory_list,
											})


def sort(request):
	val = request.POST.get('select')
	if val == '1':
		return 'price_rub'
	else:
		return '-price_rub'

