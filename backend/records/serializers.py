from rest_framework import serializers
from records.models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['id', 'start_time', 'record_type', 'duration', 'comments']
