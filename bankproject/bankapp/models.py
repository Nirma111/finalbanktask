from django.db import models

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class SubArea(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    sub_area = models.ForeignKey(SubArea, on_delete=models.SET_NULL, blank=True, null=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.SET_NULL, blank=True, null=True)
    materials_provide = models.ManyToManyField('Materials')

    def __str__(self):
        return self.name

class Materials(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
