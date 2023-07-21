from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from utils import fibonacci

app = FastAPI()

  
@app.get("/fib")
def read_fib(n: int):
  try:
    result = fibonacci(n)
  except ValueError as e:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"status": status.HTTP_400_BAD_REQUEST, "message": "Bad Request"})
  except Exception as e:
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Internal Server Error"})
  
  return JSONResponse(status_code=status.HTTP_200_OK, content={"result": result})
