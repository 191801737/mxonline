from django.contrib import admin

# Register your models here.

from .models import UserProfile, Banner


class UserProfileAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Banner, BannerAdmin)


