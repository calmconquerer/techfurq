from django.shortcuts import render
from .models import AboutUsQuote, AboutUs, AboutUsSectionOne, \
                    AboutUsSectionOneHeading, AboutUsSectionTwo, AboutUsSectionTwoHeading


def home(request):
    about_us_quotes = AboutUsQuote.objects.all()
    about_us = AboutUs.objects.all()
    about_us_section_one_heading = AboutUsSectionOneHeading.objects.all()
    about_us_section_two_heading = AboutUsSectionTwoHeading.objects.all()
    about_us_section_one = AboutUsSectionOne.objects.all()
    about_us_section_two = AboutUsSectionTwo.objects.all()
    return render(request, 'portfolio/index.html', {'about_us_quotes': about_us_quotes,
                                                    'about_us': about_us,
                                                    'about_us_section_one_heading': about_us_section_one_heading,
                                                    'about_us_section_two_heading': about_us_section_two_heading,
                                                    'about_us_section_one': about_us_section_one,
                                                    'about_us_section_two': about_us_section_two})
