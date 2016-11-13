Title:    Server version 0.2 -- Webservice infrastructure
Tags:     DevOps, infrastructure, LXD
Category: my NUC as a server
Authors:  Bjarni Jens Kristinsson

I own the domain bjk.is which I want to use to host various webservices under different subdomains. I currently have DNS records for bjk.is, blog.bjk.is and bio.bjk.is which I'm using to serve three independent web applications. Two of them are static HTML sites and one is driven by a Django backend.

At work I whould be able to start three instances in AWS, each with their own public IP address, and deploy the webapplications to their own seperate instances. I whould then configure the three DNS entries to resolve to their respective IP addresses, see diagram below.

![AWS three servers]({filename}/static/AWS_three_servers.png)

This approach is however not possible with my NUC server as I only have one public IP address to play with. Thus all my different DNS entries must point to the same IP address and my NUC must therefore determine what webapplication to serve based on the URL used to connect to it. This is shown in the following diagram.

![NUC one server]({filename}/static/NUC_one_server.png)

The routing logic happens in software on my NUC, contrary to happening in hardware on network switches in the AWS scenario. Before I decided to use my NUC as a server I was hosting my websites on a Raspberry Pi (RPi) using Apache's [Virtual Hosts](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-16-04) to serve different sites based on the URL in the HTTP headers. I had all the static HTML sites on the same filesystem on my main RPi webserver, but the Django website was running on another RPi on my home network. One of the virtual hosts on the main RPi was a proxy to the second RPi that were running Apache on it's own to serve the dynamic site. I did this partly because I liked the segregation, but mainly because we were actively working on the Django project and used the second RPi as a development server so it made sense to isolate it from my stable webserver.

### The limitation of Virtual Hosts

There are two problems that virtual hosts do not solve on their own. One of them being that it's designed to serve only HTTP traffic (ports 80 and 443) but not general web traffic. For example, I wouldn't set up a VPN server as a virtual host as it is a completly different webservice speaking a completely different protocol. I would therefore need to run some other logic on my NUC to handle the traffic to vpn.bjk.is correctly and then I could just as well use that for all web traffic.

The other one is that virtual hosts are not a solution on how to isolate the webservices from one another. This is actually one of the key benefits to the AWS scenario from the beginning of this post. I don't want the unstable Django development environment to be able to delete a configuration file for another webservice located on the shared filesystem. They should be plug&play independant from each other. If I set up OwnCloud and decide I don't like it I need to be confident that I can scrap it without leaving a trace behind. That's the only way to run a stable server in my opinion.

### VMs and containers

I do like the segregation from the AWS scenario. It truly isolates the webservices from each other and makes them plug&play compatible by deleting and creating different instances. I believe this is the semantically correct thing to do, and I would like to be able to mimic this segregation on my NUC by using different URLs as I would use different IP addresses in the AWS scenario.

Behind the scenes the instances on AWS are simply virtual machines (VMs) running on a very very large cluster of servers. I can spin up instances of different sizes, ranging from one core machines with half a gigabyte of memory, up to instances with tens or even hundreds of CPU cores with memory in the range of tens, hundreds and even thousands of gigabytes. With my NUC, I may be limited by hardware, but it has 2 cores (4 threads) and 16GiB of RAM which I can split between at least a few VMs.

