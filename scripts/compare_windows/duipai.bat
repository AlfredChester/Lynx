@echo off
mk.exe>tmp.in
1.exe<tmp.in>tmp1.out
2.exe<tmp.in>tmp2.out
fc /w tmp1.out tmp2.out
if errorlevel == 1 pause
%0