from django.urls import path

from .views import index, detail

urlpatterns = [
    path('index/', index),
    path('detail/<int:my_id>/', detail)
]
