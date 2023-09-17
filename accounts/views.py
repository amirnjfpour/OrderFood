from rest_framework.generics import CreateAPIView

from accounts.serializers import RegisterSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
