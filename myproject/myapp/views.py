from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Product, AboutDetail, Category, Cart, Wishlist
from .forms import PostForm, ProductForm, AboutDetailForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.all().order_by('-created_at')[:3] 
    products = Product.objects.all().order_by('-created_at')[:5]
    return render(request, 'index.html', {'posts': posts, 'products': products})

def contact(request):
    return render(request, 'contact.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})

def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    featured_products = Product.objects.order_by('?')[:5]
    return render(request, 'product_list.html', {
        'products': products,
        'categories': categories,
        'featured_products': featured_products
    })

def product_list_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category).order_by('-created_at')
    categories = Category.objects.all()
    featured_products = Product.objects.order_by('?')[:5]
    return render(request, 'product_list.html', {
        'products': products,
        'category': category,
        'categories': categories,
        'featured_products': featured_products
    })

def about(request):
    about_details = AboutDetail.objects.all()
    return render(request, 'about.html', {'about_details': about_details})

def about_detail(request, slug):
    about_detail = get_object_or_404(AboutDetail, slug=slug)
    return render(request, 'about_detail.html', {'about_detail': about_detail})

from django.contrib import messages

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"Added {product.name} to your cart.")
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f"Added {product.name} to your wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = get_object_or_404(Wishlist, user=request.user, product=product)
    wishlist_item.delete()
    messages.success(request, f"Removed {product.name} from your wishlist.")
    return redirect('view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(Cart, user=request.user, product=product)
    cart_item.delete()
    messages.success(request, f"Removed {product.name} from your cart.")
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.get_total() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def profile(request):
    return render(request, 'account/profile.html')



# Admin Dashboard
def admin_dashboard_index(request):
    return render(request, 'form/indexAdmin.html')

# Post Admin
class PostListView(ListView):
    model = Post
    template_name = 'myapp/post_list.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('post_list_admin')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('post_list_admin')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'myapp/post_confirm_delete.html'
    success_url = reverse_lazy('post_list_admin')

# Product Admin
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/product_list.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('product_list_admin')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('product_list_admin')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'myapp/product_confirm_delete.html'
    success_url = reverse_lazy('product_list_admin')

# About Admin
class AboutDetailListView(ListView):
    model = AboutDetail
    template_name = 'myapp/about_list.html'

class AboutDetailCreateView(CreateView):
    model = AboutDetail
    form_class = AboutDetailForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('about_list_admin')

class AboutDetailUpdateView(UpdateView):
    model = AboutDetail
    form_class = AboutDetailForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('about_list_admin')

class AboutDetailDeleteView(DeleteView):
    model = AboutDetail
    template_name = 'myapp/about_confirm_delete.html'
    success_url = reverse_lazy('about_list_admin')
class UserListView(ListView):
    model = User
    template_name = 'myapp/user_list.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('user_list_admin')

class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('user_list_admin')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'myapp/user_confirm_delete.html'
    success_url = reverse_lazy('user_list_admin')