from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from core.models import Car
from django.db.models import Q
from django.urls import reverse_lazy
from core.forms import CarForm
from django.shortcuts import get_object_or_404



# Create your views here.

class Home(ListView):
    model = Car
    template_name = 'index.html'


class Upload(CreateView):
    template_name = 'upload.html'
    form_class = CarForm


def search_ride(request):
    con = {}
    query = []
    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            results = Car.objects.filter(Q(name__iexact=query) | Q(name__icontains=query))
            con = {"query":query, "queryset": results}

    return render(request,'find.html',con)





class Update(UpdateView):
    #model = Car
    template_name = 'upload.html'
    form_class = CarForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Car, id=id_)


class Delete(DeleteView):
    model = Car
    template_name = 'delete.html'
    success_url = reverse_lazy('home')



