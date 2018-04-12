from django.shortcuts import render
from .forms import UsersForm
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import datetime

def main(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    texts=Text.objects.filter(session_key=session_key)
    count=texts.count()
    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    form = UsersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_form=form.save()

    return render(request, 'Spellcheck/main.html', locals())


def checkInputedText(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST

    inputedText = data.get("inputedText")
    user = User.objects.filter(username="anonymous")

    print("kdkkdkd")
    language=data.get("language")
    for u in user:
        new_inputedText=Text.objects.create(user_id=2, session_key=session_key, language=language, textInputed=inputedText, textChecked=inputedText, dateTime=datetime.now())
    checkedText = inputedText
    return_dict["checkedText"] = checkedText
    return JsonResponse(return_dict)

def notFound(request):
    return render(request, 'Spellcheck/notfound.html', locals())


#def main(request, inputedText):
   # name = 'Kavinnnn'
    #texts=Text.objects.filter()
    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    #form = InputText(request.POST or None)

    #if request.method=="POST" and form.is_valid():
       # new_form=form.save()

   # return render(request, 'Spellcheck/main.html', locals())