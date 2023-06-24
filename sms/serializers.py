from rest_framework import serializers
from .models import Type


class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=12)
    type = serializers.CharField(max_length=50)
    data = serializers.JSONField()

    def validate_phone(self, value):
        if str(value)[:3]!='998' and len(str(value))!='12':
            raise serializers.ValidationError("Phone must be like 998977366898")
        return value
    
    def validate_data(self, value):
        for val in value.values():
            if type(val)!=str:
                raise serializers.ValidationError("Values of data must be string!")
        return value


class TypeSerializer(serializers.ModelSerializer):
    text = serializers.SerializerMethodField("custom_text")
    class Meta:
        model = Type
        fields = 'text', 'type', 'keys'

    def custom_text(self, value):
        lan = self.context.get("lan")
        text_by_lan = value.text
        return text_by_lan.get(lan)
    