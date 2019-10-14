from django.shortcuts import render
from django.http import HttpResponse
from Business.Teams import Teams
from .forms import QuestionForm

def index(request):
    teams = Teams()
    vals = teams.GetTeams('test')
    context = { 'team_list': vals, }
    return render(request, 'teams/index.html', context)

def question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            return "OK!"
    else:
        form = QuestionForm()
    
    return render(request, 'teams/question.html', { 'form': form })


