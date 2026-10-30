@echo off
chcp 65001 >nul
echo ========================================================
echo   啟動本地 Web 伺服器 (供手機、平板同區網測試或桌機預覽)
echo ========================================================
echo 本地存取網址: http://localhost:8080/
start http://localhost:8080/
python -m http.server 8080 --directory "%~dp0"
pause
