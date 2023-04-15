from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

# Create your models here.

class books(models.Model):
    course_name=models.TextField(max_length=100)
    book_name=models.TextField(max_length=100)
    book_code=models.TextField(max_length=100,null=True)
    auther=models.TextField(max_length=300,null=True)
    semester=models.TextField(max_length=100)
    eng_branch=models.TextField(max_length=100)
    price=models.IntegerField(default=550,null=True,blank=True)

    def __str__(self):
        return self.course_name
    
class courses(models.Model):
    course_name=models.CharField(max_length=100)

    def __str__(self):
        return self.course_name
    
class course_offer_university(models.Model):
    university_name=models.CharField(max_length=100)
    course_offered=models.ManyToManyField(courses,related_name='courses')


class userdata(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    address=models.TextField(max_length=300) 
    phone = models.CharField(max_length=12)



class usercart(models.Model):
      uuid=models.UUIDField(primary_key=True,default = uuid.uuid4,editable=False)
      user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
      book_name=models.CharField(max_length=300,null=True,blank=True)
      bundle_name=models.CharField(max_length=300,null=True,blank=True)
      quantity=models.IntegerField(1) 
      price=models.IntegerField()
      order_status=models.BooleanField(default=False)
      payment_status=models.BooleanField(default=False)
      cancel_order=models.BooleanField(default=False)
      sub_total=models.PositiveSmallIntegerField(default=0,blank=True,null=True)


class bundlecart(models.Model):
      uuid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
      user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bundlecart')
      bundle_name=models.ManyToManyField(books,related_name='bundle')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		userdata.objects.create(user=instance) and bundlecart.objects.create(user=instance)
                
		print('Profile created!')
    
post_save.connect(create_profile, sender=User)

@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
	
	if created == False:
		instance.userdata.save() and instance.bundlecart.save()
                
		print('Profile updated!')

post_save.connect(update_profile, sender=User)



