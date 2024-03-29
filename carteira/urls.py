"""carteira URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_mongoengine import routers
from api import views as myapp_views

router = routers.DefaultRouter()
router.register(r'ativos', myapp_views.AtivosViewset, basename='ativo')
router.register(r'atual', myapp_views.AtualViewset, basename='atual')
router.register(r'historico', myapp_views.HistoricoViewSet, basename='historico')


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
