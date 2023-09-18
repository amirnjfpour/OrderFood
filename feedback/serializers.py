from rest_framework import serializers

from feedback.models import Comment


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ("id",)
