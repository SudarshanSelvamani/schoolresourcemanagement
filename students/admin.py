from django.contrib import admin
from .models import Student,Teacher,Student_map,home_room,Assignment,Semester1,Semester2,User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Teacher)
admin.site.register(home_room)
admin.site.register(Student_map)
admin.site.register(Assignment)
admin.site.register(Semester1)
admin.site.register(Semester2)
admin.site.register(User, UserAdmin)
admin.site.register(Student)


# admin.site.register()
# admin.site.register()

class StudentAdmin(admin.ModelAdmin):
    fields = ('Gender')

    radio_fields = {'Gender': admin.VERTICAL}