import os
import json

import boto3
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import EventSerializer
from .models import Event


SQS_URL = os.getenv('SQS_URL')
SQS_REGION = os.getenv('SQS_REGION')
AWS_ACCESS_ID = os.getenv('AWS_ACCESS_ID')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')


def send_sqs_message(messageAttributes: dict) -> str:
    sqs = boto3.client('sqs', region_name=SQS_REGION,  aws_access_key_id=AWS_ACCESS_ID,
                       aws_secret_access_key=AWS_ACCESS_KEY)

    response = sqs.send_message(
        QueueUrl=SQS_URL,
        DelaySeconds=10,
        MessageAttributes={
            'event_id': {
                'DataType': 'String',
                'StringValue': messageAttributes['event_id']
            },
            'user_id': {
                'DataType': 'String',
                'StringValue': messageAttributes['user_id']
            },
            'event': {
                'DataType': 'String',
                'StringValue': messageAttributes['event']
            },
            'parameters': {
                'DataType': 'String',
                'StringValue': json.dumps(messageAttributes['parameters'])
            },
            'event_datetime': {
                'DataType': 'String.datetime',
                'StringValue': messageAttributes['event_datetime']
            }
        },
        MessageBody=(
            f'이벤트 발생 : {messageAttributes["event"]}'
            f'수집일시 : {messageAttributes["event_datetime"]}'
        )
    )

    return response['MessageId']


class CollectEventAPI(APIView):
    def post(self, request):
        # 이벤트 수신 시점
        request.data['event_datetime'] = timezone.now()

        serializer = EventSerializer(data=request.data)

        if serializer.is_valid():
            send_sqs_message(serializer.data)

            return Response(dict(is_success=True))
        else:
            return Response(dict(is_success=False))


class SearchEventAPI(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', None)

        event_list = Event.objects.filter(user_id=user_id).order_by('-event_datetime')

        serializer = EventSerializer(event_list, many=True)

        return Response(dict(success=True, result=serializer.data))
