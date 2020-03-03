from django.urls import path
from . import views

app_name = 'myBlog'

urlpatterns = [
    path(r'', views.post_list, name='list'), #全記事表示
    path('<int:pk>/', views.PostDetail, name='detail'), #記事詳細

    path('Python/', views.List_Python, name='BigCategory_lis'),#大カテゴリー　python
    path('C#/', views.List_CShrp, name='CShrp_lis'),#大カテゴリーC#
    path('creation/', views.List_creation, name='creation_lis'),#大カテゴリー創作物
    path("Django/", views.Small_List, name='small_Django'),#小カテゴリーDjango
    path("image_display/", views.Small_List_image, name='small_img'),#小カテゴリー画像

]