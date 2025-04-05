from django.urls import path
from .import views

app_name = 'mobileapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/',views.create_product,name='create'),
    path('list/',views.list_Products,name='list'),
    path('delete/<int:id>/', views.deletepdt, name='delete'),
    path('edit/<int:id>',views.edit_pdtlist,name='edit'),
    path('detail/<int:id>/', views.pdt_detail, name='detail'), 
]
