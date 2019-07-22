from django.db import models


class AboutUsQuote(models.Model):
    content = models.CharField(null=True, max_length=100)


class AboutUs(models.Model):
    content = models.TextField(null=True, max_length=2000)


class AboutUsSectionOneHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class AboutUsSectionTwoHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class AboutUsSectionOne(models.Model):
    content = models.TextField(null=True, max_length=2000)


class AboutUsSectionTwo(models.Model):
    content = models.TextField(null=True, max_length=2000)


class ServiceOneHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceTwoHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceThreeHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceFourHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceFiveHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceSixHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceSevenHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)


class ServiceEightHeading(models.Model):
    heading = models.CharField(null=True, max_length=200)
