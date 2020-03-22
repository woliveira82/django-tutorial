from django.shortcuts import render

from django.http import HttpResponse

from .models import Question
# Create your views here.

def index(request):
    latest_question = Question.objects.order_by('pub_date')[:5]
    output = ', '.join(q.question_text for q in latest_question)
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse(f'Detail view for {question_id}')

def results(request, question_id):
    return HttpResponse(f'Result view for {question_id}')
    
def vote(request, question_id):
    return HttpResponse(f'Vote view for {question_id}')
