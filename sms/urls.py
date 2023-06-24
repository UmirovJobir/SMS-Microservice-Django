from django.urls import path
from .views import SMSView

urlpatterns = [
    path('send_sms/', SMSView.as_view(), name='send-sms')
]