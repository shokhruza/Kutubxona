from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('apps.books.urls')),
    path('api/orders/', include('apps.orders.urls')),
    path('api/ratings/', include('apps.ratings.urls')),
    # path('api/users/', include('apps.users.urls')),  # foydalanuvchi endpointlari kerak bo‘lsa
]