# pySDOM_demo
This is a repository to demonstrate how to setup and work with the python-based version of NREL Storage Deployment Optimization Model pySDOM that will be released soon.

# INSTRUCTIONS

## CLONE THE SDOM REPO
- Open VS code and use file -> open folder and select the folder where you want to copy the repo.
- Clone in your local the python version of SDOM repo:
```powershell
git clone https://github.com/Omar0902/SDOM.git
```
- While the new branch is merged in main, please open in VS code the folder with the SDOM source code and open the correct branch:
```powershell
git checkout sm/io_improovements
```

## INSTALL uv AND CREATE A VIRTUAL ENVIROMENT
- Install uv (A python manager for virtual enviroments, installing packages etc). Follow the instructions in: https://pypi.org/project/uv/
- Create a virtual enviroment ".venv"
```powershell
uv venv .venv
```
This command creates a new Python virtual environment in the `.venv` directory.

## INSTALL YOUR LOCAL SDOM PYTHON MODULE
- Install, in your local virtual enviroment tha you've just created, your local python SDOM module that you have cloned in the previus steps by doing:
```powershell
uv pip install -e "C:\YOUR_PATH\SDOM"
```
- It will install also the SDOM dependencies. You should see something like this:

```powershell
 uv pip install -e "C:\YOUR_PATH\SDOM"
Resolved 9 packages in 1.90s
      Built sdom @ file:///C:/YOUR_PATH/SDOM
Prepared 1 package in 1.68s
Installed 9 packages in 1.60s
 + numpy==2.3.2
 + pandas==2.3.1
 + ply==3.11
 + pyomo==6.9.2
 + python-dateutil==2.9.0.post0
 + pytz==2025.2
 + sdom==0.0.1 (from file:///C:/Users/smachado/repositories/pySDOM/SDOM)
 + six==1.17.0
 + tzdata==2025.2
```


# USE SDOM

- Please see the script in this repo "demo_SDOM.py" as an example on how you can use SDOM.
- In this Demo it was used cbc solver. please copy also the "Solver" folder and specify the address to the cbc.exe.


