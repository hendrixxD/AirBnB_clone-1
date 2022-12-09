from fabric.api import *

env.hosts = ['ubuntu@3.234.25.224']

def copy():
    # make a directory
    run('mkdir -p /home/ubuntu/fabfile')

    # upload file from a remote serevr to a local serber
    put('fabfile.py', '/home/ubuntu/fabfile')
