from django.db.models import Model
from django.db.models.fields import CharField, TextField, DateTimeField


# Create your models here.




class PostModel(Model):
    title = CharField(max_length=255)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
