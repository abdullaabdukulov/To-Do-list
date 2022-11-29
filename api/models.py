from django.db import models
from django.conf import settings
from django.db.models import CharField

User = settings.AUTH_USER_MODEL


class Todo(models.Model):
    name = models.CharField(max_length=30, default="", blank=True, null=True, help_text='TODO name')
    image = models.ImageField(upload_to='todos/', height_field=None, width_field=None, max_length=200,
                              help_text='TODO image')
    desc = models.TextField("TODO description", default="", max_length=200, help_text="TODO description")
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'todo'
        managed = True
        verbose_name = 'TODO'
        verbose_name_plural = 'Todo'

    def __str__(self) -> CharField:
        return self.name
