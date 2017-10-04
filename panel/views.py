from django.shortcuts import render
from django.http import Http404
from panel.models import Order


def index(request):
    all_orders = Order.objects.all()
    context = {
        'all_orders': all_orders
    }
    return render(request, 'panel/index.html', context)


def order_detail(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        raise Http404("Order does not exists")
    return render(request, 'panel/detail.html', {'order': order})
