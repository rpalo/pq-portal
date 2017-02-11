"""Quality Models"""

import datetime
from django.db import models


class PrimaryQualityItem(models.Model):
    """An abstract class to store the basic quality needs"""

    STATUS_CHOICES = (("OPEN", "Open"),
                      ("CLOSED", "Closed"))
    number = models.CharField("document number", unique=True, max_length=30)
    open = models.DateField("date opened", auto_now_add=True)
    closed = models.DateField("date closed", blank=True, null=True)
    customer = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def close(self):
        """Marks the current document as closed"""

        self.closed = datetime.date.today()
        self.status = "CLOSED"
        # Not sure if there needs to be a database save here or not
        # No return value

    def __str__(self):
        return self.number

    class Meta:
        abstract = True

class RMA(PrimaryQualityItem):
    """Return Material Authorization"""
    
    def get_absolute_url(self):
        return "/quality/rma/{}/".format(self.id)
