from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    plan_id = models.IntegerField(default=0)
    active_phone_number = models.IntegerField(default=0, unique=True)


class Plan(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)
    customer_id = models.IntegerField(default=0)
    company_id = models.IntegerField(default=0)


class PaymentInfo(models.Model):
    plan_id = models.IntegerField(default=0)
    customer_id = models.IntegerField(default=0)
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=20)
    phone_id = models.IntegerField(default=0)
    withdraw = models.BooleanField(default=False)
