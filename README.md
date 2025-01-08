# Krishi Dibanishi

Krishi Dibanishi is a basic web application designed to assist farmers by providing valuable insights and tools to improve their farming practices. Built with Flask, the app offers the following key features:

## Features
1. **Crop Suggestion**
   - Recommends the best crops to grow based on soil conditions, weather, and other factors.

2. **Weather Prediction**
   - Provides accurate and up-to-date weather forecasts to help farmers plan their activities.

3. **Market Prices**
   - Displays the latest market prices for crops, enabling farmers to make informed decisions.

4. **Soil Tips**
   - Suggests tips for how to improve the soil

## Installation

### Prerequisites
- Python (3.8 or higher)
- pip (Python package manager)
- Virtual environment setup (optional but recommended)

### Steps
1. Clone the repository:
```bash
git clone https://github.com/shadmansaleh/Krishi-DibaNishi
cd krishi-dibanishi
```
2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate virtual environtment:

- On Linux
```bash
source .venv/bin/activate
```

- On Windows
```bash
source .venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Setup environment:

```bash
cp .env.example .env
```
Then edit .env to fill it with required secrete values

6. Set Up the Database:
```bash
flask db upgrade
```

7. Run the app:
```bash
python run.py
```

5. Open your browser and visit:
    http://127.0.0.1:5000

### Folder Structure

```python
/Krishi-DibaNishi/
    /run.py              # Entry point to start the app
    /config.py           # Application configuration settings
    /app/                # Main application code
        /__init__.py     # Initializes the Flask app
        /routes/         # All route handlers
          /api.py        # Api endpoints
          /views.py      # Webpage router from pages/
          /auth.py       # Authentication handler
        /static/         # Static assets (CSS, JS, images)
          /css           # css files (mostly generated from scss)
          /scss          # scss stylesheets
          /js            # imported js for frontend
          /images        # image directory
          /favicon.ico   # favicon
        /templates/      # HTML templates
          /layouts/      # Layout-related templates
          /pages/        # Templates for individual pages
          /partials/     # Reusable partial components
        /models.py       # Database models
        /utils.py        # utility functions
        /extensions.py   # extra
    /requirements.txt    # Python dependencies
    /.venv               # Virtual environment (not included in repository)
    /.env                # Environtment file for holding secretes
```

### License

This project is open-source. Feel free to modify and distribute as per the terms of the license.

### Credits
- [Shadman Saleh](https://github.com/shadmansaleh) ([shadmansaleh3@gmail.com](mailto://shadmansaleh3@gmail.com))
- [Ratnajit Dhar](https://github.com/ratnajit-dhar) ([rdpratnajit@gmail.com](mailto://rdpratnajit@gmail.com))
- [Arpita Mallik](https://github.com/ArpitaMallik) ([arpitamallik13@gmail.com](mailto://arpitamallik13@gmail.com))
- [Faozia Fariha](https://github.com/bountyhunter12) ([faoziafariha058@gmail.com](mailto://faoziafariha058@gmail.com))
