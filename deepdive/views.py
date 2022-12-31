import json

from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone



from .models import Post,PostItem,AnalyzingPeople,Journal

#available categories of posts
post = ['home','ideal','improvement','activity']

def index(request):
    posts = Post.objects.all()
    return render(request,"deepdive/index.html",{
        "posts" : posts,
    })


@login_required
def create_post(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."})
    data = json.loads(request.body)
    title = data["title"]
    desc = data["desc"]
    image = data["image"]
    page = data["page"]
    Post.objects.create(title=title,desc=desc,page=page,image=image)
    return JsonResponse({"message": "post created successfully."})


@login_required
def add_item(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."})
    data = json.loads(request.body)
    content = data["content"]
    post = data["post"]
    postItem = PostItem.objects.create(user=request.user,content=content)
    post = Post.objects.get(id=post)
    post.item.add(postItem)
    post.save()
    id = postItem.id
    return JsonResponse({"message": "post item saved successfully.","id":id})


@login_required
def completed(request):
    if request.method != "PUT":
        return JsonResponse({"error": "Put request required."})
    data = json.loads(request.body)
    postItemId = data["postItemId"]
    postItemId = int(postItemId)
    postItem = PostItem.objects.get(id=postItemId)
    postItem.completed = True
    postItem.save()
    return JsonResponse({"message":"postItem marked completed successfully."})


def analyzingPeople(request):
    people = AnalyzingPeople.objects.filter(user=request.user).all()
    return render(request,"deepdive/analyzingPeople.html",{
        "people":people,
    })


@login_required
def add_analysis(request):
    if request.method != "POST":
        return HttpResponse({"error": "POST request required."})

    person = request.POST["person"]
    openness = request.POST["openness"]
    conscientiousness = request.POST["conscientiousness"]
    extroversion = request.POST["extroversion"]
    agreeableness = request.POST["agreeableness"]
    neuroticism = request.POST["neuroticism"]
    values = request.POST["values"]
    passions = request.POST["passions"]
    similarities = request.POST["similarities"]
    importance = request.POST["importance"]
    darkside = request.POST["darkside"]
    AnalyzingPeople.objects.create(
        user=request.user,
        person=person,
        openness=openness,
        conscientiousness=conscientiousness,
        extroversion=extroversion,
        agreeableness=agreeableness,
        neuroticism=neuroticism,
        values=values,
        passions=passions,
        similarities=similarities,
        importance=importance,
        darkside=darkside,
        )
    return redirect(reverse('analyzingPeople'))


def journal(request):
    journals = Journal.objects.filter(user=request.user).all()
    return render(request,'deepdive/journal.html',{
        'journals':journals
    })


@login_required
def add_journal(request):
    if request.method != "POST":
        return HttpResponse("Post request is required.")
    
    highlights = request.POST['highlights']
    lowlights = request.POST['lowlights']
    knowledge = request.POST['knowledge']
    emotions = request.POST['emotions']
    other = request.POST['other']
    rating = request.POST['rating']
    Journal.objects.create(
        user=request.user,
        highlights=highlights,
        lowlights=lowlights,
        emotions=emotions,
        knowledge=knowledge,
        other=other,
        rating=rating
        )
    return redirect(reverse('journal'))