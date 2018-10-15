from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from core.models import Car
from django.db.models import Q
from django.urls import reverse
from core.forms import CarForm
from django.shortcuts import get_object_or_404



# Create your views here.

class Home(ListView):
    model = Car
    queryset = Car.objects.order_by('price')
    template_name = 'index.html'


class Upload(CreateView):
    template_name = 'upload.html'
    form_class = CarForm


def search_ride(request):
    con = {}
    query = []
    no_results = 0
    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            results = Car.objects.filter(Q(name__iexact=query) | Q(name__icontains=query))
            con = {"query":query, "queryset": results}

    return render(request,'find.html',con)





class Update(UpdateView):
    template_name = 'update.html'
    form_class = CarForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Car, id=id_)


class Delete(DeleteView):
    #model = Car
    template_name = 'delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Car, id=id_)

    def get_success_url(self):
        return reverse('app:home')

