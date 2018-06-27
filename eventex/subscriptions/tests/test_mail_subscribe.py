from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Renan Moura', cpf='12345665443',
                    email='rvmoura.96@gmail.com', phone='11-92345-6789')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'rvmoura.96@gmail.com']

        self.assertEquals(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Renan Moura',
            '12345665443',
            'rvmoura.96@gmail.com',
            '11-92345-6789',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
