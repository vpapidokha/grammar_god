from django.shortcuts import render
from .forms import UsersForm
from .models import Text

def main(request):
    session_key=request.session.session_key
    if not session_key:
        request.session.cycle_key()

    name = 'Kavinnnn'
    texts=Text.objects.filter()
    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    form = UsersForm(request.POST or None)

    if request.method=="POST" and form.is_valid():
        new_form=form.save()

    return render(request, 'Spellcheck/main.html', locals())

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