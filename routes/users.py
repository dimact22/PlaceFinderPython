from fastapi import APIRouter, HTTPException, status, Depends
from db.dbconn import users_collections  # Assuming this is your database collection or function
from db.hash import Hash
from jose import jwt
import os
from shemas.users import UserLogin, UserRegister

user_app = APIRouter()  # Correct instantiation of APIRouter

@user_app.post("/login")
async def login_user(user: UserLogin):
    """
    Login user: Authenticates and returns a JWT token.
    """
    
    found_user = users_collections.find_one({"email": user.email})  # Access your DB here
    
    if not found_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    if Hash.verify(user.password, found_user["password"]):
        token = jwt.encode({'sub': found_user["email"]}, os.getenv("SecretJwt"), algorithm='HS256')
        return {"token": token}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")

@user_app.post("/register")
async def create_user(user: UserRegister):
    """
    Register a new user

    Creates a new user account with a hashed password. If a user with the provided email already exists, an HTTP 400 error is returned.
    - **name**: The name of the user.
    - **lastname**: The lastname of the user.
    - **email**: The email address of the user.
    - **password**: The password of the user.
    """
    existing_user = users_collections.find_one({"email": user.email}) # Check if the email already exists in the database
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists") # Return error if user exists
    hashed_password = Hash.bcrypt(user.password) # Hash the password for security
    user.password = hashed_password
    token = jwt.encode(
            {'sub': user.email}, os.getenv("SecretJwt"), algorithm='HS256') # Generate JWT token
    try:
        users_collections.insert_one(dict(user)) # Insert new user into database
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="There is some problem with the database, please try again later")
    return {"status": "Ok", "token": token} # Return success message and token


