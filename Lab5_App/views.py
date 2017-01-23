from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

data = {'orders': []}
for i in range(1, 10):
    data['orders'].append(
        {
            'id': i,
            'title': '{0}{1}'.format('Заказ №', i),
            'description': 'There should be a description of some kind',
            'text': 'Imagine a whole lot of text here',
            'date': '01.01.2016'
        }
    )


def main_page(request):
    return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data_order = {
            'order': data['orders'][int(id)-1]
        }
        return render(request, 'order.html', data_order)
