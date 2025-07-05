import uvicorn

def start():
    uvicorn.run(
        "main:app",         # <--- Use import string
        host="127.0.0.1",
        port=8000,
        reload=True         # Only works with import string
    )

if __name__ == "__main__":
    start()