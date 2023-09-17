from rest_framework.generics import CreateAPIView

from accounts.permissions import IsSuperuser
from accounts.serializers import RegisterSerializer, AddAdminSerializer


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class AddAdminView(CreateAPIView):
    serializer_class = AddAdminSerializer
    permission_classes = (IsSuperuser,)
