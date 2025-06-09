from django.urls import path,include
from myweather import views

urlpatterns = [

    # Include the URLs from the myweather app
    path('', views.weather_view, name='weather_view'),
]
