from django.urls import path
from . import views


urlpatterns = [
    path('', views.LeaveListView.as_view(), name='leave_list'),
    path('<int:pk>/edit/', views.LeaveUpdateView.as_view(), name='leave_edit'),
]
