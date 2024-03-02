from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from hr.models import JobPost, CandidateApplications, Hr
from candidate.models import MyApplyJobList

# Create your views here.
@login_required
def candidate_dashboard(request):
    jobs = JobPost.objects.all()
    return render(request, 'candidate/dash.html', {'jobs': jobs}) 

@login_required
def myJobListviews(request):
    if Hr.objects.filter(user=request.user).exists():
        return redirect('hrdash')
    joblist = MyApplyJobList.objects.filter(user=request.user)
    return render(request, 'candidate/myjoblist.html', {'joblist':joblist}) 
    
@login_required
def applyforjob(request,pk):
    if JobPost.objects.filter(id=pk).exists():
        job = JobPost.objects.get(id=pk)
        if CandidateApplications.objects.filter(user=request.user,job=job).exists():
            return redirect('candidate_dashboard')
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            college = request.POST.get('college')
            passing_year = request.POST.get('passing_year')
            yearOfExperience = request.POST.get('yearOfExperience')
            resume = request.FILES.get('resume')
            #job = JobPost.objects.get(id=pk)
            candidate_application = CandidateApplications(user=request.user,job=job,passingYear=passing_year,yearOfExperience=yearOfExperience,resume=resume)
            candidate_application.save()
            MyApplyJobList(user=request.user, job=candidate_application).save()
            job.applyCount += 1
            job.save()
            return redirect('candidate_dashboard')
        return render(request,'candidate/apply.html')
    return redirect('candidate_dashboard')