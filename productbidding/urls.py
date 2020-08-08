"""bidding URL Configuration

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

from django.urls import path
from . import views
from django.conf.urls.static import static
from bidding import settings
urlpatterns = [
    path('', views.home),
    path('home/',views.home),
    path('search/',views.search),
    path('about/',views.about),
    path('contact/',views.contact),
    path('cat/<int:pk>/',views.Categoryshow),
    path('checkout/',views.checkout),
    path('thank/',views.Order),
    path('bid/<int:pk>/',views.bid),
    path('amountupdate/<int:pk>/',views.bidamount),
    path('wineers/',views.bidwinners),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
