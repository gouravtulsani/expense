from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.day_expenses),
    url(r'^register$', views.apiregister),
]
