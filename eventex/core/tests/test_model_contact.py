from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Renan Moura',
            slug='renan-moura',
            photo=('https://www.instagram.com/p/BkGgiO5httC346'
                   '-DwMbVOVsermiHSO_lT3F4E80/?taken-by=renan_moura96')
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.EMAIL,
                                         value='rvmoura.96@gmail.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.PHONE,
                                         value='11-944449999')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P."""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind='E',
                          value='rvmoura.96@gmail.com')
        self.assertEqual('rvmoura.96@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Renan Moura',
            slug='renan-moura',
            photo='http://hbn.link/arnaldinho-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='rvmoura.96@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='11-911111111')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['rvmoura.96@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['11-911111111']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)