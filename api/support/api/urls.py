from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'feedback', views.FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('faq/', views.queryset_faq, name='query'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]