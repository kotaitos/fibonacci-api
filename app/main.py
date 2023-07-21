import os
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from utils import fibonacci
from middleware import TimeoutMiddleware


REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 5))


app = FastAPI()
app.add_middleware(TimeoutMiddleware, timeout=REQUEST_TIMEOUT)


@app.exception_handler(RequestValidationError)
async def handler(request, exc):
  return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"status": status.HTTP_400_BAD_REQUEST, "message": "Bad Request"})


@app.get(
  "/fib",
  summary="Fibonacci",
  description="Returns the nth number in the Fibonacci sequence",
  response_description="The nth number in the Fibonacci sequence",
  responses={
    200: {
      "description": "Successful Response",
      "content": {
        "application/json": {
          "example": {
            "result": 3
          }
        }
      }
    },
    400: {
      "description": "Bad Request",
      "content": {
        "application/json": {
          "example": {
            "status": 400,
            "message": "Bad Request"
          }
        }
      }
    },
    422: {
      "description": "Unprocessable Entity",
      "content": {
        "application/json": {
          "example": {
            "status": 422,
            "message": "Unprocessable Entity"
          }
        }
      }
    },
    500: {
      "description": "Internal Server Error",
      "content": {
        "application/json": {
          "example": {
            "status": 500,
            "message": "Internal Server Error"
          }
        }
      }
    },
    504: {
      "description": "Gateway Timeout",
      "content": {
        "application/json": {
          "example": {
            "status": 504,
            "message": "Gateway timeout."
          }
        }
      }
    }
  })
def read_fib(n: int):
  try:
    result = fibonacci(n)
  except ValueError as e:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"status": status.HTTP_400_BAD_REQUEST, "message": "Bad Request"})
  except RecursionError as e:
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"status": status.HTTP_400_BAD_REQUEST, "message": "Requested number is too large"})
  except Exception as e:
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "message": "Internal Server Error"})
  
  return JSONResponse(status_code=status.HTTP_200_OK, content={"result": result})
