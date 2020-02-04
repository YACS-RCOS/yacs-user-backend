# YACS User Backend
[![Actions Status](https://github.com/123joshuawu/yacs-user-backend/workflows/Simple%20Pytest/badge.svg?branch=test/simple)](https://github.com/123joshuawu/yacs-user-backend/actions)
[![Coverage Status](https://coveralls.io/repos/github/123joshuawu/yacs-user-backend/badge.svg?branch=test/simple)](https://coveralls.io/github/123joshuawu/yacs-user-backend?branch=test/simple)
[![Requirements Status](https://requires.io/github/123joshuawu/yacs-user-backend/requirements.svg?branch=test%2Fsimple)](https://requires.io/github/123joshuawu/yacs-user-backend/requirements/?branch=test%2Fsimple)

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
