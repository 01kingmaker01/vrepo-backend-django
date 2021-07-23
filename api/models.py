from djongo import models

# Create your models here.
class Post(models.Model):
    
    id = models.ObjectIdField(unique=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    committee = models.CharField(max_length=50)
    add_image = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    

    def __str__(self):
        return self.author