from django.contrib import admin
from .models import Education,Experiance
# Register your models here.
def push_live(modeladmin, request, queryset):
    rows_updated = queryset.update(is_active=True)
    if rows_updated == 1:
        message_bit = "1 deck was"
    else:
        message_bit = "%s decks were" % rows_updated
    modeladmin.message_user(request, "%s successfully marked as active." % message_bit)

push_live.short_description = "Mark selected Decks as active"

class EducationAdmin(admin.ModelAdmin):
    pass

class ExperianceAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Education, EducationAdmin)
admin.site.register(Experiance, ExperianceAdmin)
