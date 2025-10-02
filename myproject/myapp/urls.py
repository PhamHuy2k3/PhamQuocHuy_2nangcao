from django.urls import path
from .views import (
    admin_dashboard_index,
    PostListView, PostCreateView, PostUpdateView, PostDeleteView,
    ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView,
    AboutDetailListView, AboutDetailCreateView, AboutDetailUpdateView, AboutDetailDeleteView,
    UserListView, UserCreateView, UserUpdateView, UserDeleteView
)

urlpatterns = [
    path('', admin_dashboard_index, name='admin_dashboard_index'),
    path('posts/', PostListView.as_view(), name='post_list_admin'),
    path('posts/create/', PostCreateView.as_view(), name='post_create_admin'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update_admin'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete_admin'),
    path('products/', ProductListView.as_view(), name='product_list_admin'),
    path('products/create/', ProductCreateView.as_view(), name='product_create_admin'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update_admin'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete_admin'),
    path('about/', AboutDetailListView.as_view(), name='about_list_admin'),
    path('about/create/', AboutDetailCreateView.as_view(), name='about_create_admin'),
    path('about/<int:pk>/update/', AboutDetailUpdateView.as_view(), name='about_update_admin'),
    path('about/<int:pk>/delete/', AboutDetailDeleteView.as_view(), name='about_delete_admin'),
    path('users/', UserListView.as_view(), name='user_list_admin'),
    path('users/create/', UserCreateView.as_view(), name='user_create_admin'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update_admin'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete_admin'),
]
