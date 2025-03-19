from django.contrib import admin
from .models import Skill, Project, Certification, BlogPost, ContactMessage, Resume

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Resume)
admin.site.register(BlogPost)
admin.site.register(ContactMessage)

from .models import Certification

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuing_org', 'source', 'issue_date')
    list_filter = ('source', 'issue_date')



