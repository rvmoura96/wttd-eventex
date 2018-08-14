from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.core.models import Talk, Speaker, Course


class TalkListGet(TestCase):
    def setUp(self):
        talk = Talk.objects.create(title='Titulo da Palestra',
                                   start='10:00',
                                   description='Descrição da palestra.')

        talk_two = Talk.objects.create(title='Titulo da Palestra',
                                       start='13:00',
                                       description='Descrição da palestra.')

        course_one = Course.objects.create(title='Título do curso',
                                           start='09:00',
                                           description='Descrição do curso.',
                                           slots=20)

        speaker = Speaker.objects.create(name='Henrique Bastos',
                                         slug='henrique-bastos',
                                         website='http://henriquebastos.net')
        talk.speakers.add(speaker)
        talk_two.speakers.add(speaker)
        course_one.speakers.add(speaker)

        self.resp = self.client.get(r('talk_list'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        contents = [
            (2, 'Titulo da Palestra'),
            (1, '10:00'),
            (1, '13:00'),
            (3, '/palestrantes/henrique-bastos/'),
            (3, 'Henrique Bastos'),
            (2, 'Descrição da palestra.'),
            (1, 'Título do curso'),
            (1, '09:00'),
            (1, 'Descrição do curso'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    def test_content(self):
        variables = ['morning_talks', 'afternoon_talks', 'courses']

        for key in variables:
            with self.subTest():
                self.assertIn(key, self.resp.context)


class TalkListGetEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(r('talk_list'))

        self.assertContains(response, 'Ainda não há palestras de manhã.')
        self.assertContains(response, 'Ainda não há palestras de tarde.')