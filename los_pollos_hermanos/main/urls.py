from django.urls import path
from .views import contact_send

urlpatterns = [
    path("contact/send/", contact_send, name="contact_send"),
]
