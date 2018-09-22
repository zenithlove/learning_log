from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=50)
    add_time = models.DateTimeField(auto_now_add = True,null=True)
    comment = models.CharField(max_length=30,  null=True)
    owner = models.ForeignKey (User,on_delete = models.CASCADE)
    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"
        db_table ="topics"
    
    def __str__(self):
        #help()
        return self.text
        
        
        
        
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    time_added = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        db_table ="entry"
    def __str__(self):
        #help()
        return self.text        