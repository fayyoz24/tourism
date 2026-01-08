from django.http import JsonResponse
from django.http import HttpResponseForbidden
from apps.users.models import BlockedIP


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'User not logged in'}, status=401)
        
        response = self.get_response(request)
        return response


class BlockBlockedIPsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the client's IP address
        ip = self.get_client_ip(request)
        
        # Check if this IP is in the blocked IP list
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Your IP is blocked.")
        
        return self.get_response(request)

    def get_client_ip(self, request):
        # Get IP address from the request headers (may vary based on your setup)
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
