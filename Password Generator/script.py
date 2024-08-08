import secrets
import hashlib
def password():
    password_text = str(secrets.token_bytes())
    password_hashed = hashlib.sha256(password_text.encode()).hexdigest()
    print(password_hashed, 'Is your generated password')
password()