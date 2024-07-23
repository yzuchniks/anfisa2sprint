from django.db import models

from core.models import PublishedModel


class Category(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.title


class Topping(PublishedModel):
    title = models.CharField('Название', max_length=256)
    slug = models.SlugField('Слаг', max_length=64, unique=True)

    class Meta:
        verbose_name = 'Топпинг'
        verbose_name_plural = 'Топпинги'

    def __str__(self) -> str:
        return self.title


class Wrapper(PublishedModel):
    title = models.CharField('Название', max_length=256)

    class Meta:
        verbose_name = 'Обертка'
        verbose_name_plural = 'Обертки'

    def __str__(self) -> str:
        return self.title


class IceCream(PublishedModel):
    title = models.CharField('Название', max_length=256)
    description = models.TextField('Описание')
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
