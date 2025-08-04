from rest_framework import serializers
from .models import Post, Comment, Like


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ["id", "author", "text", "created_at"]
        read_only_fields = ["author", "created_at"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "text",
            "image",
            "created_at",
            "comments",
            "likes_count",
        ]
        read_only_fields = ["author", "created_at", "likes_count"]

    def get_likes_count(self, obj):
        return obj.likes.count()

    def validate(self, data):
        if len(data.get("text", "")) < 5:
            raise serializers.ValidationError(
                "Текст должен содержать минимум 5 символов"
            )
        return data


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ["id", "user", "created_at"]
        read_only_fields = ["user", "created_at"]
