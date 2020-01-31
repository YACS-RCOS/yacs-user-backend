# YACS User Backend
[![Coverage Status](https://coveralls.io/repos/github/123joshuawu/yacs-user-backend/badge.svg?branch=test/simple)](https://coveralls.io/github/123joshuawu/yacs-user-backend?branch=test/simple)

## Description
The backend API for the user management system of YACS Project.

## Installation

### Docker
```bash
git clone https://github.com/YACS-RCOS/yacs-user-backend
cd yacs-user-backend
cp config.py.example config.py
vim config.py # Modify the database connection
docker build -t userbackend .
docker run -d --name userbackend -p 5674:80 userbackend
```

### Development
```bash
git clone https://github.com/YACS-RCOS/yacs-user-backend
cd yacs-user-backend
pip3 install -r requirements.txt
cp config.py.example config.py
vim config.py # Modify the database connection
python3 app.py
```

## License
AGPL v3
