from django.contrib import admin
from .models import Customer, Comment


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'person_name', 'company_name')
    search_fields = ('person_name', 'company_name', 'exibition')
    list_filter = ('company_name', 'exibition')
    date_hierarchy = 'action_date'


class CommentAdmin(admin.ModelAdmin):
    list_filter = ('createdOn',)
    date_hierarchy = 'createdOn'
    ordering = ('-createdOn',)
    raw_id_fields = ['customer']


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Comment, CommentAdmin)
