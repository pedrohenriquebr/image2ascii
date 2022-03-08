import dotenv
import uvicorn
dotenv.load_dotenv()
from server import app
if __name__ == "__main__":
    from config import PORT
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=True)
