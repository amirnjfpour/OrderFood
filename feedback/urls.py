from django.urls import path

from feedback.views import AddCommentView

urlpatterns = [
    path("comment/", AddCommentView.as_view(), name="add_comment")
]
