from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
# Create your views here.

@csrf_exempt
@require_http_methods(['POST'])
def index(request):
    # retrieve message entered by user
    in_msg = request.POST['Body'].lower()
    
    # twilio xml response
    resp = MessagingResponse()
    msg = resp.message()

    responded = False
    if 'hello' in in_msg:
        responded = True
        response = """
        *Hi! I am the Crescendo Test!*

        Reply with START to get started with the test!
        """
        
    if 'start' in in_msg:
        responded = True
        response = "1. What is your date of birth? Please enter in DD/MM/YYYY."
    
    if not responded:
        response = "*Sorry! I am a bot and I don't understand your reply.*"

    msg.body(response)

    return HttpResponse(str(resp))

