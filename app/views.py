from itertools import chain
import profile
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from sqlalchemy import null
from .models import Complain, Status, Comment, CommentByTeacher
from .forms import CreateComplainForm, StatusChangedForm
from profiles.models import Student, Teacher
from django.urls import reverse
from django.shortcuts import get_object_or_404


def getProfile(request):
    user = request.user
    profile = []
    student = True

    try:
        profile.append(Student.objects.filter(user=user)[0])

    except:
        try:
            profile.append(Teacher.objects.filter(user=user)[0])
            student = False
        except:
            pass

    if len(profile) == 0:
        profile.append("AnonymousUser")

    profile.append(student)

    return profile
# ========================================================


def getAllComplain(request):
    allData = Complain.objects.all()
    allStatus = Status.objects.all()
    profile = getProfile(request)

    allDataList = []
    allStatusList = []
    for data in allData:
        allDataList.append(data)

    for status in allStatus:
        allStatusList.append(status)

    datas = zip(allDataList, allStatusList)

    context = {
        'complains': datas,
        'profile': profile[0],
        'student': profile[1]

    }
    return render(request, 'newsfeed.html', context,)


# ========================================================


def getSingleComplain(request, pk, title):
    profile = getProfile(request)
    post = Complain.objects.get(id=pk)
    teachers = []
    students = []

    sugList = post.suggestions.split(',')

    allCommnets = post.comment_set.all()
    for i in allCommnets:
        students.append('s')

    allCommnetsByTeachers = post.commentbyteacher_set.all()
    for i in allCommnetsByTeachers:
        teachers.append('t')

    combinedComments = list(
        chain(zip(allCommnets, students), zip(allCommnetsByTeachers, teachers)))

    status = Status.objects.get(post=post)

    context = {
        'complain': post,
        'allCommnets': combinedComments,
        'status': status.type,
        'profile': profile[0],
        'student': profile[1],
        'suggestions': sugList,
    }
    return render(request, 'postDetails.html', context)

# ========================================================


def addComplain(request):
    form = CreateComplainForm()
    profile = getProfile(request)
    if profile[1] == False:
        return HttpResponse("You Must be a Student for add a complain")

    if request.method == 'POST':
        form = CreateComplainForm(request.POST)
        if form.is_valid:
            try:
                instance = form.save(commit=False)
                instance.author = profile[0]
                instance.save()
                return redirect('home')
            except:
                return HttpResponse("You Must be a Student for add a complain")
        else:
            return HttpResponse("Something Went Wrong")

    context = {
        "form": form
    }
    return render(request, "addComplain.html", context)

# ========================================================


def editPost(request, pk, title):

    profile = getProfile(request)
    post = Complain.objects.get(id=pk)
    if profile[0] != post.author:
        return HttpResponse("You Are Not Authorized")

    form = CreateComplainForm(instance=post)
    if request.method == "POST":
        form = CreateComplainForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('post-details', pk=pk, title=title)

    context = {
        'form': form,
        'complain': post
    }
    return render(request, 'editPost.html', context)


# ========================================================


def deletePost(request, pk, title):
    profile = getProfile(request)
    compalin = Complain.objects.get(id=pk)

    if profile[0] != compalin.author:
        return HttpResponse("You Are Not Authorized")

    if request.method == "POST":
        compalin = Complain.objects.get(id=pk)
        compalin.delete()
        return redirect('/')

    context = {
        'complain': compalin
    }
    return render(request, 'deletePost.html', context)
# ========================================================


def commentPost(request, pk):
    user = request.user
    profile = null
    student = True

    post = Complain.objects.get(id=pk)

    try:
        profile = Student.objects.filter(user=user)[0]

    except:
        try:
            profile = Teacher.objects.filter(user=user)[0]
            student = False

        except:
            pass

    if request.method == 'POST' and request.POST['commnet-box'] != null:
        if student:
            Comment.objects.create(user=profile, post=post,
                                   body=request.POST['commnet-box'])
            return redirect('post-details', pk=pk, title=post.title.replace(' ', '-'))

        if student == False:
            CommentByTeacher.objects.create(user=profile, post=post,
                                            body=request.POST['commnet-box'])

            return redirect('post-details', pk=pk, title=post.title.replace(' ', '-'))


# ========================================================


def deleteComment(request, pk, type, ck):
    profile = getProfile(request)
    post = Complain.objects.get(id=ck)

    if type == 's':
        comment = Comment.objects.get(id=pk)
        if comment.user == profile[0]:
            comment.delete()
            return redirect('post-details', pk=ck, title=post.title.replace(' ', '-'))

        else:
            return HttpResponse("You Are Not Authorized")

    else:
        comment = CommentByTeacher.objects.get(id=pk)
        if comment.user == profile[0]:
            comment.delete()
            return redirect('post-details', pk=ck, title=post.title.replace(' ', '-'))

        else:
            return HttpResponse("You Are Not Authorized")

# ========================================================


def likeSame(request):

    if request.method == 'POST':
        post = Complain.objects.get(id=request.POST['postID'])

        data = {
            'lvalue': 'Like',
            'svalue': 'Same Complain',


        }
        profiletype = request.POST['profileType']
        btnType = request.POST['btnType']

        if profiletype:
            profile = Student.objects.get(id=request.POST['profileID'])
        else:
            profile = Teacher.objects.get(id=request.POST['profileID'])

        if btnType == 'like-btn':
            if profile in post.liked.all():
                post.liked.remove(profile)

            else:
                post.liked.add(profile)
                data['lvalue'] = 'Unlike'

        if btnType == 'same-btn':
            if profile in post.same.all():
                post.same.remove(profile)
            else:
                post.same.add(profile)
                data['svalue'] = 'Remove Same Complain'

        return JsonResponse(data, safe=False)


def changeStatus(request, pk, ck, type):
    if type == "False":

        post = Complain.objects.get(id=pk)
        status = Status.objects.filter(post=post)[0]
        sForm = StatusChangedForm(instance=status)
        if request.method == 'POST':
            form = StatusChangedForm(request.POST, instance=status)
            if form.is_valid:
                form.save()
                return redirect('post-details', pk=pk, title=post.title.replace(' ', '-'))
        context = {
            "sForm": sForm,
            "pk": pk,
            "ck": ck,
            "type": type,
        }
        return render(request, "statusChanges.html", context)
    else:
        return HttpResponse("You are Not Authorized")
