# Streamlit Python Project

A Python project with Streamlit-based web application.

## Project Structure

```
streamlit-python-project/
├── docs/                    # Documentation files
├── src/                     # Source code
│   └── streamlit_app/       # Streamlit application
│       ├── components/      # UI components
│       ├── config/          # Configuration
│       ├── data/            # Data handling
│       ├── models/          # Data models
│       └── utils/           # Utility functions
├── tests/                   # Test files
│   ├── unit/                # Unit tests
│   ├── integration/         # Integration tests
│   └── functional/          # Functional tests
├── .env.example             # Example environment variables
├── requirements.txt         # Production dependencies
├── requirements-dev.txt     # Development dependencies
└── setup.py                 # Package setup file
```

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements-dev.txt`
5. Copy `.env.example` to `.env` and configure as needed

## Running the Application

```bash
streamlit run src/streamlit_app/app.py
```

## Running Tests

```bash
pytest
```
