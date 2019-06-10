from django.contrib import admin
from django.urls import path

from micro_blog.views import CreateMessage

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', CreateMessage.as_view(), name='blog-home'),
]
