# linux-packages-installer
This is an application for automating the installation of Linux packages after a fresh/new install of the operating system.
## Application status
- [x] Make it work   :heavy_check_mark:
- [ ] Make it Right  (not yet)

### How to run
Ensure python is installed. This is only works on Debian based distros like Ubuntu, Pop OS and Red Hat Linux like Fedora.
- Clone the project `git clone git@github.com:jachin-manda/linux-packages-installer.git` and `cd` into the project: `cd linux-packages-installer` 
- Create a virtual environment: `python3 -m venv <name you want to call your virtual enviroment>` e.g. `python3 -m venv env`
- Activate the virtual environment: `source <name of virtual env>/bin/activate` e.g. `source env/bin/activate`
- Install requirements by running `pip install -r requiremts.txt`
- Run the app with super user privileges for the app to be able to install packages e.g. `sudo <name of virtual env>/bin/python main.py` e.g. `sudo env/bin/python main.py`
- Explore available options and follow prompts
- For the commands, don't add `sudo`. For example when adding a package instead of `sudo apt install vlc` use `apt install vlc`.
- If the package has many commands in order to install, concatenate the commands with `&&`. For example when saving the commands for 
  installing Docker on Fedora, do this: `dnf -y install dnf-plugins-core && dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo && dnf install docker-ce docker-ce-cli containerd.io`

- Also remember to add a `-y` flag if it will prompt you to enter `yes/no` before installing the package in order to bypass the `y/N` prompt.

### The app is not fully complete and will keep improving overtime.

