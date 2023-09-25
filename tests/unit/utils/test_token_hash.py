from datetime import timedelta

import pytest
from jose import jwt

from app.utils.auth import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    ALGORITHM,
    SECRET_KEY,
    create_access_token,
    pwd_context,
    verify_token,
)


def test_create_access_token():
    data = {"sub": "test_user"}
    token = create_access_token(data)
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert decoded_token["sub"] == "test_user"


def test_verify_token():
    data = {"sub": "test_user"}
    token = create_access_token(data)
    verified_data = verify_token(token)
    assert verified_data["sub"] == "test_user"


def test_verify_token_invalid_token():
    invalid_token = "invalid_token"
    verified_data = verify_token(invalid_token)
    assert verified_data is None


def test_verify_token_expired_token():
    data = {"sub": "test_user"}
    # Set the expiration time to a past time
    expire = (timedelta(minutes=-1)).total_seconds()
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    expired_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    verified_data = verify_token(expired_token)
    assert verified_data is None
