from django.contrib import admin

from .models import Question , Choice

# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["question_text","pub_date"]

    
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["question","choice_text","votes"]
