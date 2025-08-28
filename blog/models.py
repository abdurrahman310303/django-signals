from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


    def __str__(self):
        return self.title


class Notification(models.Model):

    message = models.TextField()
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.message



    
