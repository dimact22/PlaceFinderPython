# Import the googlemaps library and dotenv to load environment variables
from pydantic import BaseModel, EmailStr, Field, validator
from fastapi import HTTPException, status
import re
from typing import Optional
from typing import List, Optional

# Model to represent a user's registration data
class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6, max_length=20)

class UserRegister(BaseModel):
    firstName: str = Field(..., min_length=3, max_length=50, description="Ім'я користувача")
    lastName: str = Field(..., min_length=3, max_length=50, description="Прізвище користувача")
    email: EmailStr = Field(..., description="Електронна адреса користувача")
    phone: str = Field(..., pattern=r"^\+380\d{9}$", description="Номер телефону у форматі +380XXXXXXXXX")
    password: str = Field(
        ...,
        min_length=6,
        max_length=30,
        description="Пароль, який містить від 6 до 30 символів, включаючи цифри, спеціальні символи, великі та малі літери",
    )
    

    @validator("firstName", "lastName")
    def validate_name(cls, value: str):
        if not value.isalpha():
            raise ValueError("Поле може містити лише літери")
        return value


