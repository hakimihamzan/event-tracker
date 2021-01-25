from django.http import HttpResponseRedirect
from django.shortcuts import render
import random
import qrcode
import string
import os
from pathlib import Path
# rest framework
from rest_framework import viewsets
from .serializers import ParticipantSerializer
from .models import Participant

BASE_DIR = Path(__file__).resolve().parent.parent

unique = 12
otp = "0"


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all().order_by('id')
    serializer_class = ParticipantSerializer


def generating(request):
    return render(request, 'generator/generating.html')


def generating2(request):
    output()
    return HttpResponseRedirect('/checkin')


# this function will run button is clicked
def output():
    # everytime this page is generated, qrcode is randomly generated and saved the pics
    # particpant with one unique generated is created
    random_letters = string.ascii_letters
    random_num = random.randint(1000000, 9999999)
    result_str = ''.join(random.choice(random_letters) for i in range(9))
    result_str_end = result_str + str(random_num)
    global otp
    otp = result_str_end
    global unique
    unique = result_str_end
    qrpic = qrcode.make("OTP : " + otp)
    # qrpic.save(os.path.join(BASE_DIR, "generator/qrcode.png"))
    qrpic.save(os.path.join(os.path.dirname(BASE_DIR), 'eventrackers/mediafiles_cdn/qrpic.png'))

    participant = Participant(name="-", unique=unique, time='0', student_id=0, class_attended='-', lecturer='-',
                              programme_code='-', faculty='-', campus='-', location='-')
    participant.save()


def generatedDone(request):
    # participant_list = Participant.objects.all()
    # # participant_list = Participant.objects.filter(unique=unique).exclude(student_id=0)
    # context = {'participant_list': participant_list}
    return render(request, 'generator/generatedDone.html')


def get_more_tables(request):
    participant_list = Participant.objects.filter(unique=unique).exclude(student_id=0)
    context = {'participant_list': participant_list}
    return render(request, 'generator/get_more_tables.html', context)
