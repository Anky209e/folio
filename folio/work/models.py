from django.db import models
from info.models import Skill
# experience and projects model here

class Experience(models.Model):
    """
    Model Storing all work experience
    """
    company_name = models.CharField(max_length=150,null=False,blank=True)
    company_logo = models.FileField(upload_to='company_logos/',blank=True,null=True)
    post_name = models.CharField(max_length=150,blank=False,null=False)
    what_i_did = models.TextField(blank=True,null=True)
    skills_used = models.ManyToManyField(Skill)
    joining_date = models.DateField(null=True,blank=True)
    last_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.post_name) + "-"+ str(self.company_name)