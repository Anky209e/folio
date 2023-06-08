from django.db import models


class Skill(models.Model):
    skill_name = models.CharField(blank=False,max_length=50)
    about = models.TextField(blank=True)
    icon = models.FileField(upload_to='skill_icons/',null=True,blank=True)

    def __str__(self):
        return str(self.skill_name)

class AboutMe(models.Model):
    name = models.CharField(blank=False,max_length=50)
    profile_image = models.FileField(upload_to='profile_images/',null=True,blank=True)
    who_am_i = models.TextField(blank=True,null=True)
    what_can_i_do = models.TextField(blank=True,null=True)
    skills = models.ManyToManyField(Skill)
    resume = models.FileField(upload_to='resume/',null=True,blank=True)
    hobbies = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.name)