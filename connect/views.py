from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import QuestionForm
from firebase_token_generator import create_token

# Create your views here.

@login_required
def dashboard(request):
    open_questions = Question.objects.filter(profile=request.user.profile, is_solved=False)
    closed_questions = Question.objects.filter(profile=request.user.profile, is_solved=True)
    return render(request, 'connect/dashboard.html', {'open_questions': open_questions, 'closed_questions': closed_questions})

@login_required
def ask(request):
    context = {'form': QuestionForm()}
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.profile = request.user.profile
            question.save()
            return redirect('question-details', question_id=question.id)
    return render(request, 'connect/ask.html', context)

@login_required
def question_details(request, question_id):
    question = Question.objects.get(pk=question_id)
    auth_payload = {"uid": str(request.user.id), "username": request.user.username}
    token = create_token("RYm9fEIJ0DLyOfAOBmRShcER71JgNPIw4cNX61GD", auth_payload)
    return render(request, 'connect/question_details.html', {'question': question, 'token': token})
    
@login_required
def answer(request):
    open_questions = Question.objects.exclude(profile=request.user.profile).filter(is_solved=False)
    return render(request, 'connect/answer.html', {'open_questions': open_questions})

@login_required
def history(request):
    return render(request, 'connect/history.html')