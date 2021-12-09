from django.urls import path, include

from profiles_api import views


# maps the url to django views
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
