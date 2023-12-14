from django.test import TestCase
from django.urls import reverse

from .models import Alvo

class ListaAlvosViewTest(TestCase):
    def test_lista_alvos_view(self):
        # Criar alguns alvos para testar
        Alvo.objects.create(
            identificador= 'ALV123', 
            nome='Alvo 1', 
            latitude=-23.5505 , 
            longitude=-46.6333, 
            data_expiracao='2012-12-12'
        )
        Alvo.objects.create(
            identificador= 'ALV456', 
            nome='Alvo 2', 
            latitude=-23.5505 , 
            longitude=-46.6333, 
            data_expiracao='2012-12-12'
        )

        # Obter a URL reversa para a view
        url = reverse('lista_alvos')

        # Fazer uma solicitação GET à view
        response = self.client.get(url)

        # Verificar se a resposta tem status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto está sendo usado
        self.assertTemplateUsed(response, 'lista_alvos.html')

        # Verificar se a lista de alvos está correta no contexto do template
        self.assertQuerysetEqual(
            response.context['object_list'],
            ['<Alvo: Alvo 1>', '<Alvo: Alvo 2>'],
            ordered=False
        )


class DetalheAlvoViewTest(TestCase):
    def test_detalhe_alvo_view(self):
        # Criar um alvo para testar
        alvo = Alvo.objects.create(
            identificador= 'ALV123', 
            nome='Alvo 1', 
            latitude=-23.5505 , 
            longitude=-46.6333, 
            data_expiracao='2012-12-12'
        )

        # Obter a URL reversa para a view com o ID do alvo
        url = reverse('detalhe_alvo', args=[str(alvo.pk)])

        # Fazer uma solicitação GET à view
        response = self.client.get(url)

        # Verificar se a resposta tem status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto está sendo usado
        self.assertTemplateUsed(response, 'detalhe_alvo.html')

        # Verificar se os detalhes do alvo estão corretos no contexto do template
        self.assertEqual(response.context['object'], alvo)


class AdicionarAlvoViewTest(TestCase):
    def test_adicionar_alvo_view(self):
        # Obter a URL reversa para a view de adição de alvo
        url = reverse('adicionar_alvo')

        # Fazer uma solicitação GET à view para obter o formulário
        response = self.client.get(url)

        # Verificar se a resposta tem status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto está sendo usado
        self.assertTemplateUsed(response, 'formulario_alvo.html')

        # Criar dados de alvo simulados para enviar ao formulário (opcional)
        dados_alvo = {
            'identificador': 'ALV456', 
            'nome': 'Alvo Teste', 
            'latitude': -23.5505, 
            'longitude': -46.6333, 
            'data_expiracao': '2012-12-12'
        }

        # Fazer uma solicitação POST à view para adicionar um novo alvo
        response = self.client.post(url, data=dados_alvo)

        # Verificar se o redirecionamento para a lista de alvos ocorre após uma adição bem-sucedida
        self.assertRedirects(response, reverse('lista_alvos'))

        # Verificar se o alvo foi realmente adicionado ao banco de dados (opcional)
        self.assertTrue(Alvo.objects.filter(nome='Alvo Teste').exists())
        

class EditarAlvoViewTest(TestCase):
    def setUp(self):
        # Criar um alvo de teste para ser editado
        self.alvo = Alvo.objects.create(
            identificador= 'ALV123', 
            nome='Alvo 1', 
            latitude=-23.5505 , 
            longitude=-46.6333, 
            data_expiracao='2012-12-12'
        )

    def test_editar_alvo_view(self):
        # Obter a URL reversa para a view de edição de alvo
        url = reverse('editar_alvo', kwargs={'pk': self.alvo.pk})

        # Fazer uma solicitação GET à view para obter o formulário
        response = self.client.get(url)

        # Verificar se a resposta tem status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto está sendo usado
        self.assertTemplateUsed(response, 'formulario_alvo.html')

        # Criar dados de alvo simulados para enviar ao formulário (opcional)
        dados_alvo = {
            'identificador': 'ALV456', 
            'nome': 'Alvo Teste', 
            'latitude': -23.5505, 
            'longitude': -46.6333, 
            'data_expiracao': '2012-12-12'
        }
        # Fazer uma solicitação POST à view para salvar as alterações no alvo
        response = self.client.post(url, data=dados_alvo)

        # Verificar se o redirecionamento para a lista de alvos ocorre após uma edição bem-sucedida
        self.assertRedirects(response, reverse('lista_alvos'))

        # Recarregar o alvo do banco de dados para verificar as alterações (opcional)
        self.alvo.refresh_from_db()

        # Verificar se as alterações foram salvas corretamente
        self.assertEqual(self.alvo.nome, 'Alvo Editado')


class ExcluirAlvoViewTest(TestCase):
    def setUp(self):
        # Criar um alvo de teste para ser excluído
        self.alvo = Alvo.objects.create(
            identificador= 'ALV123', 
            nome='Alvo 1', 
            latitude=-23.5505 , 
            longitude=-46.6333, 
            data_expiracao='2012-12-12'
        )

    def test_excluir_alvo_view(self):
        # Obter a URL reversa para a view de exclusão de alvo
        url = reverse('excluir_alvo', kwargs={'pk': self.alvo.pk})

        # Fazer uma solicitação GET à view para obter a confirmação de exclusão
        response = self.client.get(url)

        # Verificar se a resposta tem status HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verificar se o template correto está sendo usado
        self.assertTemplateUsed(response, 'app/alvo_confirm_delete.html')

        # Fazer uma solicitação POST à view para confirmar a exclusão
        response = self.client.post(url)

        # Verificar se o redirecionamento para a lista de alvos ocorre após uma exclusão bem-sucedida
        self.assertRedirects(response, reverse('lista_alvos'))

        # Verificar se o alvo foi removido do banco de dados
        with self.assertRaises(Alvo.DoesNotExist):
            self.alvo.refresh_from_db()