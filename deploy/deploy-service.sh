# Fill unit path with pwd
sudo sed -i "s|^WorkingDirectory=.*|WorkingDirectory=$(pwd)|" /etc/systemd/system/fastapi-app.service

sudo systemctl daemon-reload
sudo systemctl enable fastapi.service
sudo systemctl start fastapi.service.service
sudo systemctl status fastapi.service.service
