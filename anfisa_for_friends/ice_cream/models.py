from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название категории, не более 256 символов'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=64,
        unique=True,
        help_text='Уникальный слаг, не более 64 символов'
    )
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Topping(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название топпинга, не более 256 символов'
    )
    slug = models.SlugField(
        'Слаг',
        max_length=64,
        unique=True,
        help_text='Уникальный слаг, не более 64 символов'
    )

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self) -> str:
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название обёртки, не более 256 символов'
    )

    class Meta:
        verbose_name = 'Обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self) -> str:
        return self.title


class IceCream(PublishedModel):
    title = models.CharField(
        'Название',
        max_length=256,
        help_text='Уникальное название мороженого, не более 256 символов'
    )
    description = models.TextField(
        'Описание',
        help_text='Подробное описание мороженого'
    )
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        related_name='ice_cream',
        null=True,
        blank=True,
        verbose_name='Обертка'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ice_creams',
        verbose_name='Категория'
    )
    toppings = models.ManyToManyField(Topping, verbose_name='Топпинг')
    is_on_main = models.BooleanField('На главную', default=False)

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'

    def __str__(self) -> str:
        return self.title
