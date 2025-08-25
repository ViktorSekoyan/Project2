from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('shop_single/',views.shop_single,name='shop_single'),
    path('sucess/',views.sucess,name='sucess'),
    path('sucess2/',views.sucess2, name='sucess2')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)