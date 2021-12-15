from django.shortcuts import render, get_object_or_404
from .models import category, subcategory, item


def sort(request):
	val = request.POST.get('select')
	if val == '1':
		return 'price_rub'
	else:
		return '-price_rub'


def order_view(request):
	sort1 = sort(request)
	item_list = item.objects.order_by(sort1)
	all_categories = category.objects.all()
	content = {
		'item_list': item_list,
		'all_categories': all_categories
	}
	return render(request, 'catalog.html', content)


def category_view(request, category_slug):
	get_object_or_404(category, slug=category_slug)
	sort1 = sort(request)
	current_category = category.objects.filter(slug=category_slug).first()
	all_categories = category.objects.all()
	current_subcategories = subcategory.objects.filter(category=current_category)
	items = []
	for current_subcategory in current_subcategories:
		for item_object in item.objects.filter(category=current_subcategory).order_by(sort1):
			items.append(item_object)

	content = {
		'current_category': current_category,
		'all_categories': all_categories,
		'current_subcategories': current_subcategories,
		'items': items,

	}

	return render(request, 'category_filter.html', content)


def subcategory_view(request, category_slug, subcategory_slug):
	sort1 = sort(request)
	get_object_or_404(subcategory, slug=subcategory_slug)
	current_category = category.objects.filter(slug=category_slug).first()
	current_subcategory = subcategory.objects.filter(slug=subcategory_slug).first()
	all_categories = category.objects.all()
	current_subcategories = subcategory.objects.filter(category=current_category)
	items = []
	for item_object in item.objects.filter(category=current_subcategory).order_by(sort1):
		items.append(item_object)

	content = {
		'current_subcategories': current_subcategories,
		'all_categories': all_categories,
		'current_category': current_category,
		'current_subcategory': current_subcategory,
		'items': items,

	}

	return render(request, 'subcategory_filter.html', content)


def item_view(request, category_slug, subcategory_slug, item_slug):
	subcategory_item = subcategory.objects.filter(slug=subcategory_slug).first()
	get_object_or_404(item, slug=item_slug, category=subcategory_item)
	current_item = item.objects.filter(slug=item_slug)
	content = {
		'category_slug': category_slug,
		'subcategory_slug': subcategory_slug,
		'item_slug': item_slug,
		'current_item': current_item,
	}
	return render(request, 'catalog-item.html', content)
