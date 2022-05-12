from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from sale import views

urlpatterns = [
                  path('about/', views.about),
                  path('delivery/', views.delivery),
                  path('contact/', views.contact),

                  path('admin/', admin.site.urls),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('coupons/', include('sale.urls', namespace='coupons')),
                  path('order/', include('order.urls', namespace='order')),

                  path('', include('shop.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
