from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# --- SERVICES ---
class Service(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"))
    icon = models.CharField(_("Icon"), max_length=100, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.title


# --- GALLERY ---
class GalleryImage(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_("Description"), blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to='gallery/')
    uploaded_at = models.DateTimeField(_("Uploaded At"), auto_now_add=True)

    def __str__(self):
        return self.title


# --- CONTACT ---
class ContactMessage(models.Model):
    full_name = models.CharField(_("Full Name"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    email = models.EmailField(_("Email"))
    message = models.TextField(_("Message"))
    submitted_at = models.DateTimeField(_("Submitted At"), auto_now_add=True)
    is_read = models.BooleanField(_("Is Read"), default=False)

    def __str__(self):
        return f"{self.full_name} - {self.email}"


# --- TESTIMONIALS ---
class Testimonial(models.Model):
    client_name = models.CharField(_("Client Name"), max_length=100)
    role = models.CharField(_("Role"), max_length=100, blank=True, null=True)
    message = models.TextField(_("Message"))
    submitted_at = models.DateTimeField(_("Submitted At"), auto_now_add=True)
    approved = models.BooleanField(_("Approved"), default=False)

    def __str__(self):
        return f"{self.client_name} - {self.message[:30]}"


# --- BLOG CATEGORY ---
class BlogCategory(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)

    def __str__(self):
        return self.name


# --- BLOG TAG ---
class BlogTag(models.Model):
    name = models.CharField(_("Tag Name"), max_length=50, unique=True)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)

    def __str__(self):
        return self.name


# --- BLOG POST ---
class BlogPost(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True, blank=True)
    excerpt = models.TextField(_("Excerpt"), blank=True, null=True)
    content = models.TextField(_("Content"))
    image = models.ImageField(_("Featured Image"), upload_to='blog/', blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)
    author = models.CharField(_("Author"), max_length=100, default='Admin')
    published = models.BooleanField(_("Published"), default=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(BlogTag, blank=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


# --- BLOG COMMENTS ---
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"))
    comment = models.TextField(_("Comment"))
    created_at = models.DateTimeField(_("Created At"), default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} on {self.post.title}"


# --- BLOG LIKES ---
class Like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='post_likes')
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} liked {self.post.title}"


# --- NEWSLETTER SUBSCRIPTIONS ---
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

# --- FAQS ---

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

