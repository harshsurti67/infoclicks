from django.db import models


class ContactEnquiry(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Qualified', 'Qualified'),
        ('Closed', 'Closed'),
    ]

    name = models.CharField(max_length=200, help_text="Client full name")
    email = models.EmailField(max_length=255, help_text="Contact email address")
    phone = models.CharField(max_length=50, blank=True, default="", help_text="Contact phone number")
    company = models.CharField(max_length=200, blank=True, default="", help_text="Company or business name")
    service = models.CharField(max_length=100, blank=True, default="Web Application", help_text="Service of interest")
    budget = models.CharField(max_length=100, blank=True, default="₹50,000 – ₹1,00,000", help_text="Budget range")
    message = models.TextField(help_text="Project requirements or message")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Enquiry'
        verbose_name_plural = 'Contact Enquiries'

    def __str__(self):
        return f"{self.name} - {self.company or self.email} ({self.created_at.strftime('%Y-%m-%d')})"
