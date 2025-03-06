from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import Newspaper, Redactor, Topic


# @login_required
def index(request):
    """View function for the home page of the site."""

    num_newspapers = Newspaper.objects.count()
    num_redactors = Redactor.objects.count()
    num_topics = Topic.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_newspapers": num_newspapers,
        "num_redactors": num_redactors,
        "num_topics": num_topics,
        "num_visits": num_visits + 1,
    }

    return render(request, "app/index.html", context=context)


class NewspaperListView(generic.ListView):
    model = Newspaper
    template_name = "app/newspaper_list.html"


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "app/redactor_list.html"


class TopicListView(generic.ListView):
    model = Topic
    template_name = "app/topic_list.html"
