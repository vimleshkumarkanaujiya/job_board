from django.shortcuts import render

from .models import JobPosting


def index(request):
    active_postings = JobPosting.objects.filter(is_active=True)
    return render(request, 'job_board/index.html', {'job_posting': active_postings})
