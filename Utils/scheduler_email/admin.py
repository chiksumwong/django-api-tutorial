from django.contrib import admin
from scheduler_email.models import EmailTask, EmailCheckExpiredTime


class ReadOnlyAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields] + \
            [field.name for field in obj._meta.many_to_many]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class EmailTaskDisplay(ReadOnlyAdmin):
    list_display = ('id', 'status', 'result', 'start_at', 'created_at')
    fields = ('id', 'status', 'result', 'start_at', 'created_at')
    search_fields = ['created_at', 'status']
    ordering = ['created_at']


class EmailCheckExpiredTimeDisplay(ReadOnlyAdmin):
    list_display = ('id', 'time')
    search_fields = ['id']
    ordering = ('id', 'time')


admin.site.register(EmailTask, EmailTaskDisplay)
admin.site.register(EmailCheckExpiredTime, EmailCheckExpiredTimeDisplay)