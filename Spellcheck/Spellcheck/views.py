from django.shortcuts import render
from .forms import UsersForm
from .models import Text

def main(request):
    name = 'Kavinnnn'
    texts=Text.objects.filter()
    #UsersForm.fields['email'].widget.attrs['placeholder'] = 'name'
    form = UsersForm(request.POST or None)

    if request.method=="POST" and form.is_valid():

        new_form=form.save()

    return render(request, 'Spellcheck/main.html', locals())