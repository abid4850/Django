Development server (modern ASGI) instructions

1) (Optional) Activate your virtual environment in PowerShell:

```powershell
# Windows PowerShell example
. .\.venv\Scripts\Activate.ps1
```

2) Install dev requirements (only needed to use uvicorn):

```powershell
python -m pip install -r requirements-dev.txt
```

3) Start the dev server (the script will prefer uvicorn if installed, otherwise it will use `manage.py runserver`):

```powershell
# From the `app2` project folder
./devserver.ps1
```

Notes:
- Uvicorn provides a fast ASGI server and `--reload` gives auto-reload on code changes.
- For production, use a proper ASGI server + process manager; this script is for development only.
