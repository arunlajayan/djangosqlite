from rest_framework import serializers
from countries.models import Countries


class CountriesSerializer(serializers.ModelSerializer):
    class meta:
        model = Countries
        fields = ("id", "name", "capital")
