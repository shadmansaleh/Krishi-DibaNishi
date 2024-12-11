# Krishi Dibanishi

Krishi Dibanishi is a basic web application designed to assist farmers by providing valuable insights and tools to improve their farming practices. Built with Flask, the app offers the following key features:

## Features
1. **Crop Suggestion**
   - Recommends the best crops to grow based on soil conditions, weather, and other factors.

2. **Weather Prediction**
   - Provides accurate and up-to-date weather forecasts to help farmers plan their activities.

3. **Market Prices**
   - Displays the latest market prices for crops, enabling farmers to make informed decisions.

## Installation

### Prerequisites
- Python (3.8 or higher)
- pip (Python package manager)
- Virtual environment setup (optional but recommended)

### Steps
1. Clone the repository:
```bash
   git clone https://github.com/shadmansaleh/KrishiDibaNishi
   cd krishi-dibanishi
```
2. Create and activate a virtual environment:


```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
    python run.py
```

5. Open your browser and visit:
    http://127.0.0.1:5000

### Folder Structure

```python
/krishi-dibanishi
    /run.py              # Entry point to start the app
    /config.py           # Application configuration settings
    /app                 # Main application code
        /__init__.py     # Initializes the Flask app
        /api.py          # Api endpoints
        /views.py        # Routes and logic
        /models.py       # (Future scope) Database models
        /static/         # Static assets (CSS, JS, images)
        /templates/      # HTML templates
          /layouts/      # Layout-related templates
          /pages/        # Templates for individual pages
          /partials/     # Reusable partial components
    /requirements.txt    # Python dependencies
    /.venv               # Virtual environment (not included in repository)
```

### License

This project is open-source. Feel free to modify and distribute as per the terms of the license.

### Credits
- [Shadman Saleh](https://github.com/shadmansaleh) [email](mailto://shadmansaleh3@gmail.com)
- [Ratnajit Dhar]() [email]()
- [Arpita Mallik]() [email]()
- [Faozia Fariha]() [email]()
