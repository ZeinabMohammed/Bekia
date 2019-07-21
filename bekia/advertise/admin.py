from django.contrib import admin
from .models import Advertise


admin.site.register(Advertise)
# @admin.register(Advertise)
# class AdvertiseAdmin(admin.ModelAdmin, ExportCsvMixin):
#     change_list_template = "entities/advertise_changelist.html"
# def get_urls(self):
#     urls = super().get_urls()
#     my_urls = [
#         path('approve/', self.set_approved),

#     ]
#     return my_urls + urls

# def set_approved(self, request):
#     self.model.objects.all().update(is_approved=True)
#     self.message_user(request, "All Advertises are now approved")
#     return HttpResponseRedirect("../")