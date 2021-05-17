from django.urls import path
from store import views

app_name = 'store'
urlpatterns = [
    path('', views.home, name="store"),    
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:id>/edit', views.edit_view, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('post_category', views.post_category, name='post_category'),
    path('post_product', views.post_product, name='post_product')
]
 