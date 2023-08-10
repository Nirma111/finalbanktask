from . import views
from django.urls import path
app_name='bankapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('postlogin',views.postlogin,name='postlogin'),
    path('get_branches',views.get_branches, name='get_branches'),

]