from django.shortcuts import get_object_or_404, redirect, render
from .models import Track

def alltracks(request):
    tracks = Track.objects.all().order_by("id")
    return render(request, "tracks/list.html", {"tracks": tracks})

def gettrack(request, id):
    track = get_object_or_404(Track, id=id)
    return render(request, "tracks/gettrack.html", {"track": track})

def createtrack(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            Track.objects.create(name=name)
            return redirect("alltracks")
    return render(request, "tracks/create.html")

def updatetrack(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        if name:
            track.name = name
            track.save()
            return redirect("alltracks")
    return render(request, "tracks/update.html", {"track": track})

def deletetrack(request, id):
    track = get_object_or_404(Track, id=id)
    if request.method == "POST":
        track.delete()
        return redirect("alltracks")
    return render(request, "tracks/delete.html", {"track": track})
