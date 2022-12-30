import json

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required



from .models import Post,PostItem,AnalyzingPeople
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
    page = data["page"]
    Post.objects.create(title=title,desc=desc,page=page)
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
    return JsonResponse({"message": "post item saved successfully."})


@login_required
def completed(request):
    if request.method != "PUT":
        return JsonResponse({"error": "Put request required."})
    data = json.loads(request.body)
    postItemId = data["postItemId"]
    postItem = PostItem.objects.get(id=postItemId)
    postItem.completed = True
    postItem.save()
    return JsonResponse({"message":"postItem marked completed successfully."})


def analyzingPeople(request):
    people = AnalyzingPeople.objects.get(user=request.user).all()
    return render(request,"deepdive/analyzingPeople.html",{
        "people":people,
    })


@login_required
def add_analysis(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required."})
    data = json.loads(request.body)
    person = data["person"]
    openness = data["openness"]
    conscientiousness = data["conscientiousness"]
    extroversion = data["extroversion"]
    agreeableness = data["agreeableness"]
    neuroticism = data["neuroticism"]
    values = data["values"]
    passions = data["passions"]
    similarities = data["similarities"]
    importance = data["importance"]
    darkside = data["darkside"]
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
    return JsonResponse({"message": "post item saved successfully."})