@echo off
title JAR Runner
cls
:start

set /p %jar%=JAR LOCATION: 
java -jar %jar%.jar

TIMEOUT /T 30