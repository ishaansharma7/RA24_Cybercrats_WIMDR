from django.contrib import admin
from django.urls import path
import include
from home import views

urlpatterns = [
    path('', views.home),

    path('Toyota', views.toyota),
    path('Suzuki', views.suzuki),
    path('Kia', views.kia),
    path('Hyundai', views.hyundai),
    path('Tata', views.tata),
    path('Honda', views.honda),
    
    path('navsearch', views.navsearch),

    path('Toyota/<username>/', views.car_detail),
    path('Suzuki/<username>/', views.car_detail),
    path('Kia/<username>/', views.car_detail),
    path('Tata/<username>/', views.car_detail),
    path('Hyundai/<username>/', views.car_detail),
    path('Honda/<username>/', views.car_detail),

    path('select_brand', views.brand_select),
    path('service_loc', views.service_loc),
    path('parts_list', views.semi_submit),
    path('final_submit', views.final_submit),
    path('rank', views.rank),
    path('comp_ask', views.comp_ask),
    path('comp_done', views.comp_done)

]
