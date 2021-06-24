# Time Tracking Tool 
#### Track your Working Hours during HomeOffice
![](https://github.com/DanielGuo1/HomeOffice-Time-Tracking-Tool/blob/main/img/zeitwaechter.PNG) 
- Automated TimeTracking Tool 
- PyQt5 Window with System Tray Intergration
- Reminder after regular Workingtime
- Reminder 15 min before max. time (10:45h)

![](https://github.com/DanielGuo1/HomeOffice-Time-Tracking-Tool/blob/main/img/Regelarbeitszeit.PNG)


## Requirements
- **Python: 3**
Recommended version: 3.8

## Installation
####  **Easy**:
- Run *install.bat*

####  **Advanced**:
First download everything and install required pip packages (cmd into the Folder):

`$ pip install pip --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt`

After Installation run ***Zeitwaechter.ps1*** with PowerShell:
- **Right Click on File → Run with Powershell**

Task Scheduler
----
This File contains your Shutup Time for today. If you do not want to execute this File every day:
- **Open task scheduler:  WIN+R → taskschd.msc (or search for Task Scheduler)**
- **Create a new Task**:
	*	Trigger: At Log on
	*	Action: Start a program (C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe)
		Add Arguments: -File yourPath/to/Zeitwaechter.ps1 (no quotation marks)
		e.g. *-File C:\Users\platau\Documents\Zeitwaechter.ps1*
![](https://github.com/DanielGuo1/HomeOffice-Time-Tracking-Tool/blob/main/img/action_onLOGON.PNG)
![](https://github.com/DanielGuo1/HomeOffice-Time-Tracking-Tool/blob/main/img/taskschd_action.PNG)

Problem
---
If Task Scheduler fails, change Path in *Zeitwaechter.ps1*:
Instead of `$ Get-Eventlog -Logname System -InstanceId 2147489654,2147489653  -Source Eventlog -after ([datetime]::Today) | Export-Csv -Path StartTime.csv -NoTypeInformation`


to:
`$ Get-Eventlog -Logname System -InstanceId 2147489654,2147489653  -Source Eventlog -after ([datetime]::Today) | Export-Csv -Path "C:\Users\platau\Documents\05_Projekte\ArbeitszeitTool\Zeitwaechter\StartTime.csv" -NoTypeInformation `

Run Program
----
- Run *start.vbs*

If you want to start this Tool everytime you start your Computer:
---
Create a Shortcut of *start.vbs* to this Folder:
C:\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
![](https://github.com/DanielGuo1/HomeOffice-Time-Tracking-Tool/blob/main/img/Autostart.PNG)

**Important: Do not copy start.vbs to the folder → Creat a Shortcut**
