#!/bin/sh

# Generate Certificate and Private Keys
openssl req -x509 -newkey rsa:4096 -keyout certs/key.pem -out certs/cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=localhost"

# Generate DH Params
openssl dhparam -out certs/dhparam.pem 2048