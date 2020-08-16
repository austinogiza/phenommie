
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('digi.urls')),
    path('', include('blog.urls')),
    path('', include('course.urls')),
    path('', include('order.urls')),

    path('accounts/', include('allauth.urls')),
    path("paystack", include(('paystack.urls', 'paystack'), namespace='paystack')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
