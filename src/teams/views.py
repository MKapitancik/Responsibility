from django.shortcuts import render, redirect
from django.http import HttpResponse
from Services.Teams import Teams
from .forms import QuestionForm

def index(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
             return redirect(search, question = form.cleaned_data['question'])
    else:
        form = QuestionForm()
    
    return render(request, 'teams/index.html', { 'form': form })   

def search(request, question):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
             return redirect(search, question = form.cleaned_data['question'])
    else:
        form = QuestionForm()
        teams = Teams()
        vals = teams.GetTeams(question)
        context = { 'form': form, 'team_list': vals }
        return render(request, 'teams/search.html', context)