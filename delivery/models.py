from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15,db_index=True,verbose_name='category name')
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        ordering = ['name']
        


class DeliveryModel(models.Model):
    title = models.CharField(max_length=20,verbose_name='title')
    description = models.TextField(verbose_name='description')
    price = models.FloatField(verbose_name='price')
    
    category = models.ForeignKey('Category',null=True,on_delete=models.PROTECT,verbose_name='category')
    
    datetime = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='date time')
    
    class Meta:
        verbose_name_plural = 'deliviries'
        verbose_name = 'delivery'
        ordering = ['-datetime']