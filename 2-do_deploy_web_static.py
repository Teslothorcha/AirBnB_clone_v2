#!/usr/bin/python3
""" create a tar file """

from fabric.api import *
import os
from datetime import datetime


env.hosts = ["35.196.254.124", "34.73.182.187"]
env.user = "ubuntu"


def do_pack():
    """ check files an create actual tar"""
    dirr = "versions/"
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    f_name = "web_static" + date_time + '.tgz'
    final_file = dirr + f_name
    try:
        if not os.path.exists("versions"):
            print("aca")
            local("mkdir versions")
        local("tar -zcvf {tar_name} web_static".format(tar_name=final_file))
        return final_file
    except:
        return None

def do_deploy(archive_path):
    """ distribute archive thorugh servers """
    if not os.path.exists(archive_path):
        return False

    fex = archive_path.replace("versions/", "")
    file_name = archive_path.replace("versions/", "").replace(".tgz", "")
    dir_name = "/data/web_static/releases/" + file_name

    put(archive_path, "/tmp")
    run("sudo mkdir -p {new_dir}/".format(new_dir=dir_name))
    run("sudo tar -xzf /tmp/{fi} -C {di}".format(fi=fex, di=dir_name))
    run("sudo rm /tmp/{fi}".format(fi=fex))
    run("sudo mv {di}/web_static/* {di_n}/".format(di=dir_name, di_n=dir_name))
    run("sudo rm -rf {di}/web_static".format(di=dir_name))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {di} /data/web_static/current".format(di=dir_name))
    return True
