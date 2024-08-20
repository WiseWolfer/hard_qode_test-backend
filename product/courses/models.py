from django.db import models


class Course(models.Model):
    """Модель продукта - курса.
       Добавил уникальность названию курса и id записи
       What_a_Course - внешний ключ с таблицей Subscriptions
    """

    id = models.AutoField(primary_key=True)

    author = models.CharField(
        max_length=250,
        verbose_name='Автор',
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
        unique=True
    )
    start_date = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name='Дата и время начала курса'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена',
        default=0
    )
    courses_in_stock = models.IntegerField(verbose_name="Количество курсов в наличии")

    What_a_sub = models.ForeignKey('users.Subscription',
                                   on_delete=models.CASCADE,
                                   null=True,
                                   verbose_name='Какая подписка')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ('-id',)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    """Модель урока.
       Добавил уникальность названию урока и id записи
    """

    id = models.AutoField(primary_key=True)

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Курс',
        null=True,
    )
    title = models.CharField(
        max_length=250,
        verbose_name='Название',
        unique=True
    )
    link = models.URLField(
        max_length=250,
        verbose_name='Ссылка',
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Group(models.Model):
    """Модель группы."""

    title = models.CharField(
        max_length=250,
        blank=False,
        verbose_name='Название группы'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Курс',
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('-id',)
