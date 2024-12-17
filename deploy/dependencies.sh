# Installs Dependencies: Make, Docker Engine and Docker compose Addon

# 1: Make
if ! command -v make &> /dev/null; then
    sudo apt install -y make
fi

# 2: Docker Engine
if ! command -v docker &> /dev/null; then
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install -y ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    # Install Docker Engine
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
fi

# 3: Docker compose
if ! command -v docker compose &> /dev/null; then
    sudo apt-get install -y docker-compose-plugin
fi
