from . import views
from django.urls import path
urlpatterns = [
    path('login_user',views.login_user,name="login_user"),
    path('logout_view',views.logout_view,name="logout_view"),
    path('login_page',views.login_page,name='login_page'),
    path('',views.dashboard,name='dashboard')
   

]
