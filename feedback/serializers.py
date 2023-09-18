from rest_framework import serializers

from feedback.models import Comment


class BaseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("id",)


class RetrieveCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ("id", "user", "food", )
