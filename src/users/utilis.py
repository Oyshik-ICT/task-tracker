from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"])


def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return password_context.verify(password, hash)
