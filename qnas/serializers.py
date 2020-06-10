from rest_framework import serializers
from qnas.models import Qna, QnaComment, LikeQna, LikeQnaComment


class LikeQnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeQna
        fields = '__all__'


class LikeQnaCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeQnaComment
        fields = '__all__'


class QnaCommentSerializer(serializers.ModelSerializer):
    likes = LikeQnaCommentSerializer(many=True, required=False)
    class Meta:
        model = QnaComment
        fields = '__all__'
        

class QnaSerializer(serializers.ModelSerializer):
    likes = LikeQnaSerializer(many=True, required=False)
    comments = QnaCommentSerializer(many=True, required=False)
    class Meta:
        model = Qna
        fields = '__all__'

    def get(self, instance, validated_data):
        instance.views = validated_data.get('views', instance.views) + 1
        instance.save()
        return instance