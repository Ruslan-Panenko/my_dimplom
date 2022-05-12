from django.shortcuts import render, get_object_or_404
from .models import category, subcategory, item
from cart.forms import CartAddProductForm

def main_view(request, category_slug=None, subcategory_slug=None):
	current_page = 'shop'
	if category_slug and subcategory_slug:
		if get_object_or_404(category, slug=category_slug):
			get_object_or_404(subcategory, slug=subcategory_slug)

	elif category_slug:
		get_object_or_404(category, slug=category_slug)

	value = request.GET.get('select')
	if value is None:
		value = 'title'
	all_items = item.objects.order_by(value)
	categories = category.objects.all()
	all_categories = category.objects.all()
	current_category = category.objects.filter(slug=category_slug).first()
	current_subcategories = subcategory.objects.filter(category=current_category)
	current_subcategory1 = subcategory.objects.filter(slug=subcategory_slug).first()
	cart_product_form = CartAddProductForm()
	items = []
	sorted_items_by_category = []
	sorted_items_by_subcategory = []

	for item_object in item.objects.filter(category=current_subcategory1).order_by(value):
		sorted_items_by_subcategory.append(item_object)

	for current_subcategory in current_subcategories:
		for item_object in item.objects.filter(category=current_subcategory):
			items.append(item_object)
	for j in all_items:
		for i in items:
			if i == j:
				sorted_items_by_category.append(i)

	content = {
		'value': value,
		'categories': categories,
		'all_categories': all_categories,
		'current_category': current_category,
		'current_subcategories': current_subcategories,
		'current_subcategory': current_subcategory1,
		'all_items': all_items,
		'items': items,
		'sorted_items_by_category': sorted_items_by_category,
		'sorted_items_by_subcategory': sorted_items_by_subcategory,
		'cart_product_form': cart_product_form,
		'current_page': current_page,



	}
	return render(request, 'main_catalog.html', content)


def item_view(request, category_slug, subcategory_slug, item_slug):
	if category_slug and subcategory_slug:
		if get_object_or_404(category, slug=category_slug):
			get_object_or_404(subcategory, slug=subcategory_slug)
	subcategory_item = subcategory.objects.filter(slug=subcategory_slug).first()
	get_object_or_404(item, slug=item_slug, category=subcategory_item)
	current_item = item.objects.filter(slug=item_slug)
	cart_product_form = CartAddProductForm()
	items = item.objects.filter(slug=item_slug)

	content = {
		'category_slug': category_slug,
		'subcategory_slug': subcategory_slug,
		'item_slug': item_slug,
		'current_item': current_item,
		'cart_product_form':cart_product_form,
		'items': items
	}

	return render(request, 'catalog-item.html', content)



def cart(request):

	return render(request, 'cart.html')
