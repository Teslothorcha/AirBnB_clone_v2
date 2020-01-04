#!/usr/bin/python3
""" create a tar file """

from fabric.api import local
import os
from datetime import datetime


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
