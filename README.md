# blog.bjk.is

A personal blog about my adventures with technology using [Pelican](http://blog.getpelican.com/) and [Flex](https://blog.alexandrevicenzi.com/flex-pelican-theme.html).

## developing

Run ``make devserver`` from project root and open http://localhost:8000 in browser. Then you can edit content and/or config files but you need to reload web page to see the changes.

## deploying

Run ``make publish`` and commit the ``output/`` folder as well as source code. Clone this repo on production server and serve the ``output/`` folder.