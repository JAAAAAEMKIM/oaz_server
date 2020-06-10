from rest_framework import serializers
from notices.models import Notice

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.views = validated_data.get('views', instance.views) + 1
        print(instance)
        instance.save()
        return instance