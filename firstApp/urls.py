
from django.urls import path
from .views import first_view

urlpatterns = [
    path('admin/', first_view.site),
]
