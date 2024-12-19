# Fill unit path with pwd
sudo sed -i "s|^WorkingDirectory=.*|WorkingDirectory=$(pwd)|" deploy/fastapi-app.service
sudo sed -i "s|^User=.*|User=$(whoami)|" deploy/fastapi-app.service

sudo cp deploy/fastapi-app.service /etc/systemd/system/fastapi-app.service

sudo systemctl daemon-reload
sudo systemctl enable fastapi-app.service
sudo systemctl start fastapi-app.service
sudo systemctl status fastapi-app.service
