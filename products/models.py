from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
  
class Product(models.Model):
    # product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6,  decimal_places=2)
    description = models.TextField()
    inventory = models.IntegerField()
    
    def __str__(self):
        return self.name

class Image(models.Model):
    product = models.ForeignKey(Product,  related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.product} - {self.image}"