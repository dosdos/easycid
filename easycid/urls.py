"""easycid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

from cid.urls import router
from cid.views import api_docs


admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^vehicles/', include('cid.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api/docs/', api_docs),
]
