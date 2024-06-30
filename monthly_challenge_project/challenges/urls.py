from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:month>/',views.month_number),
    path('<str:month>/',views.month,name='challenge_path'),
]
