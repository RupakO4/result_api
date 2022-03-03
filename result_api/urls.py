from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('exam/', views.getExam),
    #path('results/<str:pk1>/', views.getYearResults),
    path('exam/<str:pk1>/<str:pk2>', views.getResult),
]
