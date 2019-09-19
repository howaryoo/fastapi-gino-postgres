from app.application import app
from app.routes.users import router as user_router

ROUTERS = (user_router, )

for r in ROUTERS:
    app.include_router(r)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True, debug=True)
