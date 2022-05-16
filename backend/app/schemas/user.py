from uuid import uuid4
from typing import List
from pydantic import BaseModel, UUID4
import nacl.pwhash

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str

    @property
    def id_hash(self):
        return uuid4().hex

    @property
    def hash_password(self):
        return nacl.pwhash.scryptsalsa208sha256_str(self)


class CreateUser(UserBase):
    id: UUID4


class User(UserBase):
    id: UUID4
    is_active: bool

    class Config:
        orm_mode = True
