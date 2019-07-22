from django.contrib import admin
from .models import AboutUsSectionTwo, AboutUsQuote, AboutUsSectionOne, AboutUsSectionTwoHeading, \
                    AboutUsSectionOneHeading, AboutUs

admin.site.register(AboutUs)
admin.site.register(AboutUsQuote)
admin.site.register(AboutUsSectionOneHeading)
admin.site.register(AboutUsSectionOne)
admin.site.register(AboutUsSectionTwo)
admin.site.register(AboutUsSectionTwoHeading)
