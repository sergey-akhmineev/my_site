from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import render
from .models import Type, Subcategory, Medicine, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def index_view(request):
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


class CategoryDeleteView(UserPassesTestMixin, DeleteView):
    model = Medicine
    fields = '__all__'
    success_url = '/medicine-list/'

    def test_func(self):
        return self.request.user.is_superuser


