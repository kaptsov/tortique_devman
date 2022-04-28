from django.db import models


class Customers(models.Model):

    phone_number = models.CharField(
        max_length=256,
        blank=True,
        default="",
        verbose_name="Номер телефона заказчика",
    )
    first_name = models.CharField(
        max_length=256,
        blank=True,
        default="",
        verbose_name="Имя заказчика",
    )
    last_name = models.CharField(
        max_length=256,
        blank=True,
        default="",
        verbose_name="Фамилия заказчика",
    )
    address = models.TextField(
        verbose_name="Адрес заказчика",
    )

    def __str__(self):
        return f"Заказчик {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"


class OrderStatuses(models.Model):

    PAID = 'PA'
    COOKING = 'CO'
    IN_DELIVERY = 'IND'
    DELIVERED = 'DE'
    RETURNED = 'RE'
    ORDER_STATUSES_CHOICES = [
        (PAID, 'Оплачен'),
        (COOKING, 'Готовится'),
        (IN_DELIVERY, 'В доставке'),
        (DELIVERED, 'Доставлен'),
        (RETURNED, 'Возврат'),
    ]

    status = models.CharField(
        max_length=256,
        choices=ORDER_STATUSES_CHOICES,
        blank=True,
        default="",
        verbose_name="Статус заказа",
    )

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Статус заказа"
        verbose_name_plural = "Статусы заказов"


class Levels(models.Model):

    NOT_CHOSEN = 'NC'
    ONE = 'ON'
    TWO = 'TW'
    THREE = 'TH'
    LEVEL_CHOICES = [
        (NOT_CHOSEN, 'Не выбрано'),
        (ONE, 'Один'),
        (TWO, 'Два'),
        (THREE, 'Три'),
    ]

    name = models.CharField(
        max_length=256,
        blank=True,
        default=NOT_CHOSEN,
        choices=LEVEL_CHOICES,
        verbose_name="Наимнование уровня",
    )

    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Цена уровня",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Количество уровней"
        verbose_name_plural = "Количество уровней"


class Forms(models.Model):

    NOT_CHOSEN = 'NC'
    CIRCLE = 'CI'
    SQUARE = 'SQ'
    RECTANGLE = 'RE'
    FORMS_CHOICES = [
        (NOT_CHOSEN, 'Не выбрано'),
        (CIRCLE, 'Круг'),
        (SQUARE, 'Квадрат'),
        (RECTANGLE, 'Прямоугольник'),
    ]
    name = models.CharField(
        max_length=256,
        blank=True,
        choices=FORMS_CHOICES,
        default=NOT_CHOSEN,
        verbose_name="Наимнование формы",
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Цена формы",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма"
        verbose_name_plural = "Формы"


class Topping(models.Model):

    NOT_CHOSEN = 'NC'
    WITHOUT = 'WO'
    WHITE_SOUCE = 'WS'
    CARAMEL = 'CA'
    MAPLE = 'MA'
    BILBERRY = 'BB'
    WHITE_CHOCOLATE = 'WC'
    STRAWBERRY = 'ST'
    TOPPING_CHOICES = [
        (NOT_CHOSEN, 'Не выбрано'),
        (WITHOUT, 'Без топпинга'),
        (WHITE_SOUCE, 'Белый соус'),
        (CARAMEL, 'Карамельный'),
        (MAPLE, 'Кленовый'),
        (BILBERRY, 'Черничный'),
        (WHITE_CHOCOLATE, 'Молочный шоколад'),
        (STRAWBERRY, 'Клубничный'),
    ]

    name = models.CharField(
        max_length=256,
        blank=True,
        default=NOT_CHOSEN,
        choices=TOPPING_CHOICES,
        verbose_name="Наимнование топпинга",
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Цена топпинга",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Топпинг"
        verbose_name_plural = "Топпинг"


class Berries(models.Model):

    NOT_CHOSEN = 'NC'
    WITHOUT = 'WO'
    RASPBERRY = 'RA'
    BLUEBERRY = 'BL'
    BlACKBERRY = 'BB'
    STRAWBERRY = 'ST'
    BERRY_CHOICES = [
        (NOT_CHOSEN, 'Не выбрано'),
        (WITHOUT, 'Без ягод'),
        (RASPBERRY, 'Малина'),
        (BLUEBERRY, 'Голубика'),
        (BlACKBERRY, 'Ежевика'),
        (STRAWBERRY, 'Клубника'),
    ]
    name = models.CharField(
        max_length=256,
        blank=True,
        default=NOT_CHOSEN,
        choices=BERRY_CHOICES,
        verbose_name="Название ягоды",
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Цена ягоды",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ягода"
        verbose_name_plural = "Ягоды"


class Decors(models.Model):

    NOT_CHOSEN = 'NC'
    WITHOUT = 'WO'
    PISTACHIO  = 'PI'
    MERINQUE = 'ME'
    PECAN = 'PE'
    MARSHMALLOW = 'MM'
    MARZIPAN = 'MC'
    DECOR_CHOICES = [
        (NOT_CHOSEN, 'Не выбрано'),
        (WITHOUT, 'Без декора'),
        (PISTACHIO, ' Фисташки'),
        (MERINQUE, 'Безе'),
        (PECAN, 'Пекан'),
        (MARSHMALLOW, 'Маршмеллоу'),
        (MARZIPAN, 'Марципан'),
    ]
    name = models.CharField(
        max_length=256,
        blank=True,
        default=NOT_CHOSEN,
        choices=DECOR_CHOICES,
        verbose_name="Наименование декора",
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Цена декора",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Декор"
        verbose_name_plural = "Декор"


class Orders(models.Model):

    customer = models.ForeignKey(
        Customers,
        related_name="customers",
        verbose_name="Заказчик",
        on_delete=models.PROTECT,
    )
    title = models.TextField(
        verbose_name="Надпись",
        blank=True
    )
    comment = models.TextField(
        verbose_name="Комментарий к заказу",
        blank=True
    )
    delivery_address = models.TextField(
        verbose_name="Адрес доставки",
        blank=True,
        null=True
    )
    delivery_date = models.DateField(
        verbose_name="Дата доставки",
        blank=True,
        null=True
    )
    delivery_time = models.DateTimeField(
        verbose_name="Время доставки",
        blank=True,
        null=True
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Стоимость заказа",
        blank=True,
        null=True
    )
    status = models.ForeignKey(
        OrderStatuses,
        related_name="statuses",
        verbose_name="Статус заказа",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        choices=OrderStatuses.ORDER_STATUSES_CHOICES
    )
    level = models.ForeignKey(
        Levels,
        verbose_name="Количество уровней",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        choices=Levels.LEVEL_CHOICES
    )
    form = models.ForeignKey(
        Forms,
        verbose_name="Форма",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        choices=Forms.FORMS_CHOICES
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name="Топпинг",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        choices=Topping.TOPPING_CHOICES
    )
    berries = models.ForeignKey(
        Berries,
        verbose_name="Ягоды",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        choices=Berries.BERRY_CHOICES
    )
    decor = models.ForeignKey(
        Decors,
        verbose_name="Декор",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        choices=Decors.DECOR_CHOICES
    )

    def __str__(self):
        return f"Заказ № {self.pk}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
