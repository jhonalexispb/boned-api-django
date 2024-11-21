from django.urls import path

from . import views

urlpatterns = [
    path('lineas_farmaceuticas/', views.LineaFarmaceuticaList.as_view()),
    path('lineas_farmaceuticas/create/', views.LineaFarmaceuticaCreate.as_view()),
    path('lineas_farmaceuticas/detail/<int:pk>/', views.LineaFarmaceuticaDetail.as_view()),
    path('lineas_farmaceuticas/delete/<int:pk>/', views.LineaFarmaceuticaDelete.as_view()),
    path('lineas_farmaceuticas/update/<int:pk>/', views.LineaFarmaceuticaUpdate.as_view()),
]
