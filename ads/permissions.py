from rest_framework import permissions

from ads.models import Ad, Comment
from users.models import User, Role


class AdUpdateDeletePermission(permissions.BasePermission):
    message = "You can not touch this AD"

    def has_permission(self, request, view):
        try:
            ad = Ad.objects.get(pk=view.kwargs["pk"])
        except Ad.DoesNotExist:
            return False
        if ad.author.id == request.user.id:
            return True
        elif request.user.role != Role.USER:
            return True
        return False


class AddImagePermission(permissions.BasePermission):
    message = "You can not add to this User"

    def has_permission(self, request, view):
        try:
            user = User.objects.get(pk=view.kwargs["pk"])
        except User.DoesNotExist:
            return False
        if user.id == request.user.id:
            return True
        return False


class CommentUpdateDeletePermission(permissions.BasePermission):
    message = "You can not touch this Comment"

    def has_permission(self, request, view):
        try:
            com = Comment.objects.get(pk=view.kwargs["pk"])
        except User.DoesNotExist:
            return False
        if com.author.id == request.user.id:
            return True
        elif request.user.role != Role.USER:
            return True
        return False