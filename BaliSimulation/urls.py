"""BaliSimulation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views 1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home') Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from bali import views


urlpatterns = [
    url(r'^$',views.add,name="index"),
    url(r'^faq/$',views.faq,name="faq"),
    url(r'^readBalise/$',views.show_data,name="show_data"),
    url(r'^intro/$',views.intro,name="intro"),
    url(r'^operation/$',views.operation,name="operation"),
    url(r'^readBalise/$',views.readBalise,name="readBalise"),

    url(r'^writeBalise/$',views.writeBalise,name="writeBalise"),
    url(r'^writeBalise/writeTele$',views.writeTele,name="writeTele"),

    url(r'^about/$',views.about,name="about"),
    url(r'^readLEU/$',views.readLEU,name="readLEU"),
    url(r'^writeLEU/$',views.writeLEU,name="writeLEU"),
    url(r'^analysizeTelegram/$',views.analysizeTelegram,name="analysizeTelegram"),
#    url(r'^analysizeTelegram/$',views.myextract_tele,name="myextract_tele"),
    url(r'^generateTelegram/$',views.generateTelegram,name="generateTelegram"),
    url(r'^testBaliseSwitch/$',views.testBaliseSwitch,name="testBaliseSwitch"),
    url(r'^testBaliseNoSwitch/$',views.testBaliseNoSwitch,name="testBaliseNoSwitch"),
    url(r'^test/$',views.test,name="test"),
    url(r'^admin/', admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
