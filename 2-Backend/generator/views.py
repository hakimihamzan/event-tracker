from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
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


def generating(request):
    return render(request, 'generator/generating.html')

def generating2(request):
    output()
    return HttpResponseRedirect('/checkin')

# this function will run button is clicked
def output():
    # everytime this page is generated, qrcode is randomly generated and saved the pics
    # particpant with one unique generated is created
    randomLetters = string.ascii_letters
    randomNum = random.randint(1000000,9999999)
    result_str = ''.join(random.choice(randomLetters) for i in range(9))
    result_str_end = result_str+str(randomNum)
    global otp
    otp = result_str_end
    global unique
    unique = result_str_end
    qrpic = qrcode.make("OTP : "+otp)
    qrpic.save(os.path.join(BASE_DIR, "generator/qrcode.png"))
    participant = Participant(name="-", unique=unique, time='0',student_id=0, class_attended='-', lecturer='-', programme_code='-', faculty='-', campus='-', location='-')
    participant.save()


def generatedDone(request):
    participant_list = Participant.objects.all()
    #participant_list = Participant.objects.filter(unique=unique).exclude(student_id=0)
    context = {'participant_list': participant_list}
    return render(request, 'generator/generatedDone.html', context)
