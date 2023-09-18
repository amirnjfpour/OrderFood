from rest_framework.generics import CreateAPIView

from accounts.permissions import IsAuthenticated
from feedback.serializers import CreateCommentSerializer


class AddComment(CreateAPIView):
    serializer_class = CreateCommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
