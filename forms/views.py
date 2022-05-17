
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from forms.forms import CadastroMedico
# Create your views here.


def formulario(request):
    register_form_data = request.session.get('register_form_data')

    form = CadastroMedico(register_form_data)
    return render(request, 'forms/pages/formulario.html', context={
        'forms': form,

        'form_action': reverse('formu:create'),
    })


def verifica_formulario(request):

    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = CadastroMedico(POST, request.FILES)

    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        del(request.session['register_form_data'])
        return redirect(reverse('clinica:home'))

    return redirect('formu:formulario')
