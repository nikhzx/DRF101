from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentapi/", views.StudentListCreate.as_view()),
    # path("studentapi/<int:pk>", views.StudentRetrieve.as_view()),
    path("studentapi/<int:pk>", views.StudentRetrieveUpdateDestroy.as_view()),
]
