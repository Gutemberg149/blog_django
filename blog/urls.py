from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blogs'

urlpatterns = [
    path('',views.BlogAllList.as_view(), name = 'BlogAllList'),
    path('product_detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('create/', views.post_create, name='post_create'),
    path('delele/<slug:slug>/',views.delete_post, name='delete_post'),
    path('edit/<slug:slug>', views.edit_post,name="edit_post")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
