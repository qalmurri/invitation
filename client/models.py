from django.db import models
from datetime import datetime
import uuid

def custom_id():
    uuid_string = str(uuid.uuid4()).split("-")[0]
    custom_id = f"{datetime.now().strftime('%Y%m%d%H%M%S')}{uuid_string[:4]}"
    return custom_id

class ClientUser(models.Model):
    id_custom = models.CharField(
        max_length=8,
        primary_key=True,
        default=custom_id)
    username = models.CharField(
        max_length=255
        )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        null=True
        )
    
    def __str__(self):
        return f"{self.id_custom}, {self.username}, {self.date_joined}"

class ClientPassword(models.Model):
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.CASCADE
        )
    password = models.CharField(
        max_length=255,
        null=True
        )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        null=True
        )

    def __str__(self):
        return f"{self.client}, {self.password}, {self.pub_date}"

class ClientSetting(models.Model):
    client = models.OneToOneField(
        ClientUser,
        on_delete=models.CASCADE,
        primary_key=True)
    mode = models.IntegerField(
        blank=True)

    def __str__(self):
        return f"{self.client}, {self.mode}"

class ClientLast(models.Model):
    client = models.ForeignKey(
        ClientUser,
        on_delete=models.CASCADE
        )
    language = models.CharField(
        max_length=255,
        blank=True
        )
    platform = models.CharField(
        max_length=255,
        blank=True
        )
    agent = models.CharField(
        max_length=255,
        blank=True
        )
    ip = models.CharField(
        max_length=255,
        blank=True
        )
    last_login = models.DateTimeField(
        auto_now_add=True,
        null=True)

    def __str__(self):
        return f"{self.client}, {self.language}, {self.platform}, {self.agent}, {self.ip}, {self.last_login}"