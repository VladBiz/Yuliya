from rest_framework import serializers
from .models import *
from django import forms
from django.conf import settings
import re

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = "__all__"


class CharacteristicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characteristic

    def to_representation(self, value):
        result = {
            "ru": {
                "name": value.name.characteristic_ru,
                "value": value.data_ru,
            },
            "ua": {
                "name": value.name.characteristic_ua,
                "value": value.data_ua,
            }
            }
        return result


class MediafileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mediafile
        fields = ['url', 'name' ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ['uuid', 'product']


class ProductListSerializer(serializers.ListSerializer):

    def to_representation(self, value):
        characteristics = {}
        for x in Characteristic.objects.all():
            d = x.as_json()
            if d["product"] not in characteristics:
                characteristics[d["product"]] = []
            characteristics[d["product"]].append(d)
        expr = re.compile(".+_[a-z]{2}$")
        result = []
        for product in value:
            temp = product.as_json()
            for lang in settings.LANGUAGES:
                obj = {}
                obj["language"] = lang[0]
                for key in temp:
                    if expr.match(key) is None:
                        obj[key] = temp[key]
                        continue
                    else:
                        try:
                            i = key.index("_"+lang[0])
                            obj[key[:i]] = temp[key]
                        except:
                            pass
                if obj["brand"] is not None:
                    if "brandName_"+lang[0] in obj["brand"]:
                        obj["brand"] = obj["brand"]["brandName_"+lang[0]]
                if obj["uuid"] in characteristics:
                    chars = {}
                    for d in characteristics[obj["uuid"]]:
                        if "characteristic_"+lang[0] in d and "data_"+lang[0] in d:
                            chars[d["characteristic_"+lang[0]]] = d["data_"+lang[0]]
                    obj["characteristics"] = chars
#!!!

                result.append(obj)
        return result

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['uuid', 'name', 'alias', 'price', 'category', 'meta_keywords', 'meta_description', 'full_description', 'main_image', 'comments_field']
        list_serializer_class = ProductListSerializer

    def to_representation(self, value):
        result = {
            'uuid': value.uuid,
            'name': value.name,
            'alias': value.alias,
            'price': value.price,
            'category': value.category.name,
            'category_alias': value.category.alias,
            'meta_keywords': value.meta_keywords,
            'meta_description': value.meta_description,
            'full_description': value.full_description,
            'brand': None,
            'main_image': None,
            'images':[],
            'characteristics': {},
            'comments_field': [],
            }
        if value.brand:
            result['brand'] = value.brand.brandName
        if value.main_image:
            result['main_image'] = value.main_image.as_json()
        images = Mediafile.objects.filter(product=value)
        characteristics = Characteristic.objects.filter(product=value)
        comments = Comments.objects.filter(product=value)
        if len(images) > 0:
            result['images'] = [image.as_json() for image in images ]
        if len(comments) > 0:
            result['comments_field'] = CommentsSerializer(comments, many=True).data
        if len(characteristics) > 0:
            for characteristic in characteristics:
                result['characteristics'][characteristic.name.characteristic] =  characteristic.data
        return result


class CategoryListSerializer(serializers.ListSerializer):

    def to_representation(self, value):
        expr = re.compile(".+_[a-z]{2}$")
        result = []
        items_count = 0
        for category in value:
            items_count += 1
            temp = category.as_json()
            for lang in settings.LANGUAGES:
                obj = {}
                obj["language"] = lang[0]
                obj["items_count"] = items_count
                for key in temp:
                    if expr.match(key) is None:
                        obj[key] = temp[key]
                    else:
                        try:
                            i = key.index("_"+lang[0])
                            obj[key[:i]] = temp[key]
                        except:
                            pass
                result.append(obj)
        return result

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['uuid', 'name', 'items_count', 'children', 'meta_keywords', 'meta_description', 'full_description']
        list_serializer_class = CategoryListSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
