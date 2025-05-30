# Introduction

CYBERSHOP TERMINAL is console based, cyberpunk themed and futuristic online store. Users can register and obtain their 
ssh keys to signin. For version v.1.001 users can request delivery by drone and provide biometric payment on delivery.
While testing the application use os terminal instead of IDE internal terminal (like PyCharm) as they don't fully 
support rich terminal rendering.

**ATTENTION: use dark mode terminal this app is not really designed for light version**

## How to run

1. Clone git repository
```bash
  git clone https://github.com/Kenwoll/COMP-9001-Project.git
```

2. Navigate to Your Project Directory
```bash
  cd your/path/COMP-9001-Project
```
3. Create a Virtual Environment
```bash
  python3 -m venv venv
```
4. Activate the Virtual Environment
```bash
  source venv/bin/activate
```
5. Install Packages from `requirements.txt`
```bash
  pip install -r requirements.txt
```
6. Run Python Application
```bash
  python main.py
```

## How to sign in

You can create your own user and application will store user specific ssh key in the data folder. However, if you don't want to create user then application comes with already created one.
You can use `neon_hacker` username to sign in and explore the rarest inventory in the galaxy.

## Considerations

Data used in this project is json based and generated by AI. This was discussed with my tutor and permission was 
granted. Also even though this project uses external libraries it still can run in the ED environment. 
Perhaps env already has necessary dependencies.