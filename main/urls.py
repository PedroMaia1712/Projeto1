from django.urls import path
from . import views
from .views import AlunoUpdateView

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),

    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),

    path('alunoContact', views.contact_view, name='contato'),
    path('aluno/create/', views.AlunoCreateViews.as_view(), name='aluno-create'),
    path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
    path('alunoDelete/<int:id>', views.deleteAluno, name='aluno-delete')
]

