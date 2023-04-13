from django.shortcuts import redirect
from django.urls import reverse_lazy
from core.forms import EnderecoForm, PessoaForm, TimeForm
from core.models import Pessoa, Time, Endereco
from formtools.wizard.views import SessionWizardView
from django.views.generic.list import ListView

# Create your views here.
class PessoaWizardView(SessionWizardView):
    template_name = 'form.html'
    form_list = [PessoaForm,TimeForm,EnderecoForm]
    success_url = reverse_lazy('list-dados')

    def done(self,form_list, **kwargs):
        pessoa_form, time_form, endereco_form = form_list
        pessoa = pessoa_form.save()
        time = time_form.save(commit=False)
        endereco = endereco_form.save(commit=False)
        time.pessoa = pessoa
        endereco.pessoa = pessoa
        time.save()
        endereco.save()

        return redirect(self.success_url)


    
class PessoaURLsWizardView(SessionWizardView):
    template_name = 'form.html'
    form_list = [PessoaForm,TimeForm,EnderecoForm]
    success_url = reverse_lazy('list-dados')
    template_names = ['pessoa_add.html', 'time_add.html', 'endereco_add.html']

    def get_template_names(self):
        """Retorna o nome do modelo para a etapa atual."""
        return self.template_names

    def done(self,form_list, **kwargs):
        """Salva os objetos Pessoa, Time e Endereco no banco de dados."""
        pessoa_form, time_form, endereco_form = form_list

        pessoa = pessoa_form.save()
        time = time_form.save(commit=False)
        endereco = endereco_form.save(commit=False)

        time.pessoa = pessoa
        endereco.pessoa = pessoa

        time.save()
        endereco.save()

        return redirect(self.success_url)

class PessoaListView(ListView):
    model = Pessoa
    template_name = 'done.html'

    def get_queryset(self):
        return Pessoa.objects.prefetch_related('time_set', 'endereco_set').all()