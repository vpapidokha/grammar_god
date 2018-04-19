from django.shortcuts import render
from .forms import UsersForm
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

import aspell


def main(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    texts=Text.objects.filter(session_key=session_key)
    count=texts.count()
    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    form = UsersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        global user
        try:
            user = User.objects.get(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
        except User.DoesNotExist:
            user = User.objects.create(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
        #user, created = User.objects.get_or_create(username=form.username, email=form.email)
        #user.set_password(form.password)
       # user.save()
        #new_form=form.save()


    return render(request, 'Spellcheck/main.html', locals())


def checkInputedText(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST

    inputedText = data.get("inputedText")
    #
    #print(checkTextExist)
    global checkTextExist
    try:
       checkTextExist = Text.objects.get(session_key=session_key, textInputed=inputedText)
       #checkTextExist = checkTextExist.objects.filter(session_key=session_key)

    except Text.DoesNotExist:
       checkTextExist= None
    #for t in checkTextExist:
    if checkTextExist is None:
        #checkTextExist = Text.objects.filter(textInputed=inputedText)
        #checkTextExist = checkTextExist.objects.filter(session_key=session_key)
        user = User.objects.filter(username="anonymous")

        language=data.get("language")
        if language=="English":
            s = aspell.Speller('lang', 'en')
        else:
            s=aspell.Speller('lang', 'uk')
        checkedText=s.check(inputedText)
        #new_inputedText
        for u in user:
            new_inputedText=Text.objects.create(user_id=2, session_key=session_key, language=language, textInputed=inputedText, textChecked=checkedText, dateTime=datetime.now())
            return_dict["userName"] = u.username

        #checkedText = inputedText
        return_dict["inputedText"]=inputedText
        return_dict["checkedText"] = checkedText
        return_dict["language"] = language
        return_dict["added"] = "true"
        return_dict["textId"]=new_inputedText.id
        return JsonResponse(return_dict)
    else:
        return_dict["inputedText"]=inputedText
        return_dict["checkedText"]=checkTextExist.textChecked
        return_dict["language"]=checkTextExist.language
        return_dict["added"]="false"
        #return_dict["userName"]=checkTextExist.user_name
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