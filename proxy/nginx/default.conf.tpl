#server {
#    listen 80;
#    server_name ${DOMAIN} www.${DOMAIN};
#
#    location /.well-known/acme-challenge/ {
#        root /vol/www/;
#    }
#
#    location / {
#        return 301 https://$host$request_uri;
#    }
#}


# for dev purposes
server {
    listen 80;
    server_name 127.0.0.1;
    location /media/ {
        root /var/html/;
    }
    location /static/ {
        root /var/html/;
    }

    location / {

        proxy_pass http://${APP_HOST}:${APP_PORT};

    }
}
#server {
#    listen 81;
#    server_name 127.0.0.1;
#    location /media/{
#        root /var/html/pd/;
#    }
#    location /static/ {
#        root /var/html/pd/;
#    }
#
#    location / {
#
#        proxy_pass http://pd_web:8000;
#        include proxy_params;
#    }  
#}
