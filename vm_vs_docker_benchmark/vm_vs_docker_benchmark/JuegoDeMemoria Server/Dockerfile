# Usa una imagen simple de servidor web
FROM nginx:alpine

# Elimina la página por defecto de Nginx
RUN rm /usr/share/nginx/html/*

# Copia tu juego al directorio web de Nginx
COPY index.html /usr/share/nginx/html/index.html
