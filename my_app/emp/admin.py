from django.contrib import admin
from .models import Emp,Testimonial

class EmpAdmin(admin.ModelAdmin):
    list_display =('name','emp_id','phone','address','department','working')
    list_editable = ('working','emp_id')
    search_fields = ('name',)
    list_filter = ('working',)  
    
     
admin.site.register(Emp,EmpAdmin)
admin.site.register(Testimonial)

# Register your models here.
