pip install pip --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
timeout /T 1
start powershell.exe -Command "&'Zeitwaechter.ps1'"
