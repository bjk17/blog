Title:    What I'm aiming for
Modified: 2016-05-23
Tags:     DevOps, infrastructure, Ubuntu
Category: my NUC as a server
Authors:  Bjarni Jens Kristinsson

Before I moved my NUC I had two Raspberry Pis (web server and [XBMC/Kodi](https://kodi.tv/) media player) and one [Cubietruck](http://docs.cubieboard.org/tutorials/cubietruck/start) (NFS server) under the TV. The NUC will take over those tasks and provide me with better hardware to test new *features*. As I'm living in a small studio apartment with my girlfriend I'll try my best to keep it as silent as its predecessors.

### A server and HTPC

My NUC will not only be a server. I'm taking down the RPi running Kodi and connecting the HDMI cable to the NUC instead. I want to be running a whole DE (Desktop Environment) both for when I turn on the TV and also to have a remote desktop I'd be able to connect to over the internet. Sure, I can do most of the stuff through SSH, but this is one aspect of "poking around with" I'd like to try out.

I'm going to install Ubuntu 16.04 and I need to chose between installing the server version and applying the ``ubuntu-desktop`` package on top, or installing Ubuntu Desktop and configure server packages afterwards. The semantically correct way would be to install Ubuntu Server and run the DE as a secure and isolated service. I even posted [a question on Askubuntu](http://askubuntu.com/questions/765612/running-ubuntu-desktop-in-lxc-lxd-on-top-of-ubuntu-server/) wether this was possible using Linux containers (LXC) but haven't gotten any helpful responses yet.

### Monitoring

I'm using this opportunity to build my server [bottom-up](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design). I think that's the right way to build quality software and infrastructure. That means that after I've installed the OS the first thing I should do (after securing SSH) is to set up some kind of monitoring.

My main points of interest are physical monitoring such as temperature of core components and frequencies of fan and CPU. I want to be well aware of hardware utilization such as SSD/HDD free space and IO, memory usage and network IO. I'm very curious of power usage but it seems I can't read out those stats from the OS unless I buy some kind of (smart) power meter to plug into the wall. When I used a Linux laptop I could read the Watt usage straight from the battery.

On top of these core metrics there are some extra bits of information I'd like to have displayed on the dashboard. F.ex. how many SSH sessions are currently open, is the HDD in active or standby state, how long since I last rebooted? These are basically metrics that I can produce with simple commands or shell scripts. Later I could add application monitoring for websites and other software I'd be running on the NUC. 

The dashboard would be presented as a website that would be served on an obscure port on the NUC that would not be open to the internet (because this is sensitive information). However, I would be able to view it on my local net as well as remotely by setting up [SSH port forwarding](https://help.ubuntu.com/community/SSH/OpenSSH/PortForwarding). 

### Web services

I own the domain bjk.is which I will use to connect to the machine and host my main personal website. I will add additional DNS entries beta.bjk.is, bio.bjk.is and now blog.bjk.is for my different subsites (some in collaboration with others). I would like to do that the right way by isolating the websites from the core server and implement them as "detachable components".

At NextCODE we use [Amazon Web Services](https://aws.amazon.com/) (AWS) quite a lot. We also manage our own infrastructure with software from [VMware](https://www.vmware.com/) and [Greenqloud](https://www.greenqloud.com/). Both AWS and Greenqloud's [Qstack](https://www.qstack.com/) have web-based interfaces (as well as scriptable API's) where we can create and start virtual machines (VM) with a public IP address and configurable amount of CPU cores, RAM and storage.

This sort of [infrastructure as a service](https://en.wikipedia.org/wiki/Cloud_computing#Infrastructure_as_a_service_.28IaaS.29) (IaaS) is what I aim for when setting up the NUC. There are a lot of limitations, though, as I only have one physical computer and one public IP address to work with. But to some degree I can seperate websites and other processes into pluggable independent containers or VMs that won't affect each other.

### Network-attached storage (NAS)

The underlying server OS have direct access to all the hardware, including the 2TB spinning HDD with all my data (don't worry, I do backups). Therefore, the server OS should also be responsible of exposing and sharing the data with all parties involved. The media player in the DE needs access to it, my other computers on the home network do so too and maybe some future application running on NUC as well. When I'm not at home I want to be able to mount the data drive over the internet. The SSD is dedicated for the OS and other software whether it's core server or running inside containers/VMs.

In the next blog post(s) I'll write about what feature boxes I managed to tick and how I implemented them.
