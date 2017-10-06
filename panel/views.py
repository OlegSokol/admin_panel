from django.shortcuts import render, get_object_or_404
from panel.models import Order


def index(request):
    all_orders = Order.objects.all()
    context = {
        'all_orders': all_orders
    }
    return render(request, 'panel/index.html', context)


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    statuses = order.ORDER_STATUS
    return render(request, 'panel/detail.html', {'order': order, 'statuses': statuses})


def update_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    statuses = order.ORDER_STATUS
    order.status = request.POST['status']
    order.save()
    return render(request, 'panel/detail.html', {'order': order, 'statuses': statuses})
