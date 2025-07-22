from django.urls import path
from . import views

app_name = "documentation"

urlpatterns = [
    path("", views.documentation, name="documentation"),
    path("open_article/<selectedTitle>", views.open_article, name="open_article"), 
    path("edit_article/<selectedTitle>", views.edit_article, name="edit_article"), 
    path("save_change/<selectedTitle>", views.save_change, name="save_change"),
]