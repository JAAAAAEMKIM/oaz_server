from rest_framework import serializers
from boards.models import Post, Comment, LikePost, LikeComment


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = '__all__'


class LikeCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeComment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    likes = LikeCommentSerializer(many=True, required=False)
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    likes = LikePostSerializer(many=True, required=False)
    comment = CommentSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = '__all__'

    def get(self, instance, validated_data):
        instance.views = validated_data.get('views', instance.views) + 1
        instance.save()
        return instance