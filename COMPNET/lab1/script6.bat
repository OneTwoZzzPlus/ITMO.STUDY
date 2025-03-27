@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

:: Считываем параметры
set "mode=%~1"
set "interface=%~2"
set "address=%~3"
set "mask=%~4"
set "gateway=%~5"
set "dns=%~6"

:: Выбор режима
:choose_mode
if /i "%mode%"=="exit" goto end
if /i "%mode%"=="?" goto help
if /i "%mode%"=="/?" goto help
if /i "%mode%"=="help" goto help
if /i "%mode%"=="dhcp" goto check_interface
if /i "%mode%"=="static" goto check_interface

:invalid_mode
echo Неверный режим: "%mode%"
set "mode="
set /p "mode=Выберите режим (dhcp|static|help|exit): "
goto choose_mode

:: Проверка интерфейса
:check_interface
if "%interface%"=="" goto request_interface

netsh interface show interface "%interface%" >nul 2>&1
if %errorlevel% neq 0 (
    echo Ошибка: Интерфейс "%interface%" не найден!
    set "interface="
    goto request_interface
) else (
    goto process_mode
)

:request_interface
set /p "interface=Введите название интерфейса: "
goto check_interface

:: Обработка режима
:process_mode
if /i "%mode%"=="dhcp" (
    echo Настройка по DHCP...
    netsh interface ip set address name="%interface%" source=dhcp
    netsh interface ip set dns name="%interface%" source=dhcp
    goto result_check
)

:static_mode
echo Режим статической настройки

:: Ввод IP
:get_ip
if "%address%"=="" (
    set /p "address=Введите IP-адрес: "
    goto get_ip
)

:: Ввод маски
:get_mask
if "%mask%"=="" (
    set /p "mask=Введите маску подсети: "
    goto get_mask
)

:: Ввод шлюза
:get_gateway
if "%gateway%"=="" (
    set /p "gateway=Введите основной шлюз: "
    goto get_gateway
)

:: Ввод DNS
:get_dns
if "%dns%"=="" (
    set /p "dns=Введите DNS-сервер: "
    goto get_dns
)

:: Применение настроек
echo Применение заданных параметров...
netsh interface ip set address name="%interface%" source=static address="%address%" mask="%mask%" gateway="%gateway%"
netsh interface ip set dns name="%interface%" static "%dns%"

:result_check
echo Результат:
netsh interface ip show config name="%interface%"
goto end

:: Справка
:help
echo Автоматическая настройка:  %~nx0 dhcp "Имя интерфейса"
echo Пример ручной настройки:   %~nx0 static "Имя интерфейса" 192.168.1.77 255.255.255.0 192.168.1.1 8.8.8.8
echo В интерактивном режиме просто введите нужные параметры по запросу.

:end
endlocal