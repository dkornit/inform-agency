from django.urls import path

from app.models import Redactor
from app.views import index, NewspaperListView, RedactorListView, TopicListView, NewspaperDetailView, \
    RedactorDetailView, TopicDetailView, NewspaperCreateView, NewspaperUpdateView, NewspaperDeleteView

app_name = "app"

urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/<int:pk>", RedactorDetailView.as_view(), name="redactor-detail"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/<int:pk>/", TopicDetailView.as_view(), name="topic-detail"),
]