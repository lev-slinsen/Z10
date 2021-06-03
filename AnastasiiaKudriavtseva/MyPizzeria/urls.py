from django.contrib import admin
from django.urls import path, include
from ..stock.views import view_p

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stock/', include('stock.urls', namespace='stock')),

]
