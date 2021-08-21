# linux-packages-installer
This is an application for automating the installation of Linux packages after a fresh/new install of the operating system.
## Application status
- [x] Make it work   :heavy_check_mark:
- [ ] Make it Right  (not yet)

### How to install
Ensure python is installed. This is only working on Debian and Fedora linux distros.
- clone the project. `cd` into the project then .. 
- install requirements by running `pip install -r requiremts.txt`
- Run the app with super user previledges for the app to be able to install packages e.g `sudo python main.py` or `sudo ./script.sh`
- Select option 2 to add the package. Follow the prompts and add required details. For the commands, don't add `sudo`. for example instead of `sudo apt install vlc` for the Debian command, use `apt install vlc`. Also remember to add a `-y` flag if it will prompt you to enter `yes/no` before installing the package too bypass the prompt.
- You can install packages you have saved by selecting option 1.
- Explore other other options as well.

### The app is not fully complete and will keep improving overtime.

