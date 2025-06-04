from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="index"),
    path("remera/<int:id>", views.detalle_remera, name="detalle_remera"),
    path("contacto", views.contacto, name="contacto"),
]
