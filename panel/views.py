from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseBadRequest
from django.views import generic
from panel.models import Order


class IndexView(generic.ListView):
    template_name = 'panel/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.all()


class MyOrdersView(generic.ListView):
    model = Order
    template_name = 'panel/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id).values()


#class DetailView(generic.DetailView):
#    model = Order
#    template_name = 'panel/detail.html'


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if order.status != 'N':
        return HttpResponseBadRequest("Order already in progress.")

    statuses = order.ORDER_STATUS
    order.status = 'E'
    order.user_id = request.user.id
    order.save()
    return render(request, 'panel/detail.html', {'order': order, 'statuses': statuses})


def update_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    statuses = order.ORDER_STATUS
    order.status = request.POST['status']
    order.save()
    return render(request, 'panel/detail.html', {'order': order, 'statuses': statuses})
