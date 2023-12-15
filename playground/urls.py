from django.urls import path
from . import views
from .views import llm_ser


urlpatterns = [
    # path("", views.index, name="index"),
    path('', llm_ser, name='llm_ser'),
    # Add other URL patterns if needed

]