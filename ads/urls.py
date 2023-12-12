from django.urls import path

from ads.views import ads as ads_view, comments as com_view


urlpatterns = [
    path('ads/', ads_view.AdListView.as_view()),
    path('ads/me/', ads_view.AdMeListView.as_view()),
    path('ads/<int:pk>/', ads_view.AdDetailView.as_view()),
    path('ads/create/', ads_view.AdCreateView.as_view()),
    path('ads/<int:pk>/update/', ads_view.AdUpdateView.as_view()),
    path('ads/<int:pk>/delete/', ads_view.AdDeleteView.as_view()),

    path('ads/<int:ad>/comments/', com_view.CommentListView.as_view()),
    path('ads/<int:ad>/comments/<int:pk>/', com_view.CommentDetailView.as_view(), name='comment_detail'),
    path('ads/<int:ad>/comments/create/', com_view.CommentCreateView.as_view(), name='comment-create'),
    path('ads/<int:ad>/comment/<int:pk>/', com_view.CommentUpdateView.as_view(), name='comment-update'),
    path('ads/<int:ad>/comment/<int:pk>/delete/', com_view.CommentDeleteView.as_view(), name='comment_delete'),
]