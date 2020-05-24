from django.contrib import admin

from .models import Question , Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text","pub_date"]
    inlines = [ChoiceInline]


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["question","choice_text","votes"]
