import ormar
from pydantic.networks import EmailStr
from pydantic.types import FilePath
from datetime import datetime

from ..core.settings import metadata, database


class User(ormar.Model):
    """User model"""

    class Meta:
        tablename: str = "users"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True, index=True)
    full_name: str = ormar.String(min_length=5, max_length=50)
    username: str = ormar.String(
        min_length=3, max_length=50, allow_blank=False, unique=True, index=True
    )
    email: EmailStr = ormar.String(max_length=255)
    hashed_password: str = ormar.String(max_length=255, allow_blank=False, unique=True)
    avatar_path: FilePath = ormar.String(max_length=255, allow_blank=False, unique=True)
    is_active: bool = ormar.Boolean(default=False)
    is_superuser: bool = ormar.Boolean(default=False)
    created_at: datetime = ormar.DateTime(default=datetime.utcnow)
    updated_at: datetime = ormar.DateTime(
        default=datetime.now, onupdate=datetime.utcnow
    )
    last_login: datetime = ormar.DateTime()
