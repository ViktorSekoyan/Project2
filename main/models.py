from django.db import models
from django.utils import timezone
# Create your models here.

class Subscribe(models.Model):
    email2 = models.EmailField()
    created_at = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return 'Subscribe'
    
class headericon(models.Model):
    appletouchicon = models.ImageField(upload_to='headericon/')
    shortcuticon = models.ImageField(upload_to='headericon/')

    def __str__(self):
        return 'headericon'
    
class Categoriesofthemonth(models.Model):
    img = models.ImageField(upload_to='categoriesofthemonth/')
    img1 = models.ImageField(upload_to='categoriesofthemonth/')
    img2 = models.ImageField(upload_to='categoriesofthemonth/')
    text1 = models.TextField(max_length=200, default='a')
    text2 = models.TextField(max_length=200, default='a')
    subtitle = models.CharField(max_length=75, default='a')    
    subtitle1 = models.CharField(max_length=75, default='a')
    subtitle2 = models.CharField(max_length=75, default='a')
    title = models.CharField(max_length=75, default='a')    
    title1 = models.CharField(max_length=75, default='a')
    title2 = models.CharField(max_length=75, default='a')

    def __str__(self):
        return 'Categoriesofthemonth'
    
class Categoryandfeature(models.Model):
    cat_img1 = models.ImageField(upload_to='categoryandfeature/')
    cat_img2 = models.ImageField(upload_to='categoryandfeature/')
    cat_img3 = models.ImageField(upload_to='categoryandfeature/')
    cat_text1 = models.CharField(max_length=50)
    cat_text2 = models.CharField(max_length=50)
    cat_text3 = models.CharField(max_length=50)
    fea_img1 = models.ImageField(upload_to='categoryandfeature/')
    fea_img2 = models.ImageField(upload_to='categoryandfeature/')
    fea_img3 = models.ImageField(upload_to='categoryandfeature/')
    fea_text1 = models.CharField(max_length=50)
    fea_text2 = models.CharField(max_length=50)
    fea_text3 = models.CharField(max_length=50)
    fea_number1 = models.IntegerField()
    fea_number2 = models.IntegerField()
    fea_number3 = models.IntegerField()

    def __str__(self):
        return 'Categoryandfeature'
    
class heroandbrand(models.Model):
    hero_img = models.ImageField(upload_to='heroandbrand/')
    brand_img1 = models.ImageField(upload_to='heroandbrand/')
    brand_img2 = models.ImageField(upload_to='heroandbrand/')
    brand_img3 = models.ImageField(upload_to='heroandbrand/')
    brand_img4 = models.ImageField(upload_to='heroandbrand/')
    brand_img5 = models.ImageField(upload_to='heroandbrand/')
    brand_img6 = models.ImageField(upload_to='heroandbrand/')
    brand_img7 = models.ImageField(upload_to='heroandbrand/')
    brand_img8 = models.ImageField(upload_to='heroandbrand/')
    brand_img9 = models.ImageField(upload_to='heroandbrand/')
    brand_img10 = models.ImageField(upload_to='heroandbrand/')
    brand_img11 = models.ImageField(upload_to='heroandbrand/')
    brand_img12 = models.ImageField(upload_to='heroandbrand/')

    def __str__(self):
        return 'heroandbrand'

class Shopsinglehtml(models.Model):
    product_img1 =  models.ImageField(upload_to='shopsingleimages/')
    product_img2 =  models.ImageField(upload_to='shopsingleimages/')
    product_img3 =  models.ImageField(upload_to='shopsingleimages/')
    product_img4 =  models.ImageField(upload_to='shopsingleimages/')
    product_img5 =  models.ImageField(upload_to='shopsingleimages/')
    product_img6 =  models.ImageField(upload_to='shopsingleimages/')
    product_img7 =  models.ImageField(upload_to='shopsingleimages/')
    product_img8 =  models.ImageField(upload_to='shopsingleimages/')
    product_img9 =  models.ImageField(upload_to='shopsingleimages/')
    product_img10 =  models.ImageField(upload_to='shopsingleimages/')
    shop_img1 = models.ImageField(upload_to='shopsingleimage/')
    shop_img2 = models.ImageField(upload_to='shopsingleimage/')
    shop_img3 = models.ImageField(upload_to='shopsingleimage/')
    shop_img4 = models.ImageField(upload_to='shopsingleimage/')
    shop_img5 = models.ImageField(upload_to='shopsingleimage/')
    shop_img6 = models.ImageField(upload_to='shopsingleimage/')
    shop_img7 = models.ImageField(upload_to='shopsingleimage/')
    shop_img8 = models.ImageField(upload_to='shopsingleimage/')
    shop_img9 = models.ImageField(upload_to='shopsingleimage/')
    shop_img10 = models.ImageField(upload_to='shopsingleimage/')
    shop_img11 = models.ImageField(upload_to='shopsingleimage/')
    shop_img12 = models.ImageField(upload_to='shopsingleimage/')

    def __str__(self):
        return 'Shopsingle'
    
class Shophtml(models.Model):
    shop_img1 = models.ImageField(upload_to='shopimages/')
    shop_img2 = models.ImageField(upload_to='shopimages/')
    shop_img3 = models.ImageField(upload_to='shopimages/')
    shop_img4 = models.ImageField(upload_to='shopimages/')
    shop_img5 = models.ImageField(upload_to='shopimages/')
    shop_img6 = models.ImageField(upload_to='shopimages/')
    shop_img7 = models.ImageField(upload_to='shopimages/')
    shop_img8 = models.ImageField(upload_to='shopimages/')
    shop_img9 = models.ImageField(upload_to='shopimages/')
    brand_img1 = models.ImageField(upload_to='shopimages/')
    brand_img2 = models.ImageField(upload_to='shopimages/')
    brand_img3 = models.ImageField(upload_to='shopimages/')
    brand_img4 = models.ImageField(upload_to='shopimages/')
    brand_img5 = models.ImageField(upload_to='shopimages/')
    brand_img6 = models.ImageField(upload_to='shopimages/')
    brand_img7 = models.ImageField(upload_to='shopimages/')
    brand_img8 = models.ImageField(upload_to='shopimages/')
    brand_img9 = models.ImageField(upload_to='shopimages/')
    brand_img10 = models.ImageField(upload_to='shopimages/')
    brand_img11 = models.ImageField(upload_to='shopimages/')
    brand_img12 = models.ImageField(upload_to='shopimages/')

    def __str__(self):
        return 'Shophtml'
    
class Letstalk(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(default=timezone.localtime)

    def __str__(self):
        return 'Letstalk'