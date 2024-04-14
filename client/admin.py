from django.contrib import admin
from .models import ClientUser, ClientRegistration, ClientPassword, ClientSetting, ClientLast, ClientExperience, ClientVerification, ClientMembership

@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    list_display  = ("id", "username", "firstname", "lastname")

@admin.register(ClientRegistration)
class ClientRegistrationAdmin(admin.ModelAdmin):
    list_display  = ("clientid", "accountdate")

@admin.register(ClientPassword)
class ClientPasswordAdmin(admin.ModelAdmin):
    list_display = ("clientid", "password", "passwordlevel", "passwordchangedate")

@admin.register(ClientSetting)
class ClientSettingAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientLast)
class ClientLastAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientExperience)
class ClientExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientVerification)
class ClientVerificationAdmin(admin.ModelAdmin):
    pass

@admin.register(ClientMembership)
class ClientMembershipAdmin(admin.ModelAdmin):
    pass