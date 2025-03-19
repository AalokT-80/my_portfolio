from django.shortcuts import render
from .models import Project, Skill, Certification, BlogPost, Resume
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages


def home(request):
    selected_category = request.GET.get('category')
    selected_source = request.GET.get('source')

    if selected_category:
        projects = Project.objects.filter(category=selected_category).order_by('-created_at')
    else:
        projects = Project.objects.all().order_by('-created_at')

    skills = Skill.objects.all().order_by('category')

    certifications = Certification.objects.all().order_by('-issue_date')
    if selected_source:
        certifications = certifications.filter(source=selected_source)

    blogs = BlogPost.objects.all().order_by('-created_at')
    categories = Project.CATEGORY_CHOICES
    sources = Certification.SOURCE_CHOICES

    resume = Resume.objects.last()

    # Contact Form Logic (unchanged)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_mail(
                subject=f"New Contact Message from {contact.name}",
                message=f"Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}",
                from_email='tiwariaalok.2004@gmail.com',
                recipient_list=['tiwariaalok.2004@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!")
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'projects': projects,
        'skills': skills,
        'certifications': certifications,
        'blogs': blogs,
        'categories': categories,
        'sources': sources,
        'selected_category': selected_category,
        'selected_source': selected_source,
        'form': form,
        'resume': resume
    }
    return render(request, 'portfolio/home.html', context)
