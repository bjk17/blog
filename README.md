# blog.bjk.is

A personal blog about my adventures with technology using [Pelican](http://blog.getpelican.com/) and [Flex](https://blog.alexandrevicenzi.com/flex-pelican-theme.html).

## developing

Run ``make devserver`` from project root and open http://localhost:8000 in browser. Then you can edit content and/or config files but you need to reload web page to see the changes.

## deploying

Clone this repo on production server, run ``make publish`` and serve the static ``output/`` folder.