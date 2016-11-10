# Library-Portal
ACE e-Library 

Start making your contributions here as discussed in the meeting . 
Happy Coding !


##Getting Started 

#Step 1 :
 Install Python in your system . 
 
## Windows
You can download Python for Windows from the website https://www.python.org/downloads/release/python-351/
 
## Debian or Ubuntu 
    sudo apt-get install python3.5

#Step 2 :

Set up virtualenv and install Django

 Find a directory in which you want to create the virtualenv; your home directory, for example. On Windows it might look like C:\Users\Name\ (where Name is the name of your login).
 
 NOTE: On Windows, make sure that this directory does not contain accented or special characters; if your username contains accented characters, use a different directory, for example C:\libraryPortal
 
 
 Create a new directory libraryPortal from your home directory:

command-line
    
    $ mkdir libraryPortal
    $ cd libraryPortal

#Windows

command-line
    
    C:\Users\Name\libraryPortal> C:\Python35\python -m venv myvenv

where C:\Python35\python is the directory in which you previously installed Python and myvenv is the name of your virtualenv. 
You can use any other name, but stick to lowercase and use no spaces, accents or special characters. It is also good idea to keep the name short.

#Linux
    $ python3 -m venv myvenv
    

# Step 3

##Windows
Start your virtual environment by running:


    C:\Users\Name\libraryPortal> myvenv\Scripts\activate
    
NOTE: on Windows 10 you might get an error in the Windows PowerShell says execution of scripts is disabled on this system. In those cases open another Windows PowerShell and Run as Administrator try doing this before continue:

    C:\WINDOWS\system32> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
    Execution Policy Change
    The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expos you to the security risks described in the about_Execution_Policies help topic at http://go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy? [Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): A

# Linux
Start your virtual environment by running:

    $ source myvenv/bin/activate
    
    
 
# Installing Django
 
    (myvenv) ~$ pip install django~=1.9.0
    Downloading/unpacking django==1.9
    Installing collected packages: django
    Successfully installed django
    Cleaning up...
    
    
###On Windows
If you get an error when calling pip on Windows platform, please check if your project pathname contains spaces, accents or special characters (for example, C:\Users\User Name\libraryPortal). If it does, please consider using another place without spaces, accents or special characters (suggestion: C:\libraryPortal). Create a new virtualenv in the new directory, then delete the old one and try the above command again. (Moving the virtualenv directory won't work since virtualenv uses absolute paths.)

###on Windows 8 and Windows 10

Your command line might freeze after when you try to install Django. If this happens, instead of the above command use:
Or you could use PowerShell instead of command prompt

    C:\Users\Name\libraryPortal> python -m pip install django~=1.9.0


# Fork and Clone the repo and start contributing 
    $mkdir aceLibraryProject
    $cd aceLibraryProject
    $git init
    $git remote add origin https://github.com/<your username>/Library-Portal.git
    $git pull
    $git checkout development

# Run The Development Server 
    $python manage.py runserver


    

    






 
 
 


 

