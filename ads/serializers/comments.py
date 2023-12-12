from rest_framework import serializers

from ads.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    author_image = serializers.URLField(source='author.image', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    ad_id = serializers.PrimaryKeyRelatedField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id',
                  'author_image')


class CommentCreateSerializer(serializers.ModelSerializer):
    author_image = serializers.URLField(source='author.image', read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    ad_id = serializers.PrimaryKeyRelatedField(source='ad.id', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author_id', 'created_at', 'author_first_name', 'author_last_name', 'ad_id',
                  'author_image')


class CommentDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id"]
