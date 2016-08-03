from django.db import models

class Plastic(models.Model):

    number = models.CharField("plastic part number",max_length=30)
    description = models.CharField(max_length=50)
    quantity = models.DecimalField(max_digits=5, decimal_places=1)
    purchase_date = models.DateField("last date of purchase", blank=True, null=True)
    vendor = models.CharField(max_length=30, blank=True)
    purchase_price = models.DecimalField("last purchase price", max_digits=5, decimal_places=2, blank=True, null=True)
    order_threshhold = models.DecimalField(max_digits=5, decimal_places=1)

    def needs_ordered(self):
        return self.quantity < self.order_threshhold

    def __str__(self):
        return "<Plastic {}>".format(self.number)

    def get_absolute_url(self):
        return "/inventory/detail/{}/".format(str(self.id))
