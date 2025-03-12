# hnet
hnet pentest tools

## Setting up the Environment

### Prerequisites:
- Python 3
- `pip`
- `virtualenv` (for setting up a virtual environment)

### Setup Instructions:

1. **For Linux/MacOS:**
    - Run the following commands to install system dependencies and set up a virtual environment:
        ```bash
        ./scripts/install_dependencies.sh
        ./scripts/setup_virtualenv.sh
        ```

2. **For Windows:**
    - You can manually set up a Python virtual environment:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        pip install -r requirements.txt
        ```

3. **Using Python Script**:
    - If you prefer to use a Python script to install requirements, you can use `install_requirements.py`:
        ```bash
        python scripts/install_requirements.py
        ```

### Notes:
- After setting up the virtual environment, make sure to activate it:
    ```bash
    source venv/bin/activate  # Linux/MacOS
    venv\Scripts\activate     # Windows
    ```
- All dependencies will be installed in the virtual environment, ensuring that your tools run with the correct versions of libraries.

