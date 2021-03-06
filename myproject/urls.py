"""myproject URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from share.views import HomeView,DisplayView,MyView,SearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view(),name='home'),
    #因为是以对象的形式去调用视图,必须要加括号,而不是 as_view
    url(r'^f/(?P<code>\d+)/$',DisplayView.as_view(),name='display'),
    url(r'^my/$',MyView.as_view(),name='my'),
    url(r'^search/',SearchView.as_view(),name='search')
]
