from django.db import models

# -------------------------------
# Skill Model
# -------------------------------
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Data Analysis', 'Data Analysis'),
        ('Machine Learning', 'Machine Learning'),
        ('Visualization', 'Visualization'),
        ('Django', 'Django'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name

# -------------------------------
# Project Model
# -------------------------------
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('Data Analysis', 'Data Analysis'),
        ('Machine Learning', 'Machine Learning'),
        ('Visualization', 'Visualization'),
        ('Django', 'Django'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    demo_image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# -------------------------------
# Certification Model
# -------------------------------
# class Certification(models.Model):

#     CATEGORY_CHOICES = [
#         ('Google Data Analytics', 'Google Data Analytics'),
#         ('Infosys Springboard', 'Infosys Springboard'),
#         ('AI', 'Visualization'),
#         ('Django', 'Django'),
#     ]
#     name = models.CharField(max_length=200)
#     issuing_org = models.CharField(max_length=100)
#     issue_date = models.DateField()
#     certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
#     certificate_link = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.name} by {self.issuing_org}"



# class Certification(models.Model):
#     PLATFORM_CHOICES = [
#         ('GOOGLE', 'Google'),
#         ('INFOSYS', 'Infosys Springboard'),
#         ('MICROSOFT', 'Microsoft Azure'),
#         ('OTHER', 'Other'),
#     ]

#     name = models.CharField(max_length=200)
#     issuing_org = models.CharField(max_length=100)
#     issue_date = models.DateField()
#     certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
#     certificate_link = models.URLField(blank=True, null=True)
#     platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default='OTHER')

#     def __str__(self):
#         return f"{self.name} by {self.issuing_org}"


class Certification(models.Model):
    GOOGLE = 'Google'
    INFOSYS = 'Infosys Springboard'
    MICROSOFT = 'Microsoft Azure'
    OTHER = 'Other'

    SOURCE_CHOICES = [
        (GOOGLE, 'Google'),
        (INFOSYS, 'Infosys Springboard'),
        (MICROSOFT, 'Microsoft Azure'),
        (OTHER, 'Other')
    ]

    name = models.CharField(max_length=200)
    issuing_org = models.CharField(max_length=100)
    source = models.CharField(max_length=50, choices=SOURCE_CHOICES, default=OTHER)
    issue_date = models.DateField()
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    certificate_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} by {self.issuing_org}"


# -------------------------------
# BlogPost Model (Optional)
# -------------------------------
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} ({self.email})"


from django.db import models

class Resume(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resumes/')  # Make sure 'file' field is used!
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
