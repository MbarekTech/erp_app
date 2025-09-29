@echo off

echo Installing SDRT app...

REM Get the container ID for the backend service
for /f "tokens=*" %%i in ('docker-compose ps -q backend') do set CONTAINER_ID=%%i

if "%CONTAINER_ID%"=="" (
    echo Error: Backend container not found. Make sure the Docker setup is running.
    exit /b 1
)

echo Found backend container: %CONTAINER_ID%

REM Install the SDRT app
echo Step 1: Getting SDRT app from GitHub...
docker exec -it %CONTAINER_ID% bench get-app --branch main https://github.com/MbarekTech/erp_app.git

echo Step 2: Installing SDRT app on the site...
docker exec -it %CONTAINER_ID% bench --site frontend install-app sdrt

echo Step 3: Restarting services...
docker-compose restart backend frontend

echo SDRT app installation completed!
echo You can now access your site at http://localhost:8080
echo Login with: Administrator / 123456@info

pause

