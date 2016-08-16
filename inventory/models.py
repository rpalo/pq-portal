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
        return self.number

    def get_absolute_url(self):
        return "/inventory/detail/{}/".format(str(self.id))

class Log(models.Model):

    plastic = models.ForeignKey('Plastic', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    change = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.timestamp)

    class Meta:
        ordering = ['-timestamp']
