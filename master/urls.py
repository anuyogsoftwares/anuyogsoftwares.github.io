from django.urls import path
from .views import HomeView


app_name = "master"


urlpatterns =[
    path("", HomeView.as_view(), name="home"),
    # path("dashboard/", DashboardView.as_view(), name="dashboard")
]