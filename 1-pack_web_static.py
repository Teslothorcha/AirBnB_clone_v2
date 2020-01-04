#!/usr/bin/python3
""" create a tar file """


import tarfile
import os
from datetime import datetime


def do_pack():
    """ check files an create actual tar"""
    dirr = "versions/"
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    f_name = web_static + date_time + '.tgz'
    final_file = dirr + f_name

    if not os.path.exists(dirr):
        os.mkdir(dirr)
    with tarfile.open(dirr + f_name, "w:gz") as tar:
        tar.add("web_static", arcname=os.path.basename("web_static"))
    if os.path.exists("final_file"):
        return final_file
    else:
        return None
