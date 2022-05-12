from modeltranslation.translator import translator, TranslationOptions
from .models import category, subcategory, item, discount, coupon

class CategoryTranslationOptions(TranslationOptions):
    pass
class SubcategoryTranslationOptions(TranslationOptions):
    pass
class ItemTranslationOptions(TranslationOptions):
    pass
class ItemTermsTranslationOptions(TranslationOptions):
    pass
class ItemFilesTranslationOptions(TranslationOptions):
    pass
class DiscountTranslationOptions(TranslationOptions):
    pass
class CouponTranslationOptions(TranslationOptions):
    pass


translator.register(category, CategoryTranslationOptions)
translator.register(subcategory, SubcategoryTranslationOptions)
translator.register(item, ItemTranslationOptions)

translator.register(discount, DiscountTranslationOptions)
translator.register(coupon, CouponTranslationOptions)