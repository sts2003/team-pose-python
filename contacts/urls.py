from django.urls import path
from contacts import views as contact_views

app_name = "contacts"

urlpatterns = [path("send/", contact_views.renderContact, name="send")]
