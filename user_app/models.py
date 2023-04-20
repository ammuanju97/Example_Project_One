from django.db import models
from core.models import SignUpModel
# Create your models here.


class PostCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class AddPost(models.Model):
    user = models.ForeignKey(SignUpModel, on_delete=models.CASCADE)
    post_name = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(PostCategory,on_delete=models.CASCADE, related_name='products')
    # created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to ='uploads/')
    
    def __str__(self):
        return self.post_name