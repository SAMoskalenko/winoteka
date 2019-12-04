from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Страна происхождения')

    def __str__(self):
        return u'%s' % self.name


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='Регион происхождения')
    country = models.ManyToManyField('Country', verbose_name='Страна происхождения', related_name='region')

    def country_list(self):
        return ', '.join([str(a.name) for a in self.country.all()])

    def __str__(self):
        return u'%s' % self.name


class Area(models.Model):
    name = models.CharField(max_length=50, verbose_name='Административная область')
    region = models.ForeignKey('Region', on_delete=models.PROTECT, related_name='area')

    def __str__(self):
        return u'%s' % self.name


class Quality(models.Model):
    name = models.CharField(max_length=50, verbose_name='Марка качества')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, related_name='quality', blank=True,
                                null=True)
    region = models.ForeignKey('Region', on_delete=models.PROTECT, related_name='quality', blank=True, null=True)
    area = models.ForeignKey('Area', on_delete=models.PROTECT, related_name='quality', blank=True, null=True)

    def __str__(self):
        return u'%s' % self.name


class Drink(models.Model):
    name = models.CharField(max_length=50, verbose_name='Напиток')
    quality = models.ForeignKey('Quality', on_delete=models.PROTECT, related_name='drink')
    classification = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return u'%s' % self.name
