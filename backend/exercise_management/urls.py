# exercise_management/urls.py
from django.urls import path
from . import views


urlpatterns = [

    # Exercises
    path('exercises/', views.exercise_list, name='exercise_list'),
    path('exercise/<int:pk>/', views.exercise_detail, name='exercise_detail'),
    path('exercise/create/', views.exercise_create, name='exercise_create'),
    path('exercise/update/<int:pk>/', views.exercise_update, name='exercise_update'),

    # Exercise Categories
    path('exercise-categories/', views.exercise_category_list, name='exercise_category_list'),
    path('exercise-category/create/', views.exercise_category_create, name='exercise_category_create'),
    path('exercise-category/update/<int:pk>/', views.exercise_category_update, name='exercise_category_update'),
    path('exercise-category/delete/<int:pk>/', views.exercise_category_delete, name='exercise_category_delete'),

    # Equipment Categories
    path('equipment-categories/', views.equipment_category_list, name='equipment_category_list'),
    path('equipment-category/create/', views.equipment_category_create, name='equipment_category_create'),
]
