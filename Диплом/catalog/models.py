from django.db import models
import uuid
from datetime import datetime
import cyrtranslit
from django.utils.safestring import mark_safe  
import os
#from modelTest import settings
from django.db.models.signals import *
from django.dispatch.dispatcher import receiver
from tinymce import HTMLField
from django.utils.translation  import get_language, gettext as _
from changes.models import *
from django.conf import settings

class CharacteristicName(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic_ru = models.CharField(max_length=100, null=True, verbose_name=_('Наименование'))
    characteristic_ua = models.CharField(max_length=100, null=True, verbose_name=_('Наименование'))

    class Meta:
        verbose_name=_('Наименование характеристики')
        verbose_name_plural=_('Наименования характеристик')

    def __str__(self):
        return self.characteristic

    def as_json(self):
        return {
            "characteristic_ru": self.characteristic_ru,
            "characteristic_ua": self.characteristic_ua
        }

class Brand(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brandName_ru = models.CharField(max_length=100, null=True, verbose_name=_('Наименование производителя'))
    brandName_ua = models.CharField(max_length=100, null=True, verbose_name=_('Наименование производителя'))

    class Meta:
        verbose_name=_('Производитель')
        verbose_name_plural=_('Производители')

    def __str__(self):
        return self.brandName_ru + "  " + self.brandName_ua

    def as_json(self):
        return {
            "uuid": self.uuid,
            "brandName_ru": self.brandName_ru,
            "brandName_ua": self.brandName_ua
        }


@receiver(post_save, sender=Brand)
@receiver(post_delete, sender=Brand)
def Brand_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(brands=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.brands=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

class Product(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    alias = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=False, verbose_name=_('Наименование товара/услуги по-русски'))
    name_uk = models.CharField(max_length=128, blank=False, verbose_name=_('Наименование товара/услуги по-украински'), null=True)
    price = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=_('Цена'))
    brand = models.ForeignKey('Brand', on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('Производитель'))
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Категория'))
    meta_keywords = models.TextField(blank=True, null=True, verbose_name=_('Ключевые слова страницы товара/услуги (meta keywords)'))
    meta_description = models.TextField(blank=True, null=True, verbose_name=_('Meta-теги страницы продукта'))
    full_description = HTMLField(blank=True, verbose_name=_('Полное описание по-русски'))
    full_description_uk = HTMLField(blank=True, verbose_name=_('Полное описание по-украински'))
    main_image = models.ForeignKey('Mediafile', blank=True, null=True, on_delete=models.SET_NULL, verbose_name=_('Основное изображение'), related_name='Mediafile')

    class Meta:
        verbose_name=_('Товар/услуга')
        verbose_name_plural=_('Товары/услуги')

    def __str__(self):
        return self.name

    def as_json(self):
        result = {
            "uuid": self.uuid,
            "alias": self.alias,
            "name_ru": self.name,
            "name_ua": self.name_uk,
            "price": self.price,
            "brand": self.brand,
            "category": self.category.uuid,
            "category_alias": self.category.alias,
            "meta_keywords": self.meta_keywords,
            "meta_description": self.meta_description,
            "full_description_ru": self.full_description,
            "full_description_ua": self.full_description_uk,
            "main_image": None,
            "images": [],
            "characteristics": {},
            "comments_field": [],
        }
        if self.brand:
            result["brand"] = self.brand.as_json()
        if self.main_image:
           result["main_image"] = self.main_image.as_json()
        images = Mediafile.objects.filter(product=self)
        if len(images) > 0:
            result["images"] = [image.as_json() for image in images]
#        comments = Comments.objects.select_related('product')
#filter(product=self)
#        if len(comments) > 0:
#            result["comments_field"] = CommentsSerializer(comments, many=True).data
#        characteristics = Characteristic.objects.select_related('product')
#filter(product=self)
#        if len(characteristics) > 0:
#            for characteristic in characteristics:
#                result['characteristics'][str(characteristic.uuid)] = characteristic.data_ru
        return result

@receiver(pre_save, sender=Product)
def product_save(sender, instance, **kwargs):
    instance.alias=cyrtranslit.to_latin(instance.name, 'ru').replace(" ","_")

@receiver(post_save, sender=Product)
@receiver(post_delete, sender=Product)
def Product_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(products=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.products=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

class Characteristic(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(CharacteristicName, blank=False, on_delete=models.CASCADE, null=True, related_name='ncategoryName', verbose_name=_('Характеристика'))
    product = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE, verbose_name=_('Товар/услуга'), related_name="product_characteristics")
    data_ru = models.CharField(max_length=100, verbose_name=_('Значение по-русски'), null=True)
    data_ua = models.CharField(max_length=100,verbose_name=_('Значение по-украински'), null=True)
    class Meta:
        verbose_name=_('Характеристика')
        verbose_name_plural=_('Характеристики')

    def __str__(self):
        return self.name.characteristic

    def as_json(self, language=None):
        names = self.name.as_json()
        data = {
            "data_ru": self.data_ru,
            "data_ua": self.data_ua,
        }
        if language is not None:
            if "characteristic_"+language in names:
                return {
                    names["characteristic_"+language]: data["data_"+language],
                }
            else:
                result = {}
        else:
            result = {}
            result.update(names)
            result.update(data)
        result["product"] = self.product.uuid
        return result

@receiver(post_save, sender=Characteristic)
@receiver(post_delete, sender=Characteristic)
def Characteristic_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(products=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.products=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

class Comments(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment = models.TextField()
    product = models.ForeignKey(Product, default=None, related_name='comment', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    raiting = models.SmallIntegerField()
    user = models.CharField(default='temp', max_length=20)

@receiver(post_save, sender=Comments)
@receiver(post_delete, sender=Comments)
def Comments_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(comments=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.comments=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

def get_image_filename(instance, filename):
    product = cyrtranslit.to_latin(instance.product.name, 'ru').lower().replace(" ","_")
    category = cyrtranslit.to_latin(instance.product.category.name, 'ru').lower().replace(" ","_")
    return f"{category}/{product}/{filename}"

class Mediafile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, default='image', verbose_name=_('Название'))
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE, verbose_name=_('Товар/услуга'))
    file = models.ImageField(upload_to=get_image_filename, verbose_name=_('Загрузить изображение'))
    class Meta:
        verbose_name=_('Multimedia file')
        verbose_name_plural=_('Multimedia files')

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = _('Изображение')

    def __str__(self):
        return self.name

    def as_json(self):
        return dict(
            uuid=self.uuid,
            name=self.name,
            url=self.file.url)

@receiver(post_save, sender=Mediafile)
@receiver(post_delete, sender=Mediafile)
def Mediafile_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(mediafiles=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.mediafiles=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

def get_category_image_filename(instance, filename):
    category = cyrtranslit.to_latin(instance.name, 'ru').lower().replace(" ","_")
    return f"categories/{category}/{filename}"

class Category(models.Model):
    class Meta:
        verbose_name= _('Категория')
        verbose_name_plural = _('Категории')

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128, blank=False, verbose_name=_('Наименование по-русски'))
    name_uk = models.CharField(max_length=128, blank=False,  verbose_name=_('Наименование по-украински'), null=True)
    meta_keywords = models.TextField(blank=True, null=True, verbose_name=_('Ключевые слова страницы товара (meta keywords)'))
    meta_description = models.TextField(blank=True, null=True, verbose_name=_('Meta-теги страницы категории'))
    full_description = HTMLField(blank = True, null=True, verbose_name=_('Полное описание по-русски'))
    full_description_uk = HTMLField(blank = True, null=True, verbose_name=_('Полное описание по-украински'))
    alias = models.CharField(max_length=128, blank=True, null=True)
    children = models.ManyToManyField('Category', blank=True, verbose_name='Подкатегории')
    image = models.ImageField(upload_to=get_category_image_filename,
                              verbose_name=_('Загрузить изображение'))
    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = _('Изображение')

    def __str__(self):
        return self.name

    def as_json(self):
        return {
            "uuid": self.uuid,
            "name_ru": self.name,
            "name_ua": self.name_uk,
            "meta_keywords": self.meta_keywords,
            "meta_description": self.meta_description,
            "full_description_ru": self.full_description,
            "full_description_ua": self.full_description_uk,
            "alias": self.alias,
            "image": settings.MEDIA_URL+str(self.image)
        }

@receiver(pre_save, sender=Category)
def category_save(sender, instance, **kwargs):
    instance.alias=cyrtranslit.to_latin(instance.name, 'ru').replace(" ","_")

@receiver(pre_delete, sender=Mediafile)
def mymodel_delete(sender, instance, **kwargs):
    instance.file.delete(False)

@receiver(post_save, sender=Category)
@receiver(post_delete, sender=Category)
def Category_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(categories=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.categories=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

def get_project_image_filename(instance, filename):
    name = cyrtranslit.to_latin(instance.name, 'ru').lower().replace(" ","_")
    return f"projects/{name}/{filename}"

class Project(models.Model):
    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=64, blank=True, verbose_name=_('Название проекта по-русски'))
    name_uk = models.CharField(max_length=64, blank=True, verbose_name=_('Название проекта по-украински'))
    description = HTMLField(blank=True, verbose_name=_('Описание по-русски'))
    description_uk = HTMLField(blank=True, verbose_name=_('Описание по-украински')), 
    image = models.ImageField(upload_to=get_project_image_filename,
                              verbose_name=_('Загрузить изображение'))
    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))
    image_tag.short_description = _('Изображение')

@receiver(pre_delete, sender=Project)
def project_delete(sender, instance, **kwargs):
    instance.image.delete(False)

@receiver(post_save, sender=Project)
@receiver(post_delete, sender=Project)
def Project_saved(sender, instance, **kwargs):
    try:
        changes = Changes.objects.first()
    except:
        pass
    if changes is None:
        Changes.objects.create(projects=datetime.now().strftime("%d%m%Y%H%M%S%f"))
    else:
        changes.projects=datetime.now().strftime("%d%m%Y%H%M%S%f")
        changes.save()

