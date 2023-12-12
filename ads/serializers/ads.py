from rest_framework import serializers
from ads.models import Ad


class AdListSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source='author.image', read_only=True)

    class Meta:
        model = Ad
        fields = ["id", "title", "price", "description", "image"]


class AdDetailSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source='author.image', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = ('id', "title", 'price', 'description', 'image', 'author_id', 'author_first_name', 'author_last_name',
                  'phone')


class AdCreateSerializer(serializers.ModelSerializer):
    image = serializers.URLField(source='author.image', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        fields = ('id', "title", 'price', 'description', 'image', 'author_id', 'author_first_name', 'author_last_name',
                  'phone')

    def create(self, validated_data):
        # получает текущего пользователя из контекста запроса и
        # использует его в качестве автора для новой записи обьекта `Ad`
        user = self.context['request'].user
        return Ad.objects.create(author=user, **validated_data)

    # def create(self, validated_data):
    #     try:
    #         author_id = validated_data.pop('author_id')
    #         author = User.objects.get(id=author_id)
    #     except (KeyError, User.DoesNotExist):
    #         raise serializers.ValidationError("Invalid author ID")
    #
    #     validated_data['author'] = author
    #     ad = Ad.objects.create(**validated_data)
    #     return ad


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["id"]
