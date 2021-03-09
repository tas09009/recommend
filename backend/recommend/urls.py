from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getISBN, name = "getISBN"),
    # path("isbns/<int:id>/", views.isbn_detail, name = "isbn_detail")
    path('', views.get_meals, name = "get_meals"),
    path('meals/<int:id>/',views.meal_detail, name = "meal_detail")
]