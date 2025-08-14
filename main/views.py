from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.conf import settings
from .models import ShortURL
from django.views.decorators.http import require_POST

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")
        if name and url:
            ShortURL.objects.create(name=name, original_url=url)
        return redirect("home")

    short_urls = ShortURL.objects.all().order_by("-created_at")
    return render(request, "home.html", {"short_urls": short_urls, "base_url": settings.BASE_URL})

def redirect_url(request, code):
    short_url = get_object_or_404(ShortURL, short_code=code)
    return redirect(short_url.original_url)

def shorturl_details(request, pk):
    short_url = get_object_or_404(ShortURL, pk=pk)
    data = {
        "name": short_url.name,
        "original_url": short_url.original_url,
        "short_url": f"{settings.BASE_URL}/{short_url.short_code}",
        "qr_code": short_url.qr_code.url if short_url.qr_code else None
    }
    return JsonResponse(data)

@require_POST
def delete_shorturl(request, pk):
    shorturl = get_object_or_404(ShortURL, pk=pk)
    shorturl.delete()  # This also deletes the QR code file
    return JsonResponse({'status': 'success', 'message': 'ShortURL deleted'})