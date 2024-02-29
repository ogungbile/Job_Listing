from django.shortcuts import render, redirect
from hr.models import JobPost , CandidateApplications , SelectCandidateJob, Hr
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def hrHome(request):
    jobpost= JobPost.objects.filter(user=request.user)
    if Hr.objects.filter(user=request.user).exists():
        jobpost= JobPost.objects.filter(user=request.user)
        return render(request,'hr/hrdashboard.html', {'jobpost':jobpost})
    return render(request,'hr/hrdashboard.html', {'jobpost':jobpost})
    #return redirect('hrdash')


@login_required
def postJobs(request):
    msg = None
    if request.method == 'POST':
        job_title = request.POST.get('job-title')
        address = request.POST.get('address')
        company_name = request.POST.get('company-name')
        salary_low = request.POST.get('salary-low')
        salary_high = request.POST.get('salary-high')
        last_date  = request.POST.get('last-date')

        jobpost = JobPost(user=request.user,title=job_title,address=address,compnayName=company_name,salaryLow=salary_low,salaryHigh=salary_high,lastDateToApply=last_date)
        jobpost.save()
        msg = "Job Upload Done.."
        return render(request,'hr/postjob.html',{'msg':msg})


    return render(request,'hr/postjob.html')

@login_required
def candidate_view(request, pk):
    return render(request,'hr/candidate.html')