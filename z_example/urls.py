from django.urls import path
from .views import ExampleList, ExampleDetail

urlpatterns = [
    path("", ExampleList.as_view(), name="ex_apiview_list"),
    path("<int:pk>/", ExampleDetail.as_view(), name="ex_apiview_detail"),
]
