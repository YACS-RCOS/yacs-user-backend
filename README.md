# YACS User Backend
[![Actions Status](https://github.com/123joshuawu/yacs-user-backend/workflows/Simple%20Pytest/badge.svg?branch=master)](https://github.com/123joshuawu/yacs-user-backend/actions)
[![Coverage Status](https://coveralls.io/repos/github/123joshuawu/yacs-user-backend/badge.svg?branch=master)](https://coveralls.io/github/123joshuawu/yacs-user-backend?branch=master)
[![Requirements Status](https://requires.io/github/123joshuawu/yacs-user-backend/requirements.svg?branch=master)](https://requires.io/github/123joshuawu/yacs-user-backend/requirements/?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/261c6aca0498403b83c9cefb60709a4e)](https://www.codacy.com/manual/123joshuawu/yacs-user-backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=123joshuawu/yacs-user-backend&amp;utm_campaign=Badge_Grade)

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
