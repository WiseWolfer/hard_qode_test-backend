from django.contrib.auth import get_user_model
from django.db.models import Avg, Count
from rest_framework import serializers

from courses.models import Course, Group, Lesson


User = get_user_model()


class LessonSerializer(serializers.ModelSerializer):
    """Список уроков."""

    course = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Lesson
        fields = (
            'title',
            'link',
            'course'
        )


class CreateLessonSerializer(serializers.ModelSerializer):
    """Создание уроков."""

    class Meta:
        model = Lesson
        fields = (
            'title',
            'link',
            'course'
        )


class StudentSerializer(serializers.ModelSerializer):
    """Студенты курса."""

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )


class GroupSerializer(serializers.ModelSerializer):
    """Список групп."""

    # TODO Доп. задание

    class Meta:
        model = Group
        fields = ('__all__')  # Уточнить поля


class CreateGroupSerializer(serializers.ModelSerializer):
    """Создание групп."""

    class Meta:
        model = Group
        fields = (
            'title',
            'course',
        )


class MiniLessonSerializer(serializers.ModelSerializer):
    """Список названий уроков для списка курсов."""

    class Meta:
        model = Lesson
        fields = (
            'title',
        )



class CourseSerializer(serializers.ModelSerializer):
    """Список курсов."""

    lessons = MiniLessonSerializer(many=True, read_only=True)
    lessons_count = serializers.SerializerMethodField(read_only=True)
    students_count = serializers.SerializerMethodField(read_only=True)
    groups_filled_percent = serializers.SerializerMethodField(read_only=True)
    demand_course_percent = serializers.SerializerMethodField(read_only=True)

    def get_lessons_count(self, obj):
        """Количество уроков в курсе."""
        return Lesson.objects.filter(course__title=obj).count()

        # TODO Доп. задание

    def get_students_count(self, obj):
        """Общее количество студентов на курсе."""
        # return Course.objects.filter(What_a_sub__Who_use__email=obj.title).count()
        # TODO Доп. задание

    def get_groups_filled_percent(self, obj):
        """Процент заполнения групп, если в группе максимум 30 чел.."""
        # TODO Доп. задание

    def get_demand_course_percent(self, obj):
        """Процент приобретения курса."""
        # TODO Доп. задание


    class Meta:
        model = Course
        fields = (
            'id',
            'author',
            'title',
            'start_date',
            'price',
            'courses_in_stock',
            'lessons_count',
            'lessons',
            'demand_course_percent',
            'students_count',
            'groups_filled_percent',
        )


class CreateCourseSerializer(serializers.ModelSerializer):
    """Создание курсов."""

    class Meta:
        model = Course
        fields = ('id',
                  'author',
                  'title',
                  'start_date',
                  'price',
                  'courses_in_stock')  # Уточнить поля
