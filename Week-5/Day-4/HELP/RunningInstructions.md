## Install mkcert

```
sudo apt install libnss3-tools mkcert
mkcert -install
```

## Configuring Local Domain

Edit /etc/hosts:

```
127.0.0.1 practice.local
```

## Generate SSL Certificates

```
mkcert practice.local localhost 127.0.0.1
```

## Run Containers

```
docker compose up --build -d
```

## Verification

Open browser:

```
https://practice.local
```
