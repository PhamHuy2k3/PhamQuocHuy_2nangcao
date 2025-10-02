"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp.views import (
    IndexView, ContactView, PostDetailView, ProductDetailView, PostListView,
    ProductListView, ProductListByCategoryView, AboutView, AboutDetailView,
    AddToCartView, AddToWishlistView, RemoveFromWishlistView, ViewWishlistView,
    RemoveFromCartView, ViewCartView, ProfileView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("admin-dashboard/", include('myapp.urls')),
    path("", IndexView.as_view(), name="index"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path('about/<slug:slug>/', AboutDetailView.as_view(), name='about_detail'),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("blog/", PostListView.as_view(), name="post_list"),
    path("products/<slug:category_slug>/", ProductListByCategoryView.as_view(), name="product_list_by_category"),
    path("products/", ProductListView.as_view(), name="product_list"),

    # Cart and Wishlist URLs
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/', ViewCartView.as_view(), name='view_cart'),
    path('wishlist/add/<int:product_id>/', AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>/', RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),
    path('wishlist/', ViewWishlistView.as_view(), name='view_wishlist'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
