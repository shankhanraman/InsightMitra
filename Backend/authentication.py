from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from authlib.jose import jwt, JoseError
import os

SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY)
        return payload
    except JoseError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Generate JWT token for login
def create_token(data: dict):
    return jwt.encode({"alg": "HS256"}, data, SECRET_KEY)
