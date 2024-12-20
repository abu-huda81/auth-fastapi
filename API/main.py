from fastapi import FastAPI
from core.security import JWTAuth
from starlette.middleware.authentication import AuthenticationMiddleware
from users.routes import router as guest_router, user_router
from auth.route import router as auth_router
from users.models import UserModel
from core.database import Base, engine

app = FastAPI()

# routers:
app.include_router(guest_router)
app.include_router(user_router)
app.include_router(auth_router)

# Add Middleware
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())


# Create the tables in the database
Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
