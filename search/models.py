from django.db import models
from administrator.models import User, Householder
# Create your models here.






# Toifalarni belgilash E'lonlarni yaratuvchi model
class Announcement(models.Model):
    
    # title0 = "Foydalanuvchi bilan o'zaro ko'pga bir modeli"
    user = models.ForeignKey(Householder, on_delete = models.CASCADE)
    
    # title2 = "Uy Sharaitlarini Eloktron shakillantirish qismlar"
    region = models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    phone_numer = models.CharField(max_length=20, verbose_name="Telefon raqam")
    mode = models.CharField(max_length=200)
    kimlar = models.CharField(max_length=200)
    kishilar = models.CharField(max_length=200)
    topshirilgan = models.CharField(max_length=200)
    moneyc = models.CharField(max_length=200)
    floor = models.CharField(max_length=200)

    floormany = models.CharField(max_length=200, blank=True)
    rooms = models.CharField(max_length=200)

    money = models.CharField(max_length=100, verbose_name="Pul muomilasini kiriting")
    tartiblar = models.TextField(verbose_name="Uyingizdagi tartiblarni kiriting")
    ish = models.TextField(verbose_name="Ijarachiga ish taklif qila olasizmi")
   


    # title2 = "Iste'mol ehtiyojlari"
    sovuq_suv = models.CharField(max_length=200)
    issiq_suv = models.CharField(max_length=200)
    svet = models.CharField(max_length=200)
    gaz = models.CharField(max_length=200)
    additional2 = models.TextField(verbose_name="Qo'shimcha kiriting")


    # title3 = "Elektron vositalari"
    wifi = models.CharField(max_length=200)
    sovutgich = models.CharField(max_length=200)
    kondisioner = models.CharField(max_length=200)
    additional3 = models.TextField(verbose_name="Qo'shimcha kiriting")


    # title4 = "Gigiyena sharaoidlar "
    hammom = models.CharField(max_length=200)
    additional4 = models.TextField(verbose_name="Qo'shimcha kiriting")


    # title5 = "Xavfsizlik tizimi" 
    xafsiz = models.CharField(max_length=200)
    additional5 = models.TextField(verbose_name="Qo'shimcha kiriting")
    likes = models.ManyToManyField(User, related_name='announcement_like', blank=True)
    geolocaion = models.CharField(max_length=500)

    def __str__(self):
        return self.address

    def num_likes(self):
        return self.likes.all().count()

    def get_absolute_url(self):
        return reverse('account', args=[str(self.id)])

    class Meta:
        verbose_name = "1. E'lonlar"
        verbose_name_plural = "1. E'lonlar"





# E'lon uchun bir yoki bir nechta suratlarni biriktish modeli
class Photo(models.Model):
    announcements = models.ForeignKey(Announcement, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    # def __str__(self):
    #     return self.announcements

    # class Meta:
    #     verbose_name = "2. E'lonlar suratlari"
    #     verbose_name_plural = "2. E'lonlar suratlari"


# Yordamchi Uy manzillarini eslatuvchi model
class Streets(models.Model):
    streets = models.CharField(max_length=500, verbose_name="Eslatmali qisqa manzilni kiriting")

    def __str__(self):
        return str(self.streets)
    

    class Meta:
        verbose_name = "4. Manzillarni eslatuvchi manzillar"
        verbose_name_plural = "4. Manzillarni eslatuvchi manzillar"



# Uy hovli joy yoki ko'p qavatli tanlashlar
class Rooms(models.Model):
    name = models.CharField(max_length=200, verbose_name="Honalar soni")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "3. Honalar soni"
        verbose_name_plural = "3. Honalar soni"



# Uy hovli joy yoki ko'p qavatli tanlashlar
class Floor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nechanchi qavat")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "3. Uy Nechanchi qavat tanlashlar"
        verbose_name_plural = "3. Uy Nechanchi qavat tanlashlar"
