from django.shortcuts import render, get_object_or_404
from django.views import generic
from panel.models import Order


class IndexView(generic.ListView):
    template_name = 'panel/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.all()


class DetailView(generic.DetailView):
    model = Order
    template_name = 'panel/detail.html'


def update_status(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    statuses = order.ORDER_STATUS
    order.status = request.POST['status']
    order.save()
    return render(request, 'panel/detail.html', {'order': order, 'statuses': statuses})
