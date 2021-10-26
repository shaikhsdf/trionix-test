from django.urls import path
from . import views

urlpatterns=[
    path('student/',views.studentApi),
    path('student/<int:id>/',views.studentApi),
]