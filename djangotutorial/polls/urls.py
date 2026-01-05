from django.urls import path

from . import views
# "" (empty double quotes) means home page or index page.
urlpatterns = [
    path("", views.index, name="index"),
]