from django.db import models

class ClientUser(models.Model):
    username = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.username}, {self.firstname}, {self.lastname}"

class ClientRegistration(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)
    accountdate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.accountdate}"

class ClientPassword(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)
    password = models.CharField(max_length=255, null=True)
    passwordlevel = models.CharField(max_length=255, null=True)
    passwordchangedate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.password}, {self.passwordlevel}, {self.passwordchangedate}"

class ClientSetting(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)
    mode = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.mode}"

class ClientLast(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)
    devicelogin = models.CharField(max_length=255)
    lastlogin = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.devicelogin}, {self.lastlogin}"

class ClientExperience(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)    
    experience = models.CharField(max_length=255)
    experiencelevel = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.experience}, {self.experiencelevel}"

class ClientVerification(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)
    verification = models.CharField(max_length=255)
    verificationdate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.verification}, {self.verificationdate}"

class ClientMembership(models.Model):
    clientid = models.OneToOneField(ClientUser, on_delete=models.CASCADE, primary_key=True)
    membership = models.CharField(max_length=255)
    membershipdate = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.membership}, {self.membershipdate}"