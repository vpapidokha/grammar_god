from django.shortcuts import render
from .forms import UsersForm
from .models import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import auth
from django.template.context_processors import csrf
from datetime import datetime, timedelta
from django.shortcuts import render_to_response, redirect, HttpResponseRedirect

import aspell

def account(request):
    render(request, 'Spellcheck/account.html', locals())

def loginInAccount(request):
    args={}
    args.update(csrf(request))
    if request.POST:
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
        userCheck=auth.authenticate(username=username, password=password)
        if userCheck is not None:
            auth.login(request, userCheck)
            return render(request, "Spellcheck/account.html", locals())
        else:
            login_error="User wasn't found!"
            return render(request, "Spellcheck/main.html", locals())
    else:
        return render(request, "Spellcheck/main.html", locals())

def main(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    texts=""
    historyOfOthers=""
    form = UsersForm(request.POST or None)
    countUsersText=0
    ifThereUserAuthenticated = False
    if request.user.is_authenticated:
        id = request.user.id
        texts = Text.objects.filter(user_id=id)
        historyOfOthers=Text.objects.filter().exclude(user_id=id)
        countUsersText=historyOfOthers.count()
        allUsers=User.objects.filter()
        ifThereUserAuthenticated = True
    else:
        id=2
        texts = Text.objects.filter(session_key=session_key)
        ifThereUserAuthenticated = False

    allUser=User.objects.filter(id=id)
    currentUserNow=None
    for a in allUser:
        currentUserNow=a
    count=texts.count()
    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    print('Herere')
    if not request.user.is_authenticated:

        if 'login' in request.POST:
            if request.method == "POST":
                print("login")
                username = request.POST.get('username', '')
                password = request.POST.get('password', '')
                userCheck = auth.authenticate(username=username, password=password)
                if userCheck is not None:
                    auth.login(request, userCheck)
                    historyOfOthers = Text.objects.filter().exclude(user_id=id)
                    texts = Text.objects.filter(user_id=request.user.id)
                    allUsers = User.objects.filter()
                    count = texts.count()
                    countUsersText = historyOfOthers.count()
                    ifThereUserAuthenticated = True
                    return render(request, "Spellcheck/account.html", locals())
                else:
                    login_error = "User wasn't found!"
                    return render(request, "Spellcheck/main.html", locals())
            else:
                return render(request, "Spellcheck/main.html", locals())

        elif 'signup' in request.POST:
            if request.method == "POST" and form.is_valid():
                global user
                try:
                    user = User.objects.get(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
                except User.DoesNotExist:
                    user = User.objects.create(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
                    user.set_password(form.cleaned_data['password'])
                    user.save()
        return render(request, 'Spellcheck/main.html', locals())

    else:

        if 'delete' in request.POST:
            if request.POST == "POST":
                print("Here")
                id = request.POST.get('id', '')
                print(id)

                a=Text.objects.filter(id=id).delete()

        return render(request, 'Spellcheck/account.html', locals())

def deleteQuery(request):
    return_dict = dict()
    return JsonResponse(return_dict)

def checkInputedText(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST

    inputedText = data.get("inputedText")
    if request.user.is_authenticated:
        current_user = User.objects.filter(id=request.user.id)
    else:
        current_user = User.objects.filter(id=2)
    global checkTextExist
    try:
        if request.user.is_authenticated:
            checkTextExist = Text.objects.get(user_id=request.user.id, textInputed=inputedText)
        else:
            checkTextExist = Text.objects.get(session_key=session_key, textInputed=inputedText)

        #checkTextExist = checkTextExist.objects.filter(session_key=session_key)

    except Text.DoesNotExist:
        checkTextExist= None
    #for t in checkTextExist:
    if checkTextExist is None:
        #checkTextExist = Text.objects.filter(textInputed=inputedText)
        #checkTextExist = checkTextExist.objects.filter(session_key=session_key)
        #if request.user.is_authenticated:
        #   user = User.objects.filter(username=request.user.username)
        # else:
        #   user = User.objects.filter(username="anonymous")

        language=data.get("language")
        if language=="English":
            s = aspell.Speller('lang', 'en')
        else:
            s=aspell.Speller('lang', 'uk')
        checkedText=s.check(inputedText)
        textSuggestion="| "
        if checkedText==False:
            for oneSuggest in s.suggest(inputedText):
                textSuggestion += oneSuggest + " | "
            if textSuggestion == "| ":
                textSuggestion = "Sorry, but we haven't found any similar words in our dictionary."
        # textSuggestionTwo=s.suggest(inputedText)
        else:
            textSuggestion=""
        new_inputedText=None
        for u in current_user:
            new_inputedText=Text.objects.create(user_id=u.id, session_key=session_key, language=language, textInputed=inputedText, textChecked=checkedText, textSuggestion=textSuggestion, dateTimeCreated=datetime.now(), dateTimeDelete=(datetime.now()+timedelta(minutes = 10)))
            return_dict["mycurrentUser"] = u.username

        return_dict["inputedText"]=inputedText
        return_dict["checkedText"] = checkedText
        return_dict["language"] = language
        return_dict["suggest"] = textSuggestion
        return_dict["added"] = "true"
        return_dict["textId"]=new_inputedText.id
        return_dict["dateCreated"] = new_inputedText.dateTimeCreated
        return JsonResponse(return_dict)
    else:
        return_dict["inputedText"]=inputedText
        return_dict["checkedText"]=checkTextExist.textChecked
        return_dict["language"]=checkTextExist.language
        return_dict["suggest"] = checkTextExist.textSuggestion
        return_dict["added"]="false"
        for a in current_user:
            return_dict["mycurrentUser"]=a.username
        return_dict["dateCreated"]=checkTextExist.dateTimeCreated
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