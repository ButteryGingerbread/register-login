from django.urls import path
from . import views

urlpatterns = [
    path("display-data/", views.display_all, name='display_data'),
    path('display-data/<str:menu_category>/', views.display_data_by_category, name='display_menu_by_category'),
]