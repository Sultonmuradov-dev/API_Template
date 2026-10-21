from rest_framework.serializers import ModelSerializer

from apps.models import PostModel


class PostSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'