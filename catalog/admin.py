from django.contrib import admin

# Register your models here.
from catalog.models import Lecturer,College,LecturerFeedback,CollegeFeedback,Lrating,Crating
admin.site.register(Lecturer)
admin.site.register(LecturerFeedback)
admin.site.register(CollegeFeedback)
admin.site.register(Lrating)
admin.site.register(Crating)

# # Define the admin class
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = ('name','founder_name', 'date_of_est')


# # Register the admin class with the associated model
# admin.site.register(Company, CompanyAdmin)
# # Register the Admin classes for Book using the decorator
# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = ('title', 'company', 'display_skill')


# # Register the Admin classes for BookInstance using the decorator
# @admin.register(JobInstance)
# class JobInstanceAdmin(admin.ModelAdmin):
#     list_display = ('job','status','location','last_date','id')
#     list_filter = ('status', 'last_date')
@admin.register(College)
class JobInstanceAdmin(admin.ModelAdmin):
    list_filter = ('state', 'district')
    list_display = ('name','rating','district','state')
