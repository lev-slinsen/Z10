from django.contrib import admin
from django.urls import path
from ..stock.views import view_p

urlpatterns = [
    path('', view_p),
    path('admin/', admin.site.urls),

]
