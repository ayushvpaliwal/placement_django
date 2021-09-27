from django.contrib import admin

from .models import algorithm, development, enquiry, language, placement

admin.site.register(algorithm)
admin.site.register(development)
admin.site.register(enquiry)
admin.site.register(language)
admin.site.register(placement)
