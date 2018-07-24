from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField



class CompaniesLoans(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    min_days = models.IntegerField()
    max_days = models.IntegerField()
    first_free = models.BooleanField()
    amount_first_free = models.IntegerField()
    installment_loan = models.BooleanField()
    installment_min_amount = models.IntegerField()
    installment_max_amount = models.IntegerField()
    installment_min_days = models.IntegerField()
    installment_max_days = models.IntegerField()
    miscs = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class CompaniesCredit(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    min_days = models.IntegerField()
    max_days = models.IntegerField()
    miscs = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255, null=False)
    published_date = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    description = RichTextField(null=False)
    body = models.TextField(null=False)
    meta_title = models.CharField(max_length=158, null=False)
    meta_description = models.CharField(max_length=320, null=False)
    slug = models.SlugField(default='', null=False)

    def validate_title(self):
        title_exists = Post.objects.filter(title=self.title).exists()

        if title_exists:
            raise ValidationError('Title already exists ! ')


    def save(self):
        self.slug = slugify(self.title)
        self.validate_title()
        super(Post, self).save()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
