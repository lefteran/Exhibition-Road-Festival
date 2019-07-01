@echo off

for /l %%x in (1, 1, 100) do (
	python prepareData.py
	git add trafficData.json
	For /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
	git commit -a -m "batch upload 28_6" 
	git push
	)