from rest_framework import serializers
from .models import Participant

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ('id', 'name', 'student_id', 'programme_code', 'faculty', 'campus', 'location', 'time', 'class_attended', 'lecturer', 'unique')
