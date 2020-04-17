from django.urls import path, include
from rest_framework.routers import DefaultRouter
from a_shop import views

router = DefaultRouter()
router.register(r'mayor', views.MayorViewSet)
router.register(r'city', views.CityViewSet)
router.register(r'customer', views.CustomerViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'application', views.ApplicationViewSet)

urlpatterns = [
    path('shop/', include(router.urls)),
]
