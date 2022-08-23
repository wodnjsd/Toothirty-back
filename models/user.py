# ! Import datetime
from datetime import datetime, timedelta

# ! Import jwt library (this is pyjwt)
import jwt

from sqlalchemy.ext.hybrid import hybrid_property

from app import db, bcrypt
from models.base import BaseModel

# ! Import my secret
from config.environment import secret

class UserModel(db.Model, BaseModel):

    __tablename__ = "users"

    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False, unique=True)

    password_hash = db.Column(db.Text, nullable=True)

    @hybrid_property
    def password(self):
        pass

    @password.setter
    def password(self, password_plaintext):
        encoded_pw = bcrypt.generate_password_hash(password_plaintext)
        self.password_hash = encoded_pw.decode("utf-8")

    # ! Use bcrypt to validate our password
    def validate_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password_hash, plaintext_password)

    def generate_token(self):
        # ! Create a token for this user.
        # ! Need a payload for the token
        payload = {
            # ! This will expire 1 day from now.
            "exp": datetime.utcnow() + timedelta(days=1),
            # ! The token was created (issued at)
            "iat": datetime.utcnow(),
            # ! Put the user id on the token to identify the user
            "sub": self.id,
        }

        # ! Create the token itself.
        token = jwt.encode(
            payload,  # ! provide the payload
            secret,  # ! provide a secret
            algorithm="HS256",
        )

        # print(token, type(token))

        return token
