from app.auth.jwt import create_access_token

token = create_access_token("1")

print(token)
