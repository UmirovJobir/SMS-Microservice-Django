from django.conf import settings

from rest_framework import views, response, status

from .models import Type
from .service import send, multiple_replace
from .serializers import SmsSerializer, TypeSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


@extend_schema(
            summary="Send sms to users phone number.",
            description="Retrieves **product**, return 404 if not found",
            request=SmsSerializer,
            responses={
                200: SmsSerializer,
                400: OpenApiResponse(description="error: Keys must be ['PRICE', 'CODE']. Your keys ['PssRICE', 'CODE']"),
            })
class SMSView(views.APIView):
    def post(self, request):
        lan = request.META.get('HTTP_LANGUAGE')
        if lan is None:
            return response.Response(data={"error": "lan does not exist!"}, status=status.HTTP_400_BAD_REQUEST)
        
        sms_serializer = SmsSerializer(data=request.data)
        if sms_serializer.is_valid():
            text_query = Type.objects.get(type=sms_serializer.data['type'])
            text_serialzier = TypeSerializer(text_query, context={'lan': lan})

            text = multiple_replace(text_serialzier.data['text'], sms_serializer.data['data'])
            phone = sms_serializer.data['phone']

            for word in text_query.keys:
                if word in text:
                    request_keys = [key for key in sms_serializer.data['data'].keys()]
                    return response.Response(
                        data={"error": f"Keys must be {text_query.keys}. Your keys {request_keys}"},
                        status=status.HTTP_400_BAD_REQUEST
                        )
            if settings.DEBUG==False:
                result_status = send(phone=phone, text=text)
            else:
                result_status = status.HTTP_423_LOCKED
                text = "DEBUG is False, message has not sent! " + text

            return response.Response(data={"message": f"{text}"}, status=result_status)
        return response.Response(sms_serializer.errors)