from django.shortcuts import render
from .models import House, Category, PaymentMethod
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView
from .filters import HouseFilter




def index_view(request):
    houses = House.objects.filter(is_active=True)[:6]
    return render(request, 'app/index.html', {'houses': houses})

class HouseListView(ListView):
    model = House
    template_name = 'app/house_list.html'
    context_object_name = 'houses'
    filterset_class = HouseFilter
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()

        self.filterset = HouseFilter(self.request.GET, queryset=queryset)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter'] = self.filterset
        houses = context['houses']
        paginator = Paginator(houses, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            houses = paginator.page(page)
        except PageNotAnInteger:
            houses = paginator.page(1)
        except EmptyPage:
            houses = paginator.page(paginator.num_pages)
        context['houses'] = houses

        return context


def house_detail_view(request, pk):
    house = House.objects.filter(id=pk).first()
    print(house)

    return render(request, 'app/house_detail.html', {'house': house})
