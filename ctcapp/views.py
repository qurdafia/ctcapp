from django.shortcuts import render, redirect, get_object_or_404
from .forms import SurveyModelForm
from .models import Survey


def welcome(request):
    return render(request, 'ctcapp/survey_welcome.html', {'welcome': welcome})


def surveys(request):
    survey_list = Survey.objects.all().order_by('submitted')
    return render(request, 'ctcapp/survey_list.html', {'survey_list': survey_list})


def survey_detail(request, pk):
    survey = get_object_or_404(Survey, pk=pk)
    return render(request, 'ctcapp/survey_detail.html', {'survey': survey})


def survey_form(request):
    if request.method == 'POST':
        form = SurveyModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('surveys')

    else:
        form = SurveyModelForm()

    return render(request, 'ctcapp/survey_form.html', {'form': form})
