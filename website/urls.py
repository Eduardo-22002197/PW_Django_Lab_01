from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page_view, name = "home"),
    path('python', views.python_page_view, name = "python"),
    path('django', views.django_page_view, name = "django"),
    path('web_dev', views.web_dev_page_view, name = "web_dev"),
]