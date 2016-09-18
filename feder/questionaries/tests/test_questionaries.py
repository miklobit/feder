from django.core.urlresolvers import reverse
from django.test import TestCase

from feder.main.mixins import PermissionStatusMixin

from .test_general import ObjectMixin

from ..models import Questionary


class QuestionaryCreateTestCase(ObjectMixin, PermissionStatusMixin, TestCase):
    permission = ['monitorings.add_questionary', ]

    def get_url(self):
        return reverse('questionaries:create',
                       kwargs={'monitoring': str(self.questionary.monitoring.pk)})


class QuestionaryListViewTestCase(ObjectMixin, PermissionStatusMixin, TestCase):
    permission = []
    status_anonymous = 200
    status_no_permission = 200

    def get_url(self):
        return reverse('questionaries:list')

    def test_content(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionaries/questionary_filter.html')
        self.assertContains(response, self.questionary.title)


class QuestionaryDetailsViewTestCase(ObjectMixin, PermissionStatusMixin, TestCase):
    permission = []
    status_anonymous = 200
    status_no_permission = 200

    def get_url(self):
        return self.questionary.get_absolute_url()

    def test_content(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'questionaries/questionary_detail.html')
        self.assertContains(response, self.questionary.title)


class QuestionaryUpdateTestCase(ObjectMixin, PermissionStatusMixin, TestCase):
    permission = ['monitorings.change_questionary', ]

    def get_url(self):
        return reverse('questionaries:update',
                       kwargs={'pk': self.questionary.pk})


class QuestionaryDeleteTestCase(ObjectMixin, PermissionStatusMixin, TestCase):
    permission = ['monitorings.delete_questionary', ]

    def get_url(self):
        return reverse('questionaries:delete',
                       kwargs={'pk': self.questionary.pk})

    def test_get_success_url(self):
        self.grant_permission()
        self.client.login(username='john', password='pass')
        response = self.client.post(self.get_url())
        self.assertFalse(Questionary.objects.filter(pk=self.questionary.pk).exists())
        self.assertRedirects(response,
                             '/monitorings/%s' %
                             (self.questionary.monitoring.slug))
