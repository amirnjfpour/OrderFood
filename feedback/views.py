from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.response import Response

from accounts.permissions import IsAuthenticated
from feedback.serializers import BaseCommentSerializer
from foods.models import Food


class AddCommentView(CreateAPIView):
    serializer_class = BaseCommentSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data["user"] = request.user.id
        serializer = self.get_serializer(data=mutable_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        food = get_object_or_404(Food, id=mutable_data["food"])
        food.update_average_score()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
