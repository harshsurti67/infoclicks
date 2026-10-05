from django.urls import path
from .views import ContactEnquiryListCreateView

urlpatterns = [
    path('contact/', ContactEnquiryListCreateView.as_view(), name='contact-list-create'),
]
