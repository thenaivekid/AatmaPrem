import json
import openai
import os
from dotenv import load_dotenv

load_dotenv()

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


from .util import scorePerson
from .models import Post,PostItem,AnalyzingPeople,Journal,ExternalLink

#available categories of posts
post = ['home','ideal','improvement','activity']

def index(request):
    posts = Post.objects.all()
    return render(request,"deepdive/index.html",{
        "posts" : posts,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "deepdive/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "deepdive/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def user(request):
    if request.user.is_authenticated:
        return render(request,"deepdive/user.html")
    return HttpResponseRedirect(reverse('register'))


def post_details(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,"deepdive/post.html",{
        "post":post
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
    Post.objects.create(title=title,desc=desc,page=page,image=image,slug=title)
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


@login_required
def analyzingPeople(request):
    people = AnalyzingPeople.objects.filter(user=request.user).all().order_by('-score')
    return render(request,"deepdive/analyzingPeople.html",{
        "people":people,
    })


@login_required
def add_analysis(request):
    if request.method != "POST":
        return HttpResponse({"error": "POST request required."})

    person = request.POST["person"]
    openness = int(request.POST["openness"])
    conscientiousness = int(request.POST["conscientiousness"])
    extroversion = int(request.POST["extroversion"])
    agreeableness = int(request.POST["agreeableness"])
    neuroticism = int(request.POST["neuroticism"])
    values = request.POST["values"]
    passions = request.POST["passions"]
    similarities = request.POST["similarities"]
    importance = request.POST["importance"]
    darkside = request.POST["darkside"]

    score = scorePerson(
        openness=openness,
        conscientiousness=conscientiousness,
        extroversion=extroversion,
        agreeableness=agreeableness,
        neuroticism=neuroticism,
        values=values,
        passions=passions,
        similarities=similarities,
        importance=importance,
        darkside=darkside 
    )

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
        score=score
        )
    return redirect(reverse('analyzingPeople'))


@login_required
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


def mindfulness(request):
    links = ExternalLink.objects.all()
    return render(request,"deepdive/mindfulness.html",{
        "links":links,
    })


@csrf_exempt
def create_image(request):
    print('hey pic')
    if request.method != 'POST':
        return JsonResponse({"message":"post request is required"})
    data = json.loads(request.body)
    query = data['query']
    print(query)
    n = 3
    openai.api_key = os.environ.get("OPEN_AI_API_KEY")
    response = openai.Image.create(
    prompt=query,
    n=n,
    size="256x256"
    )
    image_url = []
    for i in range(n):
        image_url.append(response['data'][i]['url'])

    return JsonResponse({"img0":image_url[0],"img1":image_url[1],"img2":image_url[2]})