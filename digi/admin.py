from django.contrib import admin

from .models import Contact, CustomUser, Portfolio, PortfolioCategory, Services


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PortfolioCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', ]


admin.site.register(Contact)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Services, ServiceAdmin)

admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
