from autoslug.fields import AutoSlugField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from model_utils.managers import PassThroughManager
from model_utils.models import TimeStampedModel

from feder.institutions.models import Institution
from feder.monitorings.models import Monitoring


class CaseQuerySet(models.QuerySet):
    def with_letter_count(self):
        return self.annotate(letter_count=models.Count('letter'))

    def area(self, jst):
        return self.filter(institution__jst__tree_id=jst.tree_id,
                           institution__jst__lft__range=(jst.lft, jst.rght))


class Case(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    slug = AutoSlugField(populate_from='name', verbose_name=_("Slug"), unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    monitoring = models.ForeignKey(Monitoring, verbose_name=_("Monitoring"))
    institution = models.ForeignKey(Institution, verbose_name=_("Institution"))
    email = models.CharField(max_length=75, db_index=True, null=True)
    objects = PassThroughManager.for_queryset_class(CaseQuerySet)()

    class Meta:
        verbose_name = _("Case")
        verbose_name_plural = _("Case")
        ordering = ['created', ]

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cases:details', kwargs={'slug': self.slug})


@receiver(post_save, sender=Case)
def my_callback(sender, instance, *args, **kwargs):
    if not instance.email:
        email = settings.CASE_EMAIL_TEMPLATE.format(instance.pk)
        instance.email = email
        instance.save()

