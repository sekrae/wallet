from django.db import models


class Customer(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    fullname = models.CharField(max_length=100, verbose_name='ФИО', null=True, blank=True, help_text='Не обязательное поле')
    email = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def save(self, *args, **kwargs):
        if self.last_name:
            if self.patronymic:
                self.fullname = f'{self.last_name} {self.first_name} {self.patronymic}'
            else:
                self.fullname = f'{self.last_name} {self.first_name}'

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
