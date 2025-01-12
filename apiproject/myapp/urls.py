from django.urls import path
from django.urls.conf import include
from myapp.views import contactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contact', contactViewSet, basename='contact')
    
urlpatterns = [
    path('',include(router.urls))

]

          
