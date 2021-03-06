# Generated by Django 4.0.4 on 2022-04-26 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakecake', '0002_alter_orderstatuses_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berries',
            name='name',
            field=models.CharField(blank=True, choices=[('NC', 'Не выбрано'), ('WO', 'Без ягод'), ('RA', 'Малина'), ('BL', 'Голубика'), ('BB', 'Ежевика'), ('ST', 'Клубника')], default='NC', max_length=256, verbose_name='Название ягоды'),
        ),
        migrations.AlterField(
            model_name='decors',
            name='name',
            field=models.CharField(blank=True, choices=[('NC', 'Не выбрано'), ('WO', 'Без декора'), ('PI', ' Фисташки'), ('ME', 'Безе'), ('PE', 'Пекан'), ('MM', 'Маршмеллоу'), ('MC', 'Марципан')], default='NC', max_length=256, verbose_name='Наименование декора'),
        ),
        migrations.AlterField(
            model_name='forms',
            name='name',
            field=models.CharField(blank=True, choices=[('NC', 'Не выбрано'), ('CI', 'Круг'), ('SQ', 'Квадрат'), ('RE', 'Прямоугольник')], default='NC', max_length=256, verbose_name='Наимнование формы'),
        ),
        migrations.AlterField(
            model_name='levels',
            name='name',
            field=models.CharField(blank=True, choices=[('NC', 'Не выбрано'), ('ON', 'Один'), ('TW', 'Два'), ('TH', 'Три')], default='NC', max_length=256, verbose_name='Наимнование уровня'),
        ),
        migrations.AlterField(
            model_name='orderstatuses',
            name='status',
            field=models.CharField(blank=True, choices=[('PA', 'Оплачен'), ('CO', 'Готовится'), ('IND', 'В доставке'), ('DE', 'Доставлен'), ('RE', 'Возврат')], default='', max_length=256, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(blank=True, choices=[('NC', 'Не выбрано'), ('WO', 'Без топпинга'), ('WS', 'Белый соус'), ('CA', 'Карамельный'), ('MA', 'Кленовый'), ('BB', 'Черничный'), ('WC', 'Молочный шоколад'), ('ST', 'Клубничный')], default='NC', max_length=256, verbose_name='Наимнование топпинга'),
        ),
    ]
