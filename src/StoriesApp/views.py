from django.shortcuts import render, redirect
from django.http import HttpResponse
from Services.Stories import Stories
from .forms import QuestionForm

stories = Stories()

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
        predictions = stories.GetTeamPrediction(question)
        context = { 'form': form, 'team_list': predictions }
        return render(request, 'teams/search.html', context)