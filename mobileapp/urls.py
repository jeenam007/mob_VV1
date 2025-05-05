from django.urls import path
from .import views

app_name = 'mobileapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/',views.create_product,name='create'),
    path('list/',views.list_Products,name='list'),
    path('delete/<int:id>/', views.deletepdt, name='delete'),
    path('edit/<int:id>',views.edit_pdtlist,name='edit'),
    path('detail/<int:id>/', views.pdt_detail, name='detail'),
    path('cart/<int:id>/',views.add_to_cart,name='addcart'),
    path('cartview',views.my_cart,name='viewcart'),
    path('decrease/<int:id>/',views.decrease_quantity,name='decrease_quantity'),
    path('deleteitem/<int:id>',views.remove_from_cart,name='removeitem'), 
    path('placeorder/<int:id>/', views.place_order, name='place_order'),
    path('order-status/', views.order_status, name='order_status'),
    path('cancel-order/<str:order_id>/', views.cancel_order, name='cancel_order'),

]
