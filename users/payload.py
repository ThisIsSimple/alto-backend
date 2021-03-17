import jwt
import uuid
import warnings

from alto.settings import BASE_URL

from django.contrib.auth import get_user_model

from calendar import timegm
from datetime import datetime

from rest_framework_jwt.compat import get_username
from rest_framework_jwt.compat import get_username_field
from rest_framework_jwt.settings import api_settings


def jwt_payload_handler(user):
    username_field = get_username_field()
    username = get_username(user)

    warnings.warn(
        'The following fields will be removed in the future: '
        '`email` and `user_id`. ',
        DeprecationWarning
    )

    payload = {
        'user_id': user.pk,
        'username': username,
        'name': user.name,
        'profile': user.profile,
        'phone': user.phone,
        'birthday': user.birthday.__str__(),
        'exp': datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA
    }

    try:
        payload['rank'] = user.rank.name
        payload['level'] = user.rank.level
    except:
        pass

    try:
        payload['profile_image'] = BASE_URL + user.profile_image.url
    except:
        payload['profile_image'] = '/static/images/profile_blank.jpg'
    if hasattr(user, 'email'):
        payload['email'] = user.email
    if isinstance(user.pk, uuid.UUID):
        payload['user_id'] = str(user.pk)

    payload[username_field] = username

    # Include original issued at time for a brand new token,
    # to allow token refresh
    if api_settings.JWT_ALLOW_REFRESH:
        payload['orig_iat'] = timegm(
            datetime.utcnow().utctimetuple()
        )

    if api_settings.JWT_AUDIENCE is not None:
        payload['aud'] = api_settings.JWT_AUDIENCE

    if api_settings.JWT_ISSUER is not None:
        payload['iss'] = api_settings.JWT_ISSUER

    return payload
