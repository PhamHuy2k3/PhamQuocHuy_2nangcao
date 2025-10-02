from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.urls import reverse_lazy
from .models import Post, Product, AboutDetail, Category, Cart, Wishlist
from .forms import PostForm, ProductForm, AboutDetailForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]
        context['products'] = Product.objects.all().order_by('-created_at')[:5]
        context['best_selling_products'] = Product.objects.filter(is_best_selling=True)[:5]
        context['you_may_also_like_products'] = Product.objects.filter(is_you_may_also_like=True)[:5]
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['featured_products'] = Product.objects.order_by('?')[:5]
        return context

class ProductListByCategoryView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    ordering = ['-created_at']

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['category_slug'])
        return Product.objects.filter(category=self.category).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        context['featured_products'] = Product.objects.order_by('?')[:5]
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_details'] = AboutDetail.objects.all()
        return context

class AboutDetailView(DetailView):
    model = AboutDetail
    template_name = 'about_detail.html'
    context_object_name = 'about_detail'
    slug_url_kwarg = 'slug'

@method_decorator(login_required, name='dispatch')
class AddToCartView(TemplateView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, f"Added {product.name} to your cart.")
        return redirect(request.META.get('HTTP_REFERER', 'product_list'))

@method_decorator(login_required, name='dispatch')
class AddToWishlistView(TemplateView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
        if created:
            messages.success(request, f"Added {product.name} to your wishlist.")
        else:
            messages.info(request, f"{product.name} is already in your wishlist.")
        return redirect(request.META.get('HTTP_REFERER', 'product_list'))

@method_decorator(login_required, name='dispatch')
class RemoveFromWishlistView(TemplateView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        wishlist_item = get_object_or_404(Wishlist, user=request.user, product=product)
        wishlist_item.delete()
        messages.success(request, f"Removed {product.name} from your wishlist.")
        return redirect('view_wishlist')

@method_decorator(login_required, name='dispatch')
class ViewWishlistView(ListView):
    model = Wishlist
    template_name = 'wishlist.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class RemoveFromCartView(TemplateView):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart_item = get_object_or_404(Cart, user=request.user, product=product)
        cart_item.delete()
        messages.success(request, f"Removed {product.name} from your cart.")
        return redirect('view_cart')

@method_decorator(login_required, name='dispatch')
class ViewCartView(ListView):
    model = Cart
    template_name = 'cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_price'] = sum(item.get_total() for item in context['cart_items'])
        return context

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'account/profile.html'

class AdminDashboardIndexView(TemplateView):
    template_name = 'form/indexAdmin.html'

# Post Admin
class PostAdminListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'

class PostAdminCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('post_list_admin')

class PostAdminUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('post_list_admin')

class PostAdminDeleteView(DeleteView):
    model = Post
    template_name = 'myapp/post_confirm_delete.html'
    success_url = reverse_lazy('post_list_admin')

# Product Admin
class ProductAdminListView(ListView):
    model = Product
    template_name = 'myapp/product_list.html'

class ProductAdminCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('product_list_admin')

class ProductAdminUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('product_list_admin')

class ProductAdminDeleteView(DeleteView):
    model = Product
    template_name = 'myapp/product_confirm_delete.html'
    success_url = reverse_lazy('product_list_admin')

# About Admin
class AboutDetailAdminListView(ListView):
    model = AboutDetail
    template_name = 'myapp/about_list.html'

class AboutDetailAdminCreateView(CreateView):
    model = AboutDetail
    form_class = AboutDetailForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('about_list_admin')

class AboutDetailAdminUpdateView(UpdateView):
    model = AboutDetail
    form_class = AboutDetailForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('about_list_admin')

class AboutDetailAdminDeleteView(DeleteView):
    model = AboutDetail
    template_name = 'myapp/about_confirm_delete.html'
    success_url = reverse_lazy('about_list_admin')

class UserAdminListView(ListView):
    model = User
    template_name = 'myapp/user_list.html'

class UserAdminCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('user_list_admin')

class UserAdminUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('user_list_admin')

class UserAdminDeleteView(DeleteView):
    model = User
    template_name = 'myapp/user_confirm_delete.html'
    success_url = reverse_lazy('user_list_admin')
