# Register your models here.

from django.contrib import admin
from .models import Subject, Course, Module, Text, Content


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


# class TextInline(admin.StackedInline):
#     model = Text

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title']
    # inlines = [TextInline]
    



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['content_type']