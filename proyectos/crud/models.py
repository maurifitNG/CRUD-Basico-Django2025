from django.db import models

# Create your models here.

# Model for Task
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    
    
    # Clase Meta para ordenar las tareas por fecha de creación
    class Meta:
        ordering = ['-created']
        
    # Representación en cadena del objeto Task
    def __str__(self):
        return self.title
    