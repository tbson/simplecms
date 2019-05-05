from rest_framework.response import Response
from rest_framework import status


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'user': user
    }


def getToken(headers):
    result = headers.get('Authorization', None)
    if(result):
        return result.split(' ')[1]
    return ''


def error_format(data):
    if type(data) is str:
        return {'detail': data}
    if type(data) is dict:
        return data
    return {}


def res(*args, **kwargs):
    return Response(*args, **kwargs)


def err_res(data, status_code=status.HTTP_400_BAD_REQUEST):
    return Response(error_format(data), status=status_code)
