from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.models import Newspaper, Redactor, Topic


# @login_required
def index(request):

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
    paginate_by = 3


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("app:newspaper-list")
    template_name = "app/newspaper_form.html"

class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("app:newspaper-list")
    template_name = "app/newspaper_form.html"


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("app:newspaper-list")


class RedactorListView(generic.ListView):
    model = Redactor
    template_name = "app/redactor_list.html"


class RedactorDetailView(generic.DetailView):
    model = Redactor
    template_name = "app/redactor_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newspapers'] = self.object.newspaper_set.all()
        return context

class RedactorCreateView(generic.CreateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("app:redactor-list")
    template_name = "app/redactor_form.html"


class RedactorUpdateView(generic.UpdateView):
    model = Newspaper
    fields = ("year_of_experience")
    success_url = reverse_lazy("app:redactor-list")
    template_name = "app/redactor_form.html"


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("app:redactor-delete")


class TopicListView(generic.ListView):
    model = Topic
    template_name = "app/topic_list.html"


class TopicDetailView(generic.DetailView):
    model = Topic
    template_name = "app/topic_detail.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newspapers"] = Newspaper.objects.filter(topic=self.object)
        return context


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("app:topic-list")
    template_name = "app/topic_form.html"


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    template_name = "app/topic_form.html"
    success_url = reverse_lazy("app:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("app:topic-list")

