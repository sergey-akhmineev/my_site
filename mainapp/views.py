from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Type, Subcategory, Medicine, Category, Order, OrderItem
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse


def index_view(request):
    medicine = Medicine.objects.all()
    print(medicine)

    return render(request, 'mainapp/index.html', {'medicine': medicine})


class MedicineListView(LoginRequiredMixin, ListView):
    model = Medicine


class MedicineDetailView(DetailView):
    model = Medicine


class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    fields = '__all__'
    success_url = '/medicine-list/'


class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicine
    fields = '__all__'
    success_url = '/medicine-list/'


class MedicineDeleteView(UserPassesTestMixin, DeleteView):
    model = Medicine
    fields = '__all__'
    success_url = '/medicine-list/'


def add_to_cart(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)

    if not request.user.is_authenticated:
        return redirect('login')

    order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)

    order_item, created = order.order_items.get_or_create(medicine=medicine)
    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart')


def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    order, _ = Order.objects.get_or_create(user=request.user, is_paid=False)
    order_items = order.order_items.all()

    context = {'order': order, 'order_items': order_items}
    return render(request, 'mainapp/cart.html', context)


def remove_from_cart(request, order_item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    order_item = get_object_or_404(OrderItem, id=order_item_id)

    if order_item.order.user == request.user:
        order_item.delete()

    return redirect('cart')


def user_profile(request):
    order_items = OrderItem.objects.filter(order__user=request.user, order__is_paid=True)
    return render(request, 'mainapp/user_profile.html', {'order_items': order_items})


def checkout_order(request):
    order = Order.objects.filter(user=request.user, is_paid=False).first()
    if order:
        order.is_paid = True
        order.save()
    return redirect('user_profile')


def update_quantity(request, item_id, action):
    if request.method == 'POST':
        try:
            item = OrderItem.objects.get(id=item_id)
            if action == 'increase':
                item.quantity += 1
            elif action == 'decrease':
                item.quantity -= 1
                if item.quantity <= 0:
                    item.delete()
                    return JsonResponse({'status': 'success'}, safe=False)
            item.save()
            return JsonResponse({'status': 'success'}, safe=False)
        except OrderItem.DoesNotExist:
            return JsonResponse({'status': 'failed'}, safe=False)
    else:
        return JsonResponse({'status': 'failed'}, safe=False)


def search(request):
    query = request.GET.get('query')
    if query:
        medicines = Medicine.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        medicines = None

    return render(request, 'mainapp/search_results.html', {'medicines': medicines})