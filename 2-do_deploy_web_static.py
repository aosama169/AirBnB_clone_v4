#!/usr/bin/python3
"""
Fabric script to archive web_static files to web server
"""
from fabric.api import local


def do_deploy(archive_path):
    """
    distribute archive web_static from do_pack() to web server
    """
    if archive_path is None:
        return False
    return True
