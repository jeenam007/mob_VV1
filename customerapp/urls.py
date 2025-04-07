from django.urls import path
from .import views
app_name = 'customerapp'

urlpatterns = [
    # path('', views.home, name='home'),
    path('Register/',views.registration,name='register'), 
    path('userlist/',views.userlist,name='userlist'),
    path('deleteuser/<int:id>/',views.userdelete,name='deluser'),
    path('edituser/<int:id>/',views.useredit,name='edituser'),
    path('userdetail/<int:id>/',views.userdet,name='userdetl'),
    path('',views.login_view,name='userlogin'),
    path('signout/',views.sign_out,name='signout')
]
