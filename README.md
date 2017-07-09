# blog.bjk.is

A personal blog about my adventures with technology using [Pelican](http://blog.getpelican.com/) and [Flex](https://blog.alexandrevicenzi.com/flex-pelican-theme.html).


## dependencies

Pelican is a Python Pip package and is needed to generate the static HTML from the Markdown source content. Either install Pip on your local development machine and run `pip install -r requirements.txt` (preferably using `virtualenv` or use the custom built Docker image [bjarnijens/pelican](requirements.txt). If you decide to use the Docker image you need to prefix every command below with

````bash
docker run -it --rm -u=$(id -u `whoami`):$(id -g `whoami`) -p=8000 -v=`pwd`:/blog:rw -w=/blog bjarnijens/pelican
````


## developing

To view the blog run ``make devserver`` from project's root and open [http://localhost:8000]() in browser. You can edit content and/or config files but you need to reload web page to see the changes.

When happy, commit and push files and/or changes in ``content`` folder to the git repo.


## deploying

I'm serving this Ubuntu 16.04 VPS running NGINX web server. I'm not installing Pelican on the host but rely on git and Docker as the only dependencies. 

````bash
git clone https://github.com/bjk17/bjk.is.git /var/www/bjk.is
cd /var/www/bjk.is

git submodule init
git submodule update

````

We've yet to generate the static HTML from the source content. We will use the Docker image to do that. And these are the same commands as when updating the site so I'll add it as an alias on the host.
````bash
echo "alias update-bjk.is='docker run -it --rm -u=$(id -u `whoami`):$(id -g `whoami`) -p=8000 -v=`pwd`:/blog:rw -w=/blog bjarnijens/pelican bash -c \"git pull; make publish\"'" >> ~/.bash_aliases
source ~/.bash_aliases
update-bjk.is
````

Lastly we configure NGINX and add a valid SSL certificate from Let's Encrypt (which I've already installed on the host).
````bash
echo """
server {
    listen 80;
    server_name blog.bjk.is;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl;
    server_name blog.bjk.is;

    root /var/www/blog.bjk.is/output;

    ssl on;
    ssl_certificate         /etc/letsencrypt/live/blog.bjk.is/cert.pem;
    ssl_certificate_key     /etc/letsencrypt/live/blog.bjk.is/privkey.pem;
    ssl_trusted_certificate /etc/letsencrypt/live/blog.bjk.is/fullchain.pem;
}
""" > /etc/nginx/sites-available/blog.bjk.is
ln -s /etc/nginx/sites-available/blog.bjk.is /etc/nginx/sites-enabled/blog.bjk.is
service nginx stop
letsencrypt certonly --standalone -d blog.bjk.is
service nginx start
````
