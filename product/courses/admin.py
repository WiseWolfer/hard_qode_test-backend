from django.contrib import admin
from .models import Course, Lesson
from users.models import Subscription, Balance


class CourseAdmin(admin.ModelAdmin):
    # отображение id и title в списке Действий в админ панели
    list_display = ('id', 'author', 'title', 'start_date', 'price')
    # ссылки на статью по id и title
    list_display_links = ('id', 'author', 'title', 'start_date', 'price')
    # поисковое поле по названию статьи и контенту
    search_fields = ('author', 'title', 'start_date')


class LessonAdmin(admin.ModelAdmin):
    # отображение id и title в списке Действий в админ панели
    list_display = ('id', 'title', 'course', 'link')
    # ссылки на статью по id и title
    list_display_links = ('id', 'title', 'course', 'link')
    # поисковое поле по названию статьи и контенту
    search_fields = ('course', 'title')


class SubscriptionAdmin(admin.ModelAdmin):
    # отображение id и title в списке Действий в админ панели
    list_display = ('id', 'name_of_subscription', 'Flag_subscripton')
    # ссылки на статью по id и title
    list_display_links = ('id', 'name_of_subscription', 'Flag_subscripton')
    # поисковое поле по названию статьи и контенту
    search_fields = ('name_of_subscription', 'Flag_subscripton')


class BalanceAdmin(admin.ModelAdmin):
    # отображение id и title в списке Действий в админ панели
    list_display = ('id', 'user', 'B_value')
    # ссылки на статью по id и title
    list_display_links = ('id', 'user', 'B_value')
    # поисковое поле по названию статьи и контенту
    search_fields = ('user', 'B_value')


# Register your models here.
admin.site.register(Course, CourseAdmin)

admin.site.register(Lesson, LessonAdmin)

admin.site.register(Subscription, SubscriptionAdmin)

admin.site.register(Balance, BalanceAdmin)

