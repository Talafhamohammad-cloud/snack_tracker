from django.urls import path
from .views import SnackListView, SnackDetailsView

urlpatterns = [
    path('', SnackListView.as_view(), name='snackes_lists'),
    path('<int:pk>', SnackDetailsView.as_view(), name='snackes_details')
]
