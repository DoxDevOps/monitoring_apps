from django.urls import path

from monitoring_apps.apps import views

app_name = "apps"


# sources
urlpatterns = [
    path("apps/list", view=views.list_app_view, name="list_app"),
]
