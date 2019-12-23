from django.urls import path
from .views import *

urlpatterns = [
# path('api/lead/', views.LeadListCreate.as_view() ),
    path('', Dashboard,name="dashboard"),
    path('add_form_data', Add_Form_Data,name="add_form_data"),
]