from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ParticipantSerializer
from .models import Participant
import random
import qrcode
import string


unique = 12
otp = "0"

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('unique')
    serializer_class = ParticipantSerializer

def generateQr(request):
    randomLetters = string.ascii_letters
    randomNum = random.randint(1000000,9999999)
    result_str = ''.join(random.choice(randomLetters) for i in range(9))
    result_str_end = result_str+str(randomNum)
    global otp
    otp = result_str_end
    global unique
    unique = result_str_end
    qrpic = qrcode.make("OTP : "+otp)
    qrpic.save(r"static/persona/qrcode.jpg")
    participant = Participant(name="-", unique=unique, student_id=0, class_attended='-', lecturer='-', programme_code='-', faculty='-', campus='-', location='-')
    participant.save()
    return render(request, "persona/generate.html")

def generating(request):
    participants = Participant.objects.filter(unique=unique).exclude(student_id=0)
    number = 0
    context = {'participants': participants, 'number': number}
    return render(request, "persona/generating.html", context)



#
# def index(request):
#     # participants = Participant.objects.filter(unique=12)
#     participants = Participant.objects.all()
#
#     context = {'participants': participants}
#     return render(request, 'persona/index.html', context)
#
# def deets(request):
#     participants = Participant.objects.filter(unique=unique)
#     #participants = Participant.objects.all()
#
#     context = {'participants': participants}
#     return render(request, 'persona/index.html', context)