I've been using [VirtualBox](https://www.virtualbox.org/) on my laptop for many years but its GUI approach focuses on running and interacting with Desktop OS's rather then headless servers (though to be fair, it's capable of it). I've heard of virtualization techniques such as [KVM](http://www.linux-kvm.org/) and [QEMU](http://wiki.qemu.org/) and was interested in poking around with them to see how they'd fit for me and my hobby project. I wanted something with good command line support to be easily able to script the creation/destruction of VMs and even plug some Web UI in front of that later. Then there are application containers such as [Docker](https://www.docker.com/) and [rkt](https://coreos.com/rkt/) for deploying applications such as my web apps mentioned above.

But at that time Canonical was releasing Ubuntu 16.04 and talking a lot about [Linux containers (LXC)](https://linuxcontainers.org/) and their container "hypervisor" called [LXD](http://www.ubuntu.com/cloud/lxd). It was getting a version bump to 2.0 and they offered some [online hands-on experience](https://linuxcontainers.org/lxd/try-it/) and detailed [blog posts](https://www.stgraber.org/2016/03/11/lxd-2-0-blog-post-series-012/) for interested people like me.

For me this seemed like a good middle road of having a whole OS without having to reserve hardware resources as VirtualBox does. The "machines" started up through LXD acted as VMs but shared the Linux kernel with the host and where thus much ligther to run for my NUC. Being a Ubuntu fan I decided to pick LXD as my tool of choice to experiment with the AWS feature of "spinning up instances" to run tasks and services.

### Installing and configuring LXD

I strongly suggest that readers follow [Stéphane Graber's blog post](https://www.stgraber.org/2016/03/15/lxd-2-0-installing-and-configuring-lxd-212/) on how to install and configure LXD with some proper step-by-step instructions and explanations. But in a nutshell, it can be as easy as:

    :::bash
    ## Install LXD and the ZFS filesystem as storage backend
    sudo apt install lxd zfsutils-linux
    sudo lxd init

The last command configures LXD by asking a wide range of questions regarding storage backend, network configuration and probably something else that I don't remember at the moment. Unfortunatly for this blog post I did not note down my answers but I do know that I did end up with a 20GiB ZFS pool called ``zfs-lxd-pool`` as storage backend. It would maybe have been cleaner to partion my SSD and use a partition as a storage backend, but that would probably have meant that I would have to allocate storage for it instead of being able to share the SSD between the host and the containers as I do now.

By default, LXD instances resides on a seperate subnet under the host, with only HTTP traffic being proxied to the containers. However, I wanted a more VM-like experience and after reading [an article](https://insights.ubuntu.com/2016/04/07/lxd-networking-lxdbr0-explained/) from Ubuntu explaining the default lxdbr0 bridge I did the following to make the containers appear on my local net with their own IP addresses:

    :::bash
    # LXD/LXC machines on same local network as NUC (the host)
    lxc profile device set default eth0 parent eno1 #eno1 being NUC’s interface
    lxc profile device set default eth0 nictype macvlan

To show you what I mean let's look at the following demo:

    :::bash
    bjarni@nuc:~$ lxc launch ubuntu:16.04 a-temporary-container
    Creating a-temporary-container
    Starting a-temporary-container
    bjarni@nuc:~$ lxc list
    +-----------------------+---------+----------------------+------+------------+-----------+
    |        NAME           |  STATE  |         IPV4         | IPV6 |    TYPE    | SNAPSHOTS |
    +-----------------------+---------+----------------------+------+------------+-----------+
    | a-temporary-container | RUNNING | 192.168.0.118 (eth0) |      | PERSISTENT | 0         |
    +-----------------------+---------+----------------------+------+------------+-----------+
    
What I did was to start a new container named *a-temporary-container* running Ubuntu 16.04. The second command shows that the LXD network configuration from above was successful -- the IP address ``192.168.0.118`` is on my local net. This means I can make the container accessible from the internet by adding a NAT rule in my router, forwarding some port on it to a port on the container. We clean up after ourselves by stopping and deleting the container. This leaves absolutely no trace behind.

    :::bash
    bjarni@nuc:~$ lxc stop a-temporary-container
    bjarni@nuc:~$ lxc delete a-temporary-container
    bjarni@nuc:~$ lxc list
    +---------+---------+----------------------+------+------------+-----------+
    |  NAME   |  STATE  |         IPV4         | IPV6 |    TYPE    | SNAPSHOTS |
    +---------+---------+----------------------+------+------------+-----------+
