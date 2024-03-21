from django.shortcuts import render, get_object_or_404
from .models import Aluno
from django.http import HttpResponse


def alunoView(request):
    alunos_list = Aluno.objects.all()
    return render(request, 'main/alunos.html', {'alunos_list': alunos_list})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    print(aluno)
    return render(request, 'main/alunoID.html', {'aluno':aluno})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print('name:', name)
        print('Email:', email)
        print('Message:', message)
    return render (request, 'main/contact.html')

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import AlunoForm

class AlunoCreateViews(CreateView):
    model = Aluno
    form_class = AlunoForm
    success_url = reverse_lazy('aluno-lista')
    template_name = 'main/aluno_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AlunoUpdateView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'main/aluno_form.html'
    success_url = reverse_lazy('aluno-lista')

    