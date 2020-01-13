from django.db import models
# Customer Details Model


class CustomerDetails(models.Model):
    u_id = models.TextField()
    name = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name


class SubItems(models.Model):
    unique_id = models.CharField(max_length=200)
    tamil_name = models.TextField(null=True, blank=True)
    name = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Vessels(models.Model):
    u_id = models.TextField()
    name = models.TextField()

    def __str__(self):
        return self.name


class Items(models.Model):
    unique_id = models.CharField(max_length=200)
    tamil_name = models.TextField(null=True, blank=True)
    name = models.TextField()
    price = models.IntegerField()
    total_price = models.IntegerField()
    subitems = models.ManyToManyField(SubItems)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    subitems = models.ForeignKey(SubItems, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    total_price = models.IntegerField()

    def __str__(self):
        return self.item.name


class Order(models.Model):
    invoice_no = models.TextField()
    ordered_items = models.ManyToManyField(OrderItem)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.DO_NOTHING)
    advance = models.IntegerField()
    session = models.TextField()
    total = models.IntegerField()
    paid_amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    returned_vessel = models.BooleanField(default=False)
    balance = models.IntegerField()
    date_placed = models.DateField(auto_now_add=True)
    date_of_delivery = models.DateField()

    def __str__(self):
        return self.invoice_no


# class DailyItems(models.Model):
#     unique_id = models.CharField(max_length=200)
#     quantity = models.IntegerField()
#     date=models.DateField(auto_now_add=True,null=True,blank=True)
#     session=models.CharField(max_length=100,blank=True,null=True)

#     def __str__(self):
#         return self.unique_id


# class DailySubItems(models.Model):
#     unique_id = models.CharField(max_length=200)
#     quantity = models.IntegerField()
#     session=models.CharField(max_length=100,blank=True,null=True)
#     date=models.DateField(auto_now_add=True,null=True,blank=True)

#     def __str__(self):
#         return self.unique_id
