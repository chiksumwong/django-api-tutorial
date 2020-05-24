"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),  # for dev, comment for production
    path('t1/', include('tutorial1.urls')),
    path('t2/', include('tutorial2.urls')),
    path('t3/', include('tutorial3.urls')),
    path('t4/', include('tutorial4.urls')),
    path('t5/', include('tutorial5.urls')),
    path('t6/', include('tutorial6.urls')),
]
