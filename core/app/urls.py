from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('house_list/', views.HouseListView.as_view(), name='houses'),
    path('house_detail/<int:pk>/', views.house_detail_view, name='house_detail')
]
