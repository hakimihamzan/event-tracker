from django.shortcuts import render, redirect
from rest_framework import viewsets
from .serializers import ParticipantSerializer
from .models import Participant
from django.views import View
import random
import qrcode
import string
import os

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


unique = 12
otp = "0"

class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('id')
    serializer_class = ParticipantSerializer

# use redirect because we re changing page
class generate(View) :
    def get(self, request):
        #msg = request.session.get('msg', False)
        #if ( msg ) : del(request.session['msg'])
        randomLetters = string.ascii_letters
        randomNum = random.randint(1000000,9999999)
        result_str = ''.join(random.choice(randomLetters) for i in range(9))
        result_str_end = result_str+str(randomNum)
        global otp
        otp = result_str_end
        global unique
        unique = result_str_end
        qrpic = qrcode.make("OTP : "+otp)
        qrpic.save(os.path.join(BASE_DIR, "static/qrcode.jpg"))
        participant = Participant(name="-", unique=unique, time='0',student_id=0, class_attended='-', lecturer='-', programme_code='-', faculty='-', campus='-', location='-')
        participant.save()
        return render(request, 'persona/generate.html')

    def post(self, request):
        # if there any flash messages
        
        #guess = request.POST.get('guess')
        #msg = checkguess(guess)
        #request.session['msg'] = msg
        return redirect(request.path)

# use redirect because we re changing page
class generating(View) :
    def get(self, request):
        #msg = request.session.get('msg', False)
        #if ( msg ) : del(request.session['msg'])
        participants = Participant.objects.filter(unique=unique).exclude(student_id=0)
        context = {'participants': participants}
        return render(request, 'persona/generating.html')

    def post(self, request):
        #guess = request.POST.get('guess')
        #msg = checkguess(guess)
        #request.session['msg'] = msg
        return redirect(request.path)


#  ----------------------------------------redirect adjusted

# def generateQr(request):
#     randomLetters = string.ascii_letters
#     randomNum = random.randint(1000000,9999999)
#     result_str = ''.join(random.choice(randomLetters) for i in range(9))
#     result_str_end = result_str+str(randomNum)
#     global otp
#     otp = result_str_end
#     global unique
#     unique = result_str_end
#     qrpic = qrcode.make("OTP : "+otp)
#     qrpic.save(os.path.join(BASE_DIR, "staticfiles/qrcode.jpg"))
#     participant = Participant(name="-", unique=unique, time='0',student_id=0, class_attended='-', lecturer='-', programme_code='-', faculty='-', campus='-', location='-')
#     participant.save()
#     return render(request, "persona/generate.html")
#     #return redirect(generateQr, "persona/generate.html")
#
# def generating(request):
#     participants = Participant.objects.filter(unique=unique).exclude(student_id=0)
#     context = {'participants': participants}
#     return render(request, "persona/generating.html", context)
#     #return redirect("persona/generating.html", context)


# ----------------------------------------old retry code

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
