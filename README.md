# Sign Detection Model

## Project Setup With environment

**Use a python latest version or 3.12.6 or higher**

## window OS
### _Open terminal with command prompt only for use this commands can't use the powershell._

### 1. Create a virtual environment
```bash
python -m venv venv
```

### 2. Activate the virtual environment
```bash
venv\Scripts\activate
```

### 3. Install the requirements
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn main:app --reload --port 8000
```

## Mac OS

### 1. Create a virtual environment
```bash 
python3 -m venv venv
```

### 2. Activate the virtual environment
```bash
source venv/bin/activate
```

### 3. Install the requirements
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn main:app --reload --port 8000
```

## Endpoint Information

**_Request Method:_**
```bash
POST
```

**_URL:_**
```bash
http://localhost:8000/predict
```

**_Response:_**
```bash
{ "prediction": prediction }
```

# Other Information

### Get the all dependencies into the requirement file
```bash
pip freeze > requirements.txt
```