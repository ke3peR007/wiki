from django.urls import path

from . import views


app_name = "wikis"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.get_page, name="get_page"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page")
]
