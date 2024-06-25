#!/usr/bin/python3
"""
The Fabric script to create distribute archive web_static to web server
"""
from fabric.api import local
do_pack = __import__('1-pack_web_static').do_pack


def do_deploy():
    """
    The creates distributes archive web_static to web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return True
