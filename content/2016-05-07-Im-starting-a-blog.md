Title:    I'm starting a blog
Tags:     DevOps, Pelican
Category: blog
Authors:  Bjarni Jens Kristinsson

When you're working on a project you need to take notes. And when your project revolves around servers, networking and self-hosting services you may as well set up your own blog.

And so I did just that.

### Picking a framework

I could easily have chosen a blogging platform such as [Blogger](https://www.blogger.com/), [Ghost](https://ghost.org/) or [Medium](https://medium.com/) to save me all the hazzle. However, I'm curious about servers, networks and infrastructure so I took this chance to set up and host my own blog. It's a healthy experience for every Software Developer to do Operations from time to time. Eventually, if I get fed up on managing my own server I'll move the blog to some hosted platform.

I started looking around to see what other people did for their blog. At first I though about installing a fully blown CMS system on my server (inside a container or virtual machine) such as [WordPress](https://wordpress.org/). I was very close to [self-hosting Ghost](http://support.ghost.org/developers/) after reading [Anmol Jagetia's Blog](https://blog.anmoljagetia.me/why-ghost/). The biggest pro's of a CMS system is the ability to write your blog in a simple WYSIWYG fashion from whatever computer you're using. But in the end I decided to go for a static blog site generator framwork without any server-side logic. Comments would be handled by [Disqus](https://disqus.com/) plugin.

I searched for and stumbled upon three strong candidates: [Jekyll](https://jekyllrb.com/), [Pelican](http://blog.getpelican.com/) and [Utterson](https://github.com/stef/utterson). Jekyll seems to be the most active project and is amongst other things [powering GitHub Pages](https://jekyllrb.com/docs/github-pages/) behind the scenes. Utterson is very simple and elegant and uses Unix shell scripting instead of high-level programming languages. I tried all three and ended on choosing Pelican mainly because I found [a beautiful theme](https://blog.alexandrevicenzi.com/flex-pelican-theme.html) and it was the easiest to configure.

### Hosting the blog

So now the process is this: I write my blogposts in Markdown on my laptop, then I render them to HTML with Pelican, commit and push them to my [GitHub repository](https://github.com/bjk17/blog) and then finally ``git pull`` them on my server. The process is a bit more manual then I'd prefer as I don't have direct SSH access to where I host my blog site. (I serve it from an LXC/LXD container behind an Apache proxy, but more on that later.) Pelican has built-in deployment tools that can render and deploy directly to your server over SSH. I would need to change my server infrastructure to be able to deploy in this way. This is something I will think about. It's ugly and *semantically incorrect* (I'll be using this phrase a lot) to keep both the markdown files and the rendered HTML in source control. 

In the next few blog posts I want to write about my current server architecture/infrastructure hobby project and all the technical tidbits related to that. After all, that's why I started this blog.

I appreciate all kinds of feedback so please drop a comment or send me an email if you like what I'm dealing with or have something to say.
