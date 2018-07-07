from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=20)
    is_active = models.BooleanField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Post(models.Model):
    STATUS_DRAFT = 0
    STATUS_REJECTED = 100
    STATUS_TRASHED = 25
    STATUS_AUTHORIZED = 80
    STATUSES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_TRASHED, 'Trashed'),
        (STATUS_AUTHORIZED, 'Authorized'),
    )

    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_DRAFT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=255)
    # text = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

