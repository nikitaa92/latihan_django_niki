from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_waitress = models.BooleanField(default = False)
    is_cashier = models.BooleanField(default = False)

    def __str__(self):
        return f'{self.username}, {self.first_name}, {self.last_name}'
    
class TableResto (models.Model):
    status_choices = (
        ('Aktif', 'Aktif'),
        ('Tidak Aktif', 'Tidak Aktif'),
    )
    status_table_choices = (
        ('Kosong', 'Kosong'),
        ('Terisi', 'Terisi'),
    )
    code = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    capacity = models.IntegerField(default = 0)
    table_status = models.CharField(max_length = 15, choices = status_table_choices, default = 'Kosong')
    status = models.CharField(max_length = 15, choices = status_choices, default = 'Aktif')
    user_create = models.ForeignKey(User, related_name = 'user_create_table_resto', blank = True, null =True, on_delete = models.SET_NULL)
    user_update = models.ForeignKey(User, related_name = 'user_update_table_resto', blank = True, null =True, on_delete = models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name