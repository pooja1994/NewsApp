from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account


@admin.action(description='Block user')
def block_user(modeladmin, request, queryset):
    queryset.update(is_active=False)


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_active', 'is_admin', 'keywords')
    search_fields = ('email', 'username',)
    # readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    actions = [block_user]


admin.site.register(Account, AccountAdmin)
