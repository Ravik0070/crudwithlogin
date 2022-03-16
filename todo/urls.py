from django.urls import path
from todo import views

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.loggin,name="loggin"),
    path('logout/',views.loggout,name="loggout"),
    path('add/',views.addtodo,name="addtodo"),
    path('view/<int:id>',views.viewtodo,name="viewtodo"),
    path('edit/<int:id>',views.edittodo,name="edittodo"),
    path('delete/<int:id>',views.deletetodo,name="deletetodo"),
]
