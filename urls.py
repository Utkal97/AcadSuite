"""AcadSuite URL Configuration

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
from django.contrib import admin
from django.urls import path, include, URLPattern   #"include" is added for including our app's redirections
from django.contrib.auth import views as auth_views
from Home import views as home_views
from ShareResource import views as resource_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True,template_name='Accounts/login.html'), name = 'user-sign-in'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Home/home.html'), name = 'user-sign-out'),
    path('accounts/', include('Accounts.urls')),
    path('discussion/', include('Discussion.urls')),
    path('resources/', include('ShareResource.urls'))
    #URLPattern(r'^$', home_views.home, name = 'redirect-home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)