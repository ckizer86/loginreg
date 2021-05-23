from django.db import models
from time import gmtime, localtime, strftime
from datetime import date, datetime
import re

# Create your models here.

class UserManager(models.Manager):
    def uservalidation(self, postData):
        errors = {}
        all_users = User.objects.all()
        dob = postData['dob']
        today = str(date.today())
        comptoday = date.today()
        year = comptoday.year - 13
        month = '{:02d}'.format(comptoday.month)
        day = '{:02d}'.format(comptoday.day)
        age = f"{year}-{month}-{day}"
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be more than two characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be more than two characters"
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must contain at least eight characters"
        if postData['pw'] != postData['confirm_pw']:
            errors['pw'] = "Passwords do not match"
        if postData['dob'] == "":
            errors['dob3'] = "You must enter a date of birth"
        name_regex = re.compile(r'^[a-zA-Z]')
        if not name_regex.match(postData['first_name']):
            errors['first_name2'] = "First name can only contain letters"
        if not name_regex.match(postData['last_name']):
            errors['last_name2'] = "Last name can only contain letters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address"
        for user in all_users:
            if postData['email'] == user.email:
                errors['email'] = "Email already exists"
        if postData['dob'] > str(today):
            errors['dob'] = "Date of Birth must be in the past"
        if dob > age:
            errors['dob2'] = "Must be 13 years or older"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pw = models.CharField(max_length=255)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()