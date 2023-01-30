from django.db import models
    
class Game(models.Model):
    class Meta:
        db_table = 'game'
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, default=None)