from django.contrib import admin
from .models import ContactEnquiry


@admin.register(ContactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'service', 'budget', 'status', 'created_at')
    list_filter = ('status', 'service', 'budget', 'created_at')
    search_fields = ('name', 'email', 'company', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
    ordering = ('-created_at',)
