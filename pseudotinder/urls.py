from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^UserEdit/$', 'App.views.UserEdit'),
    url(r'^UserRegister/$', 'App.views.UserRegister'),
    url(r'^UserLogin/$', 'App.views.UserLogin'),
    url(r'^UserLogout/$', 'App.views.UserLogout'),
    url(r'^UserEdit/$', 'App.views.UserEdit'),
]

