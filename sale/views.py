from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .form import CouponApplyForm
from .models import Coupon



@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)

            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None

    return redirect('cart:cart_detail')

def about(request):
    current_page = 'about'
    return render(request, 'about.html',{'current_page': current_page}
)


def delivery(request):
    current_page = 'delivery'
    return render(request, 'delivery.html',{'current_page': current_page})


def contact(request):
    current_page = 'contact'
    return render(request, 'contact.html',{'current_page': current_page})
