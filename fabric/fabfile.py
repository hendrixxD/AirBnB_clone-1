from fabric.api import *

# ----------------------
# using 'run' command
# ----------------------

# create a directory
run("mkdir joshua")

# uptime
run("uptime")

# display system hostname
run("hostname")

# gets the result of ls command

result = run("ls -l /var/www/")

# check if command failed
result.failed

# ---------------------------
# using the 'sudo' argument
# ---------------------------

# create a directiry using sudo
sudo("mkdir hendrixx")

# create a directory as another user
sudo ("mkdir dir1", user="joshua regan")

# return the output
result = sudo("ls -l /var/www")


# ------------------------------------------------
# using 'local' command to run argument locally
# ------------------------------------------------

# create a source distribution tar archive(for a python App)
local("python setup.py sdist --formats=gztar", capture=False)

# Extract the contents of a tar archive
local("tar xzvf /tmp/trunk/app.tar.gz")

# remove a file
local("rm /tmp/trunk/app.tar.gz")

# -----------------------------------------------------------------------
# using the 'get' command to fetch or donload infor from a remote system
# similar to 'scp'.
# You can specify the remote path to this file with 'remote_path' argument
# You can specify the local -download- path with the 'local_path' argument
# -----------------------------------------------------------------------

# Download some logs
get(remote_path="/tmp/log_extracts.tar.gz", local_path="/logs/new_log.tar.gz")

# download a database backup
get("/backup/db.gz", "./db.gz")


# ---------------------------------------------------------------------------------------------------------------------------------
# 'put' works same as get.
# it is used to upload files

#    'local_path' - set the local path.
#    'remote_path' - set the remote path.
#    'use_sudo' - upload the file to anywhere on the remote machine using a nifty trick: upload to a temporary location then move.
#    'mode' - set the file mode (flags).
#    'mirror_local' - set the file flags (i.e. make executable) automatically by reading the local file’s mode.
# ----------------------------------------------------------------------------------------------------------------------------------

# Upload a tar archive of an application
put("/local/path/to/app.tar.gz", "/tmp/trunk/app.tar.gz")

# Use the context manager `cd` instead of "remote_path" arg.
# This will upload app.tar.gz to /tmp/trunk/
with cd("/tmp"):
    put("local/path/to/app.tar.gz", "trunk")

# upload a file and set the exact mode desired
upload = put("requirements.txt", "reqiorements.txt", mode=664)

# Verify the upload
upload.succeeded

# --------------------------------------------------
# using 'prompt'
# prompt does exactly as it sounds
# it can also be used to query the port number to use
# -------------------------------------------------

# prompt the user
port_number = prompt("which port would you like to use?")

# prompt the user with defaults and validation
port_number = prompt("which port?", default=42, validator=int)


# ------------------------------------------------------
# using the 'reboot' function to rebot a remote system
# by defaults.. it waits for 120seconds i.e 2minuets
# ------------------------------------------------------

# reboot the remote system
reboot()

# reboot in 30 seconds
reboot(wait=30)


# ---------------------------------------------------------
# 'cd' context manager allows keeping the directory state (i.e. where the following block of comments are to be executed).
# It is similar to running the cd command during an SSH session and running various different commands.
# -------------------------------------------------------------
# The *cd* context manager makes enwrapped command's
# execution relative to the stated path (i.e. "/tmp/trunk")
with cd("/tmp"):
    with cd("/trunk"):
        run("ls")


# ------------------------------------------------------------
# the 'lcd' context manager (local cd) works very simillar to the above state, however.. it only affects the local systems state.
# ------------------------------------------------------------

# Change the local working directory to project's
# and upload a tar archive
with lcd("~/projects/my_project"):
    print("Uploading the project archive")
    put("app.tar.gz", "/tmp/trunk/app.tar.gz")


# --------------------------------------------------------------
# 
# --------------------------------------------------------------
