Title:    My hobby project
Tags:     DevOps, infrastructure
Category: my NUC as a server
Authors:  Bjarni Jens Kristinsson

So, the main idea behind this blog is to write about what I've done and what I'm about to with this hobby project of mine.

In a nutshell, I want to learn about Linux, servers, networking, infrastructure and all the best-practises there is to set up and manage my own servers and infrastructure.

### The inspiration

In my undergraduate studies I wrote a [research thesis](http://skemman.is/handle/1946/22017) on *occurrence graphs* under the guidance of [Henning Ulfarsson](http://ulfarsson.github.io/research.html) from Reykjavik University. Our work could be categorized as [experimental mathematics](https://en.wikipedia.org/wiki/Experimental_mathematics) because of it's heavy reliance on computer analysis. To get a feeling for our new objects and mathematical structures we often wrote simple programs that looped over millions and billions and even trillions (that's a whopping $10^{12}$) of permutations to do some simple computations and then aggregate the results over the permutations to a sequence of numbers, something that we have [a much better understanding of](https://en.wikipedia.org/wiki/Sequence).

What I realized then, and have not stopped thinking about, is how extremely parallell these computations were. Today, all the rage is about [programming on the graphics processing units](https://en.wikipedia.org/wiki/General-purpose_computing_on_graphics_processing_units) (GPUs) for parallel tasks. It's all well and good when you have a [shared memory model](https://en.wikipedia.org/wiki/Shared_memory), but what if all your parallel tasks can work completely on their own on completely different computers and needed just a simple and short job description? In my and Henning's scenario the job description would only have been a few bytes, given the other computers would have the necessary libraries to do the calculations. I think [Bitcoin mining pools](http://www.coindesk.com/information/get-started-mining-pools/) works this way.

My inspiration is to learn enough to be able to *expand* my computer and it's computing capabilities to another machine. Eventually I'd be able to [scale my computer horizontally](https://en.wikipedia.org/wiki/Scalability#Horizontal_and_vertical_scaling) to more computers, over the internet, all over the world.

I want to poke around to see what's possible and what's not.

### So I need another computer

My first step must therefore be to set up my own server that I can experiment with. And in line with my mathematical background, I want to do it *the right way*.

I've been tinkering with Linux servers for the last 3-4 years now. I own several Raspberry Pi's and other [single-board computers](https://en.wikipedia.org/wiki/Single-board_computer) that I've used, among other things, as web servers. I've earned some experience at my work for [WuXi NextCODE](https://www.nextcode.com/) where I often have to debug Linux server errors.

But I didn't want to set up another handicapped low-performing Raspberry Pi. Instead I chose to relocate my [Intel NUC](http://www.intel.com/content/www/us/en/nuc/nuc-kit-d54250wykh.html) with a 15W [Intel Core i5-4250U](http://www.cpubenchmark.net/cpu.php?cpu=Intel+Core+i5-4250U+%40+1.30GHz) processor, [128GB Crucial M550 mSATA](http://ssd.userbenchmark.com/SpeedTest/12612/Crucial--CT128M550SSD3) SSD, 2TB spinning HDD (taken from a [Seagate's Backup Plus Portable Drives](http://www.seagate.com/gb/en/products/laptop-mobile-storage/laptop-external-drives/backup-plus/) unit) and [16GB DDR3L 1600MHz memory](http://www.pc-specs.com/ram/Crucial/Crucial_BLS2C8G3N169ES4CEU_Arbeitsspeicher_16GB_Kit_(Zwei_8GB_RAMs)_DDR3-RAM/322) from Crucial.

I put my NUC under the TV and plugged it into the router. In the following blog posts I'll write about how I wanted the server to turn out and what I managed to do in my first attempt.

![My NUC and my router]({filename}/static/IMG_1295.jpg)
