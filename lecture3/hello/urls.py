from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"), #could be any string we can give in url bar
    path("misha", views.misha, name="misha"),
    path("david", views.david, name="david"),
    path("world", views.html_doc, name="world"),
    path("greet1/<str:name>/", views.greet1, name="greet1")
]