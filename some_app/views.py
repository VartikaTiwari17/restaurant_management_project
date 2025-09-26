from django.http import JsonResponse
from utils.validation_utils import is valid_email


def submit_email(request):
    email = request.POST.get('email')
    if not is_valid_email(email):
          return JsonResponse({"error" "Invalid email"}, status=400)
          return JsonResponse({"success": "Email is valid"})