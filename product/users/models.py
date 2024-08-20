from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Баланс пользователя')

    B_value = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=1000,
        verbose_name="Баланс пользователя")

    def save(self, *args, **kwargs):
        """Переопределение метода save для сохранения данных"""
        """Проверка Баланса при создании, если будет меньше 0, присвоится 1000
        Проверка пользователя через is_staff"""

        if self.B_value < 0:
            self.B_value = 0

        if AbstractUser.is_staff:
            super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс.
       Через полy Who_use  можно будет понять на какой курс подписан пользователь
       Если по нему записи не будет в этой таблице, то у него нет подписки
       Идея, что пользователь имеет подписку на один курс (один ко многим)
    """
    sub_choice = [(True, "ДА"), (False, "Нет")]

    id = models.AutoField(primary_key=True)
    name_of_subscription = models.CharField(max_length=250, verbose_name="Название подписки", unique=True)
    Who_use = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                                verbose_name='Кто подписан')

    Flag_subscripton = models.BooleanField(default=False, verbose_name="Есть подписка?", choices=sub_choice)

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)

