# Import the googlemaps library and dotenv to load environment variables
from fastapi import Request, status, HTTPException
from fastapi.responses import JSONResponse
from jose import jwt, JWTError
import os
from dotenv import load_dotenv
load_dotenv()
from datetime import datetime
from db.dbconn import tempUsers
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Import HTTPBearer for authorization and token handling
security = HTTPBearer()

# Middleware to extract and return the email from the token payload
async def auth_middleware_email_return(request: Request):
    try:
        credentials: HTTPAuthorizationCredentials = await security(request)
        token = credentials.credentials
        # Decode the JWT token using the secret key and HS256 algorithm
        payload = jwt.decode(token, os.getenv("SecretJwt"), algorithms=["HS256"])
        # Return email from the payload
        return str(payload.get("sub"))
    except JWTError:
        # Raise an HTTP 403 error if the token is invalid or expired
        raise HTTPException(
            status_code=403, detail="Token is invalid or expired")
    except Exception as e:
        # Raise an HTTP 404 error for any other exceptions
        raise HTTPException(status_code=404, detail="Some error")

# Middleware to extract and return the type from the token payload
async def auth_middleware_type_return(request: Request):
    try:
        credentials: HTTPAuthorizationCredentials = await security(request)
        token = credentials.credentials
        payload = jwt.decode(token, os.getenv("SecretJwt"), algorithms=["HS256"])
        # Return the "type" attribute from the payload
        return str(payload.get("type"))
    except JWTError:
        raise HTTPException(
            status_code=403, detail="Token is invalid or expired")
    except Exception as e:
        raise HTTPException(status_code=404, detail="Some error")

# Function to validate a temporary registration token
async def validate_tempToken(token: str):
    # Query the tempUsers collection for a document with the specified registration token
    temp_user = tempUsers.find_one({"registration_token": token})

    # Check if a temporary user exists with this token
    if not temp_user:
        raise HTTPException(status_code=404, detail="Token not found or invalid")

    # Check if the token has expired
    if temp_user['expires_at'] < datetime.utcnow():
        # Delete the temporary user if the token has expired
        tempUsers.delete_one({"registration_token": token})
        raise HTTPException(status_code=400, detail="Token expired")
    # Return the temporary user data if validation is successful
    return temp_user