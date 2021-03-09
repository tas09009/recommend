from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from .models import Meal
from django.http import HttpResponse
import requests

# Create your views here.

# def index(response, id):
# 	ls = ToDoList.objects.get(id=id)
# 	return render(response, "recommend/list.html", {"ls":ls})

def home(response):
	return render(response, "recommend/home.html", {})
class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()




def get_meals(request):
    all_meals = {}
    if 'name' in request.GET:
        name = request.GET['name']
        url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=%s' % name
        response = requests.get(url)
        data = response.json()
        meals = data['meals']

        try:
            for i in meals:
                meal_data = Meal(
                    name = i['strMeal'],
                    category = i['strCategory'],
                    instructions = i['strInstructions'],
                    region = i['strArea'],
                    slug = i['idMeal'],
                    image_url = i['strMealThumb']
                )
                meal_data.save()
                all_meals = Meal.objects.all().order_by('-id')
        except TypeError:
            return HttpResponse("No results")

    return render (request, 'recommend/meal.html', { "all_meals": all_meals} )

def meal_detail(request, id):
    meal = Meal.objects.get(id = id)
    print(meal)
    return render (
        request,
        'recommend/meal_detail.html',
        {'meal': meal}
    )
