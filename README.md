# NREL SDOM (Storage Deploymrnt Optimization Model) demo
This is a repository to demonstrate how to setup and work with the python-based version of NREL Storage Deployment Optimization Model "sdom" that is now released.

# INSTRUCTIONS


## INSTALL uv AND CREATE A VIRTUAL ENVIROMENT
- Install uv (A python manager for virtual enviroments, installing packages etc). Follow the instructions in: https://pypi.org/project/uv/
- Create a virtual enviroment ".venv"
```powershell
uv venv .venv
```
This command creates a new Python virtual environment in the `.venv` directory.

## INSTALL SDOM PYTHON PACKAGE AND LOGGING
- Install, in your local virtual enviroment that you've just created, the python SDOM module by doing:
```powershell
uv pip install sdom
```
- It will install also the SDOM dependencies. 

- Also install Logging package executing:
```powershell
uv pip install logging
```

- Check your enviroment. If you do:
```powershell
uv pip list
```
You should see something like this:

```powershell
Package         Version
--------------- -----------
logging         0.4.9.6
numpy           2.3.2
pandas          2.3.1
ply             3.11
pyomo           6.9.3
python-dateutil 2.9.0.post0
pytz            2025.2
sdom            0.0.3
six             1.17.0
tzdata          2025.2
```


# USE SDOM

- Please see the script in this repo "demo.py" as an example on how you can use SDOM.
- In this Demo it was used cbc solver. please copy also the "Solver" folder and specify the address to the cbc.exe.


