from .models import Person
from rest_framework import serializers
class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields='__all__'