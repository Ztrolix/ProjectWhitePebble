@echo off
title Python Installer
cls
color 0a

py -m pip install pyuac --user
py -m pip install pypiwin32 --user
py -m pip install zipfile --user
py -m pip install requests --user
py -m pip install shutil --user
py -m pip install os --user
py -m pip install time --user