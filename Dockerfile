FROM nginx:alpine
RUN echo "<h1>Praktikum Cloud Computing - Modul 2</h1>" > /usr/share/nginx/html/index.html
EXPOSE 80
