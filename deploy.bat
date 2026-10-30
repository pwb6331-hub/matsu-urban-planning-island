@echo off
chcp 65001 >nul
echo ========================================================
echo   一鍵部署 / 同步更新至 GitHub Pages
echo ========================================================
cd /d "%~dp0"
git add -A
git commit -m "chore: update 3D island web app"
git push origin main
echo.
echo 部署完成！請等待約 1-2 分鐘，即可於 GitHub Pages 查閱最新版本：
echo https://pwb6331-hub.github.io/matsu-urban-planning-island/
pause
