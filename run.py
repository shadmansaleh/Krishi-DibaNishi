from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app()

if __name__ == "__main__":
    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        port = int(os.getenv("PORT", 5000))
        app.run(host="0.0.0.0", port=port)
    else:
        app.run(debug=True)
