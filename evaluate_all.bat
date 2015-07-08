@echo off

setlocal enabledelayedexpansion
for %%f in (*.dat) do (
	set aa=%%f
	set front=!aa:~0,-4!
	copy %%f sigsa.dat >nul
	ping 192.0.2.2 -n 1 -w 1000 > nul
	sigsa00b.exe >nul
	if %ERRORLEVEL% == 0 (
		echo %%f - all OK
		) else (
		echo %%f - ERROR
		)
	mv sigsa.res !front!.rec
	mv sigsa.mic !front!.mic
	del sigsa.dat
)

endlocal