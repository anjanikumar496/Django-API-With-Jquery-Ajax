from django.urls import path
from . import views
urlpatterns = [
path('api/lead/', views.LeadListCreate.as_view() ),
path('api/data/<int:pk>/', views.LeadListCreate_data.as_view() ),
]