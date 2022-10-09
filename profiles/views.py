from django.http import HttpResponse
from django.shortcuts import redirect, render
from sqlalchemy import null
from .models import Student, Teacher
from .forms import EditProfileForm, EditTeacherForm

# =============================================================


def myProfile(request):
    user = request.user
    student = True
    try:
        profile = Student.objects.filter(user=user)[0]

    except:
        profile = Teacher.objects.filter(user=user)[0]
        student = False

    context = {
        "profile": profile,
        "student": student
    }

    return render(request, "my-profile.html", context)


# =============================================================

def editMyProfile(request, pk):

    currentUser = request.user
    student = True


    try:
        profile = Student.objects.filter(user=currentUser)[0]
        id = profile.id
        editProfileForm = EditProfileForm(instance=profile)

        if request.method == "POST":
            form = EditProfileForm(
                request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('my-profile')

    except:
        try:
            profile = Teacher.objects.filter(user=currentUser)[0]
            id = profile.id
            student = False

            editProfileForm = EditTeacherForm(instance=profile)

            if request.method == "POST":
                form = EditTeacherForm(
                    request.POST, request.FILES, instance=profile)
                if form.is_valid():
                    form.save()
                    return redirect('my-profile')
        except:
            pass

    context = {
        "form": editProfileForm,
        'profileID': id,
        'student': student
    }

    if id == int(pk):
        return render(request, "editProfile.html", context)

    else:
        return HttpResponse("You Can't Edit Other's Profile")


# =============================================================

def getProfile(request,pk,type):
    student = True

    if type == 's':
        profile = Student.objects.get(id=pk)

    else:
        profile = Teacher.objects.get(id=pk)
        student = False
        
    context = {
        "profile": profile,
        "student": student
    }

    return render(request, "get-profile.html", context)


