from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date, timedelta


class Qualification(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    description = models.TextField(verbose_name='Cup description', max_length=100)
    experience = models.FloatField(verbose_name='Experience in years', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'
        ordering = ['pk']


class Contract(models.Model):
    name = models.CharField(verbose_name='Name', max_length=50, unique=True)
    salary = models.DecimalField(verbose_name='Salary', max_digits=9, decimal_places=2)
    term = models.IntegerField(verbose_name='Contract in month', default=12)
    start = models.DateField(verbose_name='Contract start', default=date.today)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contracts'
        ordering = ['pk']


class Cup(models.Model):
    name = models.CharField(verbose_name='Cup name', max_length=100, unique=True)
    description = models.TextField(verbose_name='Cup description', max_length=100)
    premium = models.DecimalField(verbose_name='Premium', max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cup'
        verbose_name_plural = 'Cups'
        ordering = ['pk']


class Title(models.Model):
    name = models.CharField(verbose_name='Title name', max_length=100, unique=True)
    description = models.TextField(verbose_name='Title description', max_length=100)
    premium = models.DecimalField(verbose_name='Premium', max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = 'Titles'
        ordering = ['pk']


class Achievement(models.Model):
    name = models.CharField(verbose_name='Goal name', max_length=100, unique=True)
    cup = models.ForeignKey('Cup', on_delete=models.PROTECT)
    title = models.ForeignKey('Title', on_delete=models.PROTECT)
    match_count = models.IntegerField(verbose_name='Match', default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'
        ordering = ['pk']


class PersonnelCategory(models.Model):
    name = models.CharField(verbose_name='Personnel category name', max_length=50, unique=True)
    description = models.TextField(verbose_name='Cup description', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Personnel category'
        verbose_name_plural = 'Personnel categories'
        ordering = ['pk']


class Personnel(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    middle_name = models.CharField(verbose_name='Middle name', max_length=50)
    email = models.EmailField(verbose_name='Email', max_length=80, unique=True, default='someworkmail@gmail.com')
    phone = PhoneNumberField(verbose_name='Telephone number', unique=True, default='+375333215378')
    position = models.ForeignKey('PersonnelCategory', on_delete=models.PROTECT)
    qualification = models.ForeignKey('Qualification', on_delete=models.PROTECT)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Personnel'
        verbose_name_plural = 'Personnel'
        ordering = ['pk']


class PlayerCategory(models.Model):
    name = models.CharField(verbose_name='Player category name', max_length=50, unique=True)
    description = models.TextField(verbose_name='Cup description', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Player category'
        verbose_name_plural = 'Player categories'
        ordering = ['pk']


class Player(models.Model):
    first_name = models.CharField(verbose_name='First name', max_length=50)
    last_name = models.CharField(verbose_name='Last name', max_length=50)
    middle_name = models.CharField(verbose_name='Middle name', max_length=50)
    country = models.CharField(verbose_name='Country name', max_length=100)
    age = models.IntegerField(verbose_name='Player age', default=16)
    phone = PhoneNumberField(verbose_name='Telephone number', unique=True, default='+375333215378')
    image = models.ImageField(verbose_name='Image', upload_to='photos/', blank=True, null=True)
    position = models.ForeignKey('PlayerCategory', on_delete=models.PROTECT)
    achievement = models.ForeignKey('Achievement', on_delete=models.PROTECT)
    qualification = models.ForeignKey('Qualification', on_delete=models.PROTECT)
    contract = models.OneToOneField('Contract', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ['pk']
