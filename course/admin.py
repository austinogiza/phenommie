from django.contrib import admin
from .models import Courses, SavedCourse, Reviews, Lessons, UserLibrary
# Register your models here.


class CoursesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class LessonsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Courses, CoursesAdmin)
admin.site.register(UserLibrary)
admin.site.register(SavedCourse)
admin.site.register(Lessons, LessonsAdmin)
admin.site.register(Reviews)
