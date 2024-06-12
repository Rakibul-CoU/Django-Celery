from django.urls import path

from api.views import auto_reject

urlpatterns = [
    path('auto-reject/', auto_reject, name='auto-reject')
]