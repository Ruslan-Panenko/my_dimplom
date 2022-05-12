from django.shortcuts import render
import requests
from cart.cart import Cart
from order.models import Order, OrderItem


def main(request):
    if request.method == 'GET':
        cart = Cart(request)
        print(request.method)
        return render(request, 'order.html',
                      {'cart': cart,
                       }
                      )
    elif request.method == 'POST':
        cart = Cart(request)
        new_order = Order.objects.create(
            first_name=request.POST.get('name'),
            city=request.POST.get('city'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            comment=request.POST.get('comment'),

        )
        for item in cart:
            OrderItem.objects.create(
                order=new_order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )


        requests.post('https://api.telegram.org/bot2101702181:AAFH4THkXSR56qJGmi7tRS0Usu62PhH4ny8/sendMessage',
                      data={
                          'chat_id': '-705391204',
                          'text': f"""
            name -- {request.POST.get('name')}
            city -- {request.POST.get('city')} 
            email -- {request.POST.get('email')} 
            phone -- {request.POST.get('phone')} 
            address -- {request.POST.get('address')} 
            comment -- {request.POST.get('comment')}
             """
                      })
        cart.clear()
        return render(request, 'create_order.html')
