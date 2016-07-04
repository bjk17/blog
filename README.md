# blog.bjk.is

A personal blog about my adventures with technology using [Pelican](http://blog.getpelican.com/) and [Flex](https://blog.alexandrevicenzi.com/flex-pelican-theme.html).

## developing

To view the blog run ``make devserver`` from project's root and open [http://localhost:8000]() in browser. You can edit content and/or config files but you need to reload web page to see the changes.

When happy, commit and push files and/or changes in ``content`` folder to the git repo.

## deploying

I'm serving this in a Linux Container on Ubuntu 16.04 behind an Apache web server. Pip needs to be installed with ``apt install python-pip``.

I checked out this repo under ``/var/www/blog.bjk.is``. In the very beginning I needed to run the following from the repo

````bash
git submodule init
git submodule update
pip install -r requirements.txt
````

After updates I need to build the output folder on the server. From the repo's root I run ``git pull && make publish``.