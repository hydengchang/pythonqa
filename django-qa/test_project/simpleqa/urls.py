import debug_toolbar
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from core.views import register, user_login, user_logout

admin.sites.AdminSite.site_header = 'QA管理系统'
admin.sites.AdminSite.site_title = '标题'
admin.sites.AdminSite.index_title = '管理员操作'

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    url(r'^', include('qa.urls')),
]
