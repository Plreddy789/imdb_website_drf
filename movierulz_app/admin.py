from django.contrib import admin

from movierulz_app.models import VideosList, StreamPlatform, Reviews

# Register your models here.
admin.site.register(VideosList)
admin.site.register(StreamPlatform)
admin.site.register(Reviews)