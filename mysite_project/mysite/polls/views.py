from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import datetime

from .models import Question,Choice
# Create your views here.

""" def index(requset):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {"latest_questions_list":latest_questions_list,}
    return HttpResponse(template.render(context,requset)) """

""" def index(requset):
    latest_questions_list = Question.objects.order_by("-pub_date")[:5]
    return render(requset,"polls/index.html",{"latest_questions_list":latest_questions_list,}) """

""" def detail(requset,question_id):
    return HttpResponse("you're lookking at # QUESTION: %s" %question_id) """

""" def detail(requset,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doen not exist")
    return render(requset,"polls/detail.html", {"question":question}) """

""" def detail(requset,question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render (requset,"polls/detail.html",{"question":question}) """

"""def results (requset,question_id):
    return HttpResponse("yor're looking at results of # QUESTION: %s" %question_id) """

"""def results (requset,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(requset,"polls/results.html",{"question":question}) """

""" def vote (requset,question_id):
    return HttpResponse("you're voting on # QUESTION: %s" %question_id) """

class IndexView(generic.ListView):
    """docstring for IndexView."""
    template_name = "polls/index.html"
    context_object_name = "latest_questions_list"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView (generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote (requset,question_id):
    question = get_object_or_404(Question,pk = question_id)

    try:
        # Getting the selected option from the detail

        selected_choice = question.choice_set.get(pk=requset.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render (requset,"polls/detail.html",{"question":question,"error_message":"You did't select a choice."})
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results",args=(question.id,)))
