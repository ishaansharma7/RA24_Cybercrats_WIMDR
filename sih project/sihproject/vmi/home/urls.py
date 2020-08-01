from django.contrib import admin
from django.urls import path
import include
from home import views

urlpatterns = [
    path('', views.home),

    path('Toyota', views.toyota),
    path('Suzuki', views.suzuki),
    path('Kia', views.kia),
    
    path('navsearch', views.navsearch),

    path('Toyota/<username>/', views.car_detail),
    path('Suzuki/<username>/', views.car_detail),
    path('Kia/<username>/', views.car_detail),

    path('select_brand', views.brand_select),
    path('service_loc', views.service_loc),
    path('parts_list', views.semi_submit),
    path('final_submit', views.final_submit)

]