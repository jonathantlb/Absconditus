@echo off
chcp 65001 >nul
title Absconditus - Servidor Local
echo ==========================================
echo   ABSCONTIDUS - SERVIDOR LOCAL
echo ==========================================
echo.
echo Iniciando servidor em http://localhost:8080
echo.
echo Acesse pelo navegador:
echo   http://localhost:8080/tela-inicial.html
echo.
echo Pressione Ctrl+C para parar o servidor.
echo ==========================================
echo.
python -m http.server 8080

pause
