from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from. import mypythoncode
from .models import *
from .forms import *
# Create your views here.


def indd(request):
    return render(request,'forum/ind.html',{})


def begin(request):
    return render(request,'forum/start_page.html',{})
    pass

def display_ques(request):
    all_questions=Question.objects.all()
    context={'all_questions':all_questions}
    return render(request,'forum/display_questions.html',context)
    pass

def display_ans(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        obj = Answer(answer_text=answer, question_id_of_answer=question_id)
        obj.save()

    answers = Answer.objects.filter(question_id_of_answer=question_id)
    context = {'question': question, 'answers': answers}

    return render(request, 'forum/display_answers.html', context)


'''        ans = request.POST.get('answer','')

        question.answer_set.create(answer_text=ans)

        answers = question.answer_set.all()

        context = {'question': question, 'answers': answers}

        return render(request, 'forum/display_answers.html', context)

    return render(request, 'forum/display_answers.html', {'question': question})
    pass
'''

@login_required
def ask(request):
    return render(request, 'forum/ask_questions.html', {})

@login_required
def ask_questions(request):
    if request.method == 'POST':
        form=QuestionForm(request.POST)
        question = request.POST.get('question','')
        obj=Question(question_text=question,)
        obj.save()
    return render(request,'forum/start_page.html',{})
