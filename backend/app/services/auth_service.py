from sqlalchemy.orm import Session

from app.auth.jwt import create_access_token
from app.auth.password import hash_password, verify_password
from app.models.user import User
from app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from app.schemas.user import UserCreate, UserLogin


def register_user(
    db: Session,
    user_data: UserCreate,
) -> User:
    existing_user = get_user_by_email(
        db=db,
        email=user_data.email,
    )

    if existing_user:
        raise ValueError(
            "A user with this email already exists."
        )

    hashed_password = hash_password(
        user_data.password
    )

    user = create_user(
        db=db,
        name=user_data.name,
        email=user_data.email,
        hashed_password=hashed_password,
    )

    return user


def login_user(
    db: Session,
    user_data: UserLogin,
) -> str:
    user = get_user_by_email(
        db=db,
        email=user_data.email,
    )

    # print("USER FOUND:", user)

    if not user:
        print("USER NOT FOUND")

        raise ValueError(
            "Invalid email or password."
        )

    # print("STORED HASH:", user.hashed_password)

    password_is_valid = verify_password(
        user_data.password,
        user.hashed_password,
    )

    # print("PASSWORD VALID:", password_is_valid)

    if not password_is_valid:
        raise ValueError(
            "Invalid email or password."
        )

    access_token = create_access_token(
        subject=str(user.id)
    )

    return access_token