from django.urls import path
from .views import Example1List, Example1Detail

urlpatterns = [
    path("", Example1List.as_view(), name="ex_apiview_list"),
    path("<int:pk>/", Example1Detail.as_view(), name="ex_apiview_detail"),
]
