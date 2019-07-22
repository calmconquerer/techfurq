from django.db import models


class AboutUsQuote(models.Model):
    content = models.TextField(null=True, blank=True, max_length=100)


class AboutUs(models.Model):
    content = models.TextField(null=True, blank=True, max_length=2000)


class AboutUsSectionOneHeading(models.Model):
    content = models.TextField(null=True, blank=True, max_length=200)


class AboutUsSectionTwoHeading(models.Model):
    content = models.TextField(null=True, blank=True, max_length=200)


class AboutUsSectionOne(models.Model):
    content = models.TextField(null=True, blank=True, max_length=2000)


class AboutUsSectionTwo(models.Model):
    content = models.TextField(null=True, blank=True, max_length=2000)