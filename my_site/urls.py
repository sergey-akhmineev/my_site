"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from userapp.views import RegisterView, LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index_view'),
    path('medicine-list/', views.MedicineListView.as_view(), name='medicine_list'),
    path('medicine-detail/<int:pk>/', views.MedicineDetailView.as_view(), name='medicine_detail'),
    path('medicine-update/<int:pk>/', views.MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine-delete/<int:pk>/', views.MedicineDeleteView.as_view(), name='medicine_delete'),
    path('medicine-create/', views.MedicineCreateView.as_view(), name='medicine_create'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
