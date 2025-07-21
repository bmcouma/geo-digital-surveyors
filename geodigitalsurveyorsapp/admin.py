from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import (
    Service, GalleryImage, ContactMessage, Testimonial, 
    BlogPost, BlogCategory, BlogTag, Comment, Like, Subscription, FAQ
)

# Customize admin site headers
admin.site.site_header = "Geo Digital Surveyors Admin"
admin.site.site_title = "Geo Digital Surveyors Portal"
admin.site.index_title = "Welcome to Geo Digital Surveyors Admin Panel"


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title', 'description')
    list_filter = ('uploaded_at',)
    readonly_fields = ('uploaded_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'is_read', 'submitted_at')
    readonly_fields = ('full_name', 'email', 'phone', 'message', 'submitted_at')
    search_fields = ('full_name', 'email')
    list_filter = ('is_read', 'submitted_at')
    list_editable = ('is_read',)
    actions = ['export_as_csv', 'mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
        self.message_user(request, f"{queryset.count()} messages marked as read.")
    mark_as_read.short_description = "Mark selected messages as read"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=contact_messages.csv'
        writer = csv.writer(response)
        writer.writerow(['Full Name', 'Phone', 'Email', 'Message', 'Is Read', 'Submitted At'])
        for msg in queryset:
            writer.writerow([msg.full_name, msg.phone, msg.email, msg.message, msg.is_read, msg.submitted_at])
        return response
    export_as_csv.short_description = "Export selected messages to CSV"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'role', 'approved', 'submitted_at')
    list_filter = ('approved', 'submitted_at')
    search_fields = ('client_name', 'role', 'message')
    list_editable = ('approved',)
    readonly_fields = ('submitted_at',)
    actions = ['approve_testimonials', 'export_as_csv']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} testimonials approved.")
    approve_testimonials.short_description = "Approve selected testimonials"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=testimonials.csv'
        writer = csv.writer(response)
        writer.writerow(['Client Name', 'Role', 'Message', 'Submitted At', 'Approved'])
        for t in queryset:
            writer.writerow([t.client_name, t.role, t.message, t.submitted_at, t.approved])
        return response
    export_as_csv.short_description = "Export selected testimonials to CSV"


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at',)


@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'published', 'likes', 'views', 'created_at')
    list_filter = ('published', 'category', 'tags', 'created_at')
    search_fields = ('title', 'content', 'author')
    list_editable = ('published',)
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    readonly_fields = ('likes', 'views', 'created_at', 'updated_at')
    actions = ['publish_posts', 'unpublish_posts', 'export_as_csv']

    def publish_posts(self, request, queryset):
        queryset.update(published=True)
        self.message_user(request, f"{queryset.count()} posts published.")
    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
        self.message_user(request, f"{queryset.count()} posts unpublished.")
    unpublish_posts.short_description = "Unpublish selected posts"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=blog_posts.csv'
        writer = csv.writer(response)
        writer.writerow(['Title', 'Author', 'Category', 'Published', 'Likes', 'Views', 'Created At'])
        for post in queryset:
            writer.writerow([
                post.title, 
                post.author, 
                post.category.name if post.category else '', 
                post.published, 
                post.likes, 
                post.views, 
                post.created_at
            ])
        return response
    export_as_csv.short_description = "Export selected posts to CSV"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at', 'approved', 'parent')  # Shows parent for replies
    search_fields = ('name', 'email', 'comment')
    list_filter = ('approved', 'created_at')
    list_editable = ('approved',)
    readonly_fields = ('created_at',)
    actions = ['approve_comments', 'export_as_csv']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
        self.message_user(request, f"{queryset.count()} comments approved.")
    approve_comments.short_description = "Approve selected comments"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=comments.csv'
        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Post', 'Comment', 'Approved', 'Created At', 'Parent'])
        for comment in queryset:
            writer.writerow([
                comment.name, 
                comment.email, 
                comment.post.title, 
                comment.comment, 
                comment.approved, 
                comment.created_at,
                comment.parent.id if comment.parent else ''
            ])
        return response
    export_as_csv.short_description = "Export selected comments to CSV"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'ip_address', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('post__title', 'ip_address')
    readonly_fields = ('post', 'ip_address', 'created_at')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=likes.csv'
        writer = csv.writer(response)
        writer.writerow(['Post Title', 'IP Address', 'Created At'])
        for like in queryset:
            writer.writerow([like.post.title, like.ip_address, like.created_at])
        return response
    export_as_csv.short_description = "Export selected likes to CSV"


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('email',)
    list_editable = ('is_active',)
    readonly_fields = ('created_at',)
    actions = ['activate_subscriptions', 'deactivate_subscriptions', 'export_as_csv']

    def activate_subscriptions(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} subscriptions activated.")
    activate_subscriptions.short_description = "Activate selected subscriptions"

    def deactivate_subscriptions(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} subscriptions deactivated.")
    deactivate_subscriptions.short_description = "Deactivate selected subscriptions"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=subscriptions.csv'
        writer = csv.writer(response)
        writer.writerow(['Email', 'Is Active', 'Created At'])
        for sub in queryset:
            writer.writerow([sub.email, sub.is_active, sub.created_at])
        return response
    export_as_csv.short_description = "Export selected subscriptions to CSV"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')

