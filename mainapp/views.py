from django.shortcuts import render
from .models import Type, Subcategory, Medicine, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index_view(request):
    # result = get_metrics.delay(url=request.path, method=request.method)
    # print(result)
    # print(result.id)
    # print(type(result))
    # print(result.status)
    # print(result.result)

    medicine = Medicine.objects.all()
    print(medicine)

    return render(request, 'mainapp/index.html', {'medicine': medicine})


class CategoryListView(ListView):
    model = Medicine


class CategoryDetailView(DetailView):
    model = Medicine


class CategoryCreateView(CreateView):
    model = Medicine
    fields = '__all__'
    success_url = '/medicine-list/'


class CategoryUpdateView(UpdateView):
    model = Medicine
    fields = '__all__'
    success_url = '/medicine-list/'