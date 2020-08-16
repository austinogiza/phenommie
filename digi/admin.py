from django.contrib import admin

from .models import Contact, CustomUser, Portfolio, PortfolioCategory


# Register your models here.


class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class PortfolioCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', ]


admin.site.register(Contact)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Portfolio, PortfolioAdmin)

admin.site.register(PortfolioCategory, PortfolioCategoryAdmin)
