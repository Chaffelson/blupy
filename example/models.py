from django.db import models
from .tasks import add_numbers

# Create your models here.


class Adder(models.Model):
    x = models.IntegerField(
        default=1,
        help_text=u'Set both x and y and hit save for celery to calculate the result'
    )
    y = models.IntegerField(
        default=1,
        help_text=u'Set both x and y and hit save for celery to calculate the result'
    )
    result = models.IntegerField(
        null=True,
        blank=True
    )

    def __unicode__(self):
        return u'{0} + {1} = {2}'.format(
            self.x,
            self.y,
            self.result
        )

    def save(self, *args, **kwargs):
        super(Adder, self).save(*args, **kwargs)
        if self.result is None or self.x + self.y != self.result:
            add_numbers.delay(self.pk)
