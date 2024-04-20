from django.contrib import admin
from .models import ClientUser, ClientPassword, ClientSetting, ClientLast

@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display  = (
        "id_custom",
        "username",
        "date_joined"
        )

@admin.register(ClientPassword)
class ClientPasswordAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "password",
        "pub_date"
        )

@admin.register(ClientSetting)
class ClientSettingAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "mode",
        )

@admin.register(ClientLast)
class ClientLastAdmin(admin.ModelAdmin):
    list_display = (
        "client_id",
        "language",
        "platform",
        "agent",
        "ip",
        "last_login"
        )