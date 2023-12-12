from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from ads.models import Comment, Ad
from ads.permissions import CommentUpdateDeletePermission
from ads.serializers.comments import CommentListSerializer, CommentCreateSerializer, CommentDestroySerializer


class CommentListView(ListAPIView):
    serializer_class = CommentListSerializer
    #  Список отзывов к объявлению

    def get_queryset(self):
        ad_id = self.kwargs['ad']
        return Comment.objects.filter(ad=ad_id)


class CommentDetailView(RetrieveAPIView):
    serializer_class = CommentListSerializer

    def get_queryset(self):
        ad_id = self.kwargs['ad']
        return Comment.objects.filter(ad=ad_id)


class CommentCreateView(CreateAPIView):
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad']  # Получаем значение <int:ad> из URL-параметров
        ad = Ad.objects.get(id=ad_id)

        serializer.save(author=self.request.user, ad=ad)


class CommentUpdateView(UpdateAPIView):
    serializer_class = CommentCreateSerializer
    permission_classes = [CommentUpdateDeletePermission]

    def get_queryset(self):
        ad_id = self.kwargs['ad']
        return Comment.objects.filter(ad=ad_id)

    def perform_update(self, serializer):
        serializer.save()


class CommentDeleteView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDestroySerializer
    permission_classes = [CommentUpdateDeletePermission]
