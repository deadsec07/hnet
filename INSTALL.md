For MAC/Linux

chmod +x scripts/install_dependencies.sh
chmod +x scripts/setup_virtualenv.sh
./scripts/install_dependencies.sh  # Run this to install dependencies
./scripts/setup_virtualenv.sh     # Run this to set up the virtual environment


For windows

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

For others

python scripts/install_requirements.py

