# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

# Models
from .models import (
    Service, GalleryImage, Testimonial, BlogPost,
    BlogCategory, BlogTag, Comment, Like, Subscription, FAQ
)

# Forms
from .forms import (
    ContactForm, TestimonialForm, CommentForm, SubscriptionForm, BlogPostForm
)

# Helper (optional)
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

# --- BASIC PAGES ---
def home(request):
    testimonials = Testimonial.objects.filter(approved=True).order_by('-submitted_at')[:3]
    return render(request, 'home.html', {'testimonials': testimonials})

def about(request):
    return render(request, 'about.html')

def services(request):
    service_list = Service.objects.all().order_by('-created_at')
    return render(request, 'services.html', {'services': service_list})

def gallery(request):
    images = GalleryImage.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'images': images})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Your message has been sent successfully."))
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def testimonials_view(request):
    testimonials = Testimonial.objects.filter(approved=True).order_by('-submitted_at')
    form = TestimonialForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, _("Thank you! Your feedback has been received and is awaiting approval."))
        return redirect('testimonials')
    return render(request, 'testimonials.html', {
        'testimonials': testimonials,
        'form': form
    })

# --- BLOG LIST / SEARCH / FILTER / PAGINATION ---
def blog_list(request):
    category_slug = request.GET.get('category')
    tag_slug = request.GET.get('tag')
    search_query = request.GET.get('q')

    posts = BlogPost.objects.filter(published=True)

    if category_slug:
        posts = posts.filter(category__name__iexact=category_slug)
    if tag_slug:
        posts = posts.filter(tags__name__iexact=tag_slug)
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    paginator = Paginator(posts.order_by('-created_at'), 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = BlogCategory.objects.all()
    tags = BlogTag.objects.all()
    subscription_form = SubscriptionForm()

    return render(request, 'blog/blog.html', {
        'page_obj': page_obj,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'active_category': category_slug,
        'active_tag': tag_slug,
        'subscription_form': subscription_form,
    })

# --- BLOG DETAIL ---
def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = post.comments.filter(approved=True, parent__isnull=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            parent_id = form.cleaned_data.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)
            comment.save()
            return JsonResponse({
                'success': True,
                'comment': {
                    'id': comment.id,
                    'name': comment.name,
                    'created_at': comment.created_at.strftime('%b %d, %Y'),
                    'comment': comment.comment,
                    'parent_id': comment.parent.id if comment.parent else None
                }
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = CommentForm()

    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'form': form})

# --- BLOG LIKE ---
def blog_like(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    session_id = request.session.session_key or request.session.save()
    like = Like.objects.filter(post=post, session_id=session_id)

    if like.exists():
        like.delete()
    else:
        Like.objects.create(post=post, session_id=session_id)

    return redirect('blog_detail', pk=pk)

# --- BLOG CREATE ---
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.published = True
            form.save()
            messages.success(request, "Blog post created.")
            return redirect('blog')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_create.html', {'form': form})

# --- SUBSCRIBE NEWSLETTER ---
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed successfully!")
        else:
            messages.error(request, "Subscription failed.")
    return redirect('blog')


# --- FAQS ---

def faqs_view(request):
    faqs = FAQ.objects.all().order_by('id')
    return render(request, 'faqs.html', {'faqs': faqs})

# --- PRIVACY POLICY ---

def privacy_policy(request):
    return render(request, 'privacy.html')

# --- TERMS AND CONDITIONS ---

def terms_conditions(request):
    return render(request, 'terms.html')



