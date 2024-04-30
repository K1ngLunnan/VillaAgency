from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=123
    )
    def __str__(self):
        return self.title


class House(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=299
    )
    slug = models.SlugField(unique=True)
    region = models.CharField(
        max_length=123
    )
    post_code = models.CharField(
        max_length=55
    )
    image = models.ImageField(
        upload_to='media/villa'
    )
    area = models.CharField(
        max_length=17
    )
    floor = models.PositiveSmallIntegerField()
    bedroom = models.PositiveSmallIntegerField()
    bathroom = models.PositiveSmallIntegerField()
    parking_lot = models.PositiveSmallIntegerField()
    description = models.TextField()
    is_security = models.BooleanField(
        default=False
    )
    authorization_type = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Красная книга'),
            (2, 'Зеленая книга'),
            (3, 'Белая книга'),
            (4, 'Для аренды'),
        )
    )
    payment_method = models.ForeignKey(
        'PaymentMethod'
        , on_delete=models.CASCADE
    )
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.address}, {self.region}, {self.post_code}"

class PaymentMethod(models.Model):
    title = models.CharField(
        max_length=123
    )
    def __str__(self):
        return self.title

