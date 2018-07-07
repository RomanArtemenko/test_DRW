from django.contrib.auth.models import User
from rest_framework import serializers
from app_post.models import Post, Category

class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=20)
    is_active = serializers.BooleanField()
    user = serializers.IntegerField(source='user_id')


class PostSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choices=Post.STATUSES, default=Post.STATUS_DRAFT)
    # category = serializers.IntegerField(source='category_id')
    category = CategorySerializer(required=True)
    user = serializers.IntegerField(source='user_id', read_only=True)
    title = serializers.CharField(max_length=255, required=True)
    create = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        # instance.category_id = validated_data['category']['id']
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

    def create(self, instance, validated_data):
        pass

        # def update(self, instance, validated_data):
        #     instance.title = validated_data.get('title', instance.title)
        #     instance.code = validated_data.get('code', instance.code)
        #     instance.linenos = validated_data.get('linenos', instance.linenos)
        #     instance.language = validated_data.get('language', instance.language)
        #     instance.style = validated_data.get('style', instance.style)
        #     instance.save()
        #     return instance
