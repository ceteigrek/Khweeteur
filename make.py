#!/usr/bin/python
# -*- coding: utf-8 -*-
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published
## by the Free Software Foundation; version 2 only.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
import pypackager
import os
import khweeteur

if __name__ == "__main__":
    try:
        os.chdir(os.path.dirname(sys.argv[0]))
    except:
        pass

    p=pypackager.PyPackager("khweeteur")
    p.version=khweeteur.__version__
    p.buildversion='1'
    p.display_name='Khweeteur'
    p.description="Khweeteur is a small twitter client for Maemo and MeeGo. It showing DMs, mentions and the follower timeline in one window, with a subsequent window for each search. Maemo's notification system is supported, as is auto-update and themeing.""
    p.author="Benoit HERVIER"
    p.maintainer="Khertan"
    p.email="khertan@khertan.net"
    p.depends = "python2.5-qt4-gui,python2.5-qt4-core, python2.5-qt4-maemo5, python-oauth2, python-simplejson, python-conic, python-imaging"
    #p.depends = "python2.5-qt4-experimental-gui,python2.5-qt4-experimental-core, python2.5-qt4-experimental-maemo5, python-oauth2, python-simplejson, python-conic, python-imaging"
#    p.suggests = ""
    p.section="user/network"
    p.arch="armel"
    p.urgency="low"
    p.bugtracker='http://khertan.net/khweeteur/bugs'
    p.distribution="fremantle"
    p.repository="extras-devel"
    p.icon='khweeteur.png'
    p["/usr/bin"] = ["khweeteur_launch.py",]
    p["/usr/share/dbus-1/services"] = ["khweeteur.service",]
    p["/usr/share/pixmaps"] = ["khweeteur.png"]
    p["/usr/share"] = ["icons/hicolor/32x32/apps/khweeteur.png","icons/hicolor/64x64/apps/khweeteur.png","icons/hicolor/128x128/apps/khweeteur.png"]
    p["/usr/share/applications/hildon"] = ["khweeteur.desktop",]
    files = []
    
    #Src
    for root, dirs, fs in os.walk('/home/user/MyDocs/Projects/khweeteur/khweeteur'):
      for f in fs:
        #print os.path.basename(root),dirs,f
        prefix = 'khweeteur/'
        if os.path.basename(root) != 'khweeteur':
            prefix = prefix + os.path.basename(root) + '/'
        #print os.path.splitext(f)[1]
        if ((os.path.splitext(f)[1] not in ('.pyc','.pyo')) and (os.path.basename(f) not in ('profile.py','pstats.py','get_access_token.py') )):
            files.append(prefix+os.path.basename(f))
    print files

    
    p["/usr/lib/python2.5/site-packages"] = files

    p.postinstall = """#!/bin/sh
chmod +x /usr/bin/khweeteur_launch.py
python -m compileall /usr/lib/python2.5/site-packages/khweeteur
rm -rf /home/user/.khweeteur/"""

    p.changelog=""" Change ctrl-a (reply) for ctrl-m, prevent auto focus to catch up and down to scroll in list
"""
    p.upgrade_description = p.changelog

print p.generate(build_binary=True,build_src=True)
#print p.generate(build_binary=True,build_src=True)
