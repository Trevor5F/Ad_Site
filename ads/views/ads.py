from djoser.serializers import UserSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from django_filters import rest_framework as filters
from ads.filters import MyModelFilter
from ads.models import Ad
from ads.permissions import AdUpdateDeletePermission, AddImagePermission
from ads.serializers.ads import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdDestroySerializer
from users.models import User


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MyModelFilter


class AdMeListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get_queryset(self):
        user = self.request.user
        return Ad.objects.filter(author=user)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer
    permission_classes = [AdUpdateDeletePermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [AdUpdateDeletePermission]


class UserUploadImageView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AddImagePermission]

    def put(self, request, *args, **kwargs):
        ad = self.get_object()
        serializer = self.serializer_class(ad, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
