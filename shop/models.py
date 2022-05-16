from django.db import models
import uuid
import os
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from pytils.translit import slugify
from django.utils.html import format_html
from django.utils.functional import cached_property
from django_resized import ResizedImageField
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys
import string
import random


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    if ext == 'png' or ext == 'jpg' or ext == 'jpeg' or ext == 'svg':
        dir = 'images/'
    else:
        dir = 'files/'
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join(dir, filename)


def resize_img(f1, f2, fs):
    f1 = f2
    image1 = f1
    img1 = Image.open(image1)
    new_img1 = img1.convert('RGB')
    img_width = new_img1.size[0]
    img_height = new_img1.size[1]
    img_ratio = img_width / img_height
    size_ratio = fs[0] / fs[1]
    if img_ratio < size_ratio:
        resized_new_img1 = new_img1.resize((fs[0], int(fs[0] * img_height / img_width)), Image.ANTIALIAS)
        box = (
            0, (resized_new_img1.size[1] - fs[1]) / 2, resized_new_img1.size[0], (resized_new_img1.size[1] + fs[1]) / 2)
        resized_new_img1 = resized_new_img1.crop(box)
    elif img_ratio > size_ratio:
        resized_new_img1 = new_img1.resize((int(fs[1] * img_width / img_height), img_height), Image.ANTIALIAS)
        box = (
            (resized_new_img1.size[0] - fs[0]) / 2, 0, (resized_new_img1.size[0] + fs[0]) / 2, resized_new_img1.size[1])
        resized_new_img1 = resized_new_img1.crop(box)
    else:
        resized_new_img1 = new_img1.resize((fs[0], fs[1]), Image.ANTIALIAS)
    filestream1 = BytesIO()
    resized_new_img1.save(filestream1, 'JPEG', quality=80)
    filestream1.seek(0)
    name1 = f"{f1.name}"
    return InMemoryUploadedFile(
        filestream1, 'ImageField', name1, 'jpeg/image',
        sys.getsizeof(filestream1), None
    )


class category(models.Model):
    order = models.IntegerField('Порядок показа')
    title = models.CharField('Заголовок', max_length=500)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную',
                            unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        else:
            self.slug = slugify(self.slug)[:50]
        super().save(*args, **kwargs)


class subcategory(models.Model):
    order = models.IntegerField('Порядок показа')
    category = models.ForeignKey(category, on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField('Заголовок', max_length=500)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            help_text='URL генерируется автоматически из названия раздела, но может быть задан вручную',
                            unique=True)

    def __str__(self):
        return str(self.category) + ' — ' + self.title

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:50]
        else:
            self.slug = slugify(self.slug)[:50]
        super().save(*args, **kwargs)


class item(models.Model):
    title = models.CharField('Заголовок', max_length=500)
    slug = models.SlugField('URL', max_length=50, allow_unicode=True, blank=True,
                            unique=True)
    price = models.IntegerField(null=True)

    order = models.IntegerField('Порядок показа')
    is_active = models.BooleanField('Показывать на сайте', default=True)
    description = models.TextField('Описание', blank=True)
    category = models.ForeignKey(subcategory, on_delete=models.CASCADE, verbose_name='Категория')
    main_photo_xxl2 = ResizedImageField('Основное изображение',
                                        upload_to=get_file_path, quality=80,
                                        help_text='Формат файла: jpg, jpeg или png. Ограничение размера: 3 Мбайт.')

    __original_main_photo_xxl2 = None

    def __init__(self, *args, **kwargs):
        super(item, self).__init__(*args, **kwargs)
        self.__original_main_photo_xxl2 = self.main_photo_xxl2

    def __str__(self):
        return str(self.category) + ': ' + str(self.title)

    def get_absolute_url(self):
        return f'/{self.category.category.slug}/{self.category.slug}/{self.slug}'

    class Meta:
        ordering = ['order']


class discount(models.Model):
    pass


class coupon(models.Model):
    pass


class item_basket(models.Model):
    pass
