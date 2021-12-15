from django.shortcuts import render, get_object_or_404
from .models import category, subcategory, item


def main_view(request, category_slug=None, subcategory_slug=None):
	val = request.POST.get('select')
	if val == '1':
		sort = 'price_rub'
	else:
		sort = '-price_rub'
	all_items = item.objects.order_by(sort)
	categories = category.objects.all()
	all_categories = category.objects.all()
	current_category = category.objects.filter(slug=category_slug).first()
	current_subcategories = subcategory.objects.filter(category=current_category)
	current_subcategory1 = subcategory.objects.filter(slug=subcategory_slug).first()

	items = []
	sorted_items_by_category = []
	sorted_items_by_subcategory = []

	for item_object in item.objects.filter(category=current_subcategory1).order_by(sort):
		sorted_items_by_subcategory.append(item_object)

	for current_subcategory in current_subcategories:
		for item_object in item.objects.filter(category=current_subcategory):
			items.append(item_object)
	for j in all_items:
		for i in items:
			if i == j:
				sorted_items_by_category.append(i)

	content = {
		'categories': categories,
		'all_categories': all_categories,
		'current_category': current_category,
		'current_subcategories': current_subcategories,
		'current_subcategory': current_subcategory1,
		'all_items': all_items,
		'items': items,
		'sorted_items_by_category': sorted_items_by_category,
		'sorted_items_by_subcategory': sorted_items_by_subcategory,



	}
	return render(request, 'main_catalog.html', content)


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
