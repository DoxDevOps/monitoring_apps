from apps.models import App
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView


# Create your views here.
class ListAppView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """List apps"""

    permission_required: str = "apps.view_stock"
    model = App
    paginate_by = 15
    template_name = "apps/list_app.html"
    context_object_name = "app_list"  # Set the context object name for the app list


list_app_view = ListAppView.as_view()
