from django.contrib import admin
from .models import category, subcategory, item,  discount, coupon
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib.auth.models import User, Group
import string
import random
from modeltranslation.admin import TranslationAdmin, TranslationStackedInline









class subcategory_admin(SortableAdminMixin, TranslationAdmin):
	save_as = True
	save_on_top = True
	prepopulated_fields = {'slug': ('title',)}


class category_admin(SortableAdminMixin, TranslationAdmin):
	save_as = True
	save_on_top = True
	prepopulated_fields = {'slug': ('title',)}


class item_admin(SortableAdminMixin, TranslationAdmin):
	save_on_top = True

	list_display = ('category', 'is_active')
	prepopulated_fields = {'slug': ('title',)}


	def get_fields(self, request, obj=None):
		fields = super().get_fields(request, obj)
		fields = fields[-1:] + fields[:-1]
		return fields


admin.site.register(item, item_admin)
admin.site.register(category, category_admin)
admin.site.register(subcategory, subcategory_admin)
admin.site.unregister([User, Group])
