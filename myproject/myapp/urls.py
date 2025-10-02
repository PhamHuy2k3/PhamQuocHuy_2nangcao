from django.urls import path
from .views import (
    ContactView, PostDetailView, ProductDetailView, PostListView,
    ProductListView, ProductListByCategoryView, AboutView, AboutDetailView,
    AddToCartView, AddToWishlistView, RemoveFromWishlistView, ViewWishlistView,
    RemoveFromCartView, ViewCartView, ProfileView, AdminDashboardIndexView,
    PostAdminListView, PostAdminCreateView, PostAdminUpdateView, PostAdminDeleteView,
    ProductAdminListView, ProductAdminCreateView, ProductAdminUpdateView, ProductAdminDeleteView,
    AboutDetailAdminListView, AboutDetailAdminCreateView, AboutDetailAdminUpdateView, AboutDetailAdminDeleteView,
    UserAdminListView, UserAdminCreateView, UserAdminUpdateView, UserAdminDeleteView
)

urlpatterns = [
    path('', AdminDashboardIndexView.as_view(), name='admin_dashboard_index'),

    # Admin views
    path('admin/posts/', PostAdminListView.as_view(), name='post_list_admin'),
    path('admin/posts/create/', PostAdminCreateView.as_view(), name='post_create_admin'),
    path('admin/posts/<int:pk>/update/', PostAdminUpdateView.as_view(), name='post_update_admin'),
    path('admin/posts/<int:pk>/delete/', PostAdminDeleteView.as_view(), name='post_delete_admin'),

    path('admin/products/', ProductAdminListView.as_view(), name='product_list_admin'),
    path('admin/products/create/', ProductAdminCreateView.as_view(), name='product_create_admin'),
    path('admin/products/<int:pk>/update/', ProductAdminUpdateView.as_view(), name='product_update_admin'),
    path('admin/products/<int:pk>/delete/', ProductAdminDeleteView.as_view(), name='product_delete_admin'),

    path('admin/about/', AboutDetailAdminListView.as_view(), name='about_list_admin'),
    path('admin/about/create/', AboutDetailAdminCreateView.as_view(), name='about_create_admin'),
    path('admin/about/<int:pk>/update/', AboutDetailAdminUpdateView.as_view(), name='about_update_admin'),
    path('admin/about/<int:pk>/delete/', AboutDetailAdminDeleteView.as_view(), name='about_delete_admin'),

    path('admin/users/', UserAdminListView.as_view(), name='user_list_admin'),
    path('admin/users/create/', UserAdminCreateView.as_view(), name='user_create_admin'),
    path('admin/users/<int:pk>/update/', UserAdminUpdateView.as_view(), name='user_update_admin'),
    path('admin/users/<int:pk>/delete/', UserAdminDeleteView.as_view(), name='user_delete_admin'),
]
