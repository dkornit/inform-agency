from django.urls import path

from app.models import Redactor
from app.views import index, NewspaperListView, RedactorListView, TopicListView

app_name = "app"

urlpatterns = [
    path("", index, name="index"),
    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("topics/", TopicListView.as_view(), name="topic-list"),

]