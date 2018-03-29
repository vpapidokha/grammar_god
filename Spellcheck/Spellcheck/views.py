from django.shortcuts import render
from .forms import UsersForm

def main(request):
    name = 'Kavinnnn'

    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    form = UsersForm(request.POST or None)

    if request.method=="POST" and form.is_valid():

            new_form=form.save()

    return render(request, 'Spellcheck/main.html', locals())