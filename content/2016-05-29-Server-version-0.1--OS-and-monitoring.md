Title:    Server version 0.1 -- OS and monitoring
Modified: 2016-07-04
Tags:     DevOps, infrastructure, Ubuntu, monitoring, netdata
Category: my NUC as a server
Authors:  Bjarni Jens Kristinsson

I chose to download and install Ubuntu Desktop 16.04 as there is no difference in the kernel versions and I needed the graphical DE anyway.

The installation process is really easy and straight-forward. I chose to use the whole mSATA SSD under the OS with default [LVM](https://wiki.ubuntu.com/Lvm) configuration. I did not choose full disk encryption this time because there are problems with remote reboots (you have to enter the encryption key at startup) but there are [workarounds](https://benediktkr.github.io/ops/2015/05/01/remote-fde.html) that I might look into later.

### Configuring the HDD

The 2TB HDD was formatted with ext4 from previous installation (when I used the NUC as a desktop PC) and it is packed with various data such as media and backups. I really doubt that ext4 is the best filesystem for this kind of media as I have considerable less space available than on my identical 2TB external hard drive that is formatted with NTFS.

I mount the HDD under ``/hdd`` and configure it to spin down after 5 minutes of inactivity to save power and reduce background noise. I really don't care about the extra 2-3 seconds of spin-up time for the rare times when I access data on the disk. By running ``sudo blkid`` I found out that the UUID of my partition on the HDD is ``83652517-02c7-438d-9fad-35469c3a17b8`` (it's [more reliable to use UUIDs](https://help.ubuntu.com/community/UsingUUID) in Linux then ``/dev/sdXY`` addresses as they may change). 

To achieve all this I ran

    :::bash
    ## Find your UUID by running sudo blkid
    HDD_UUID="83652517-02c7-438d-9fad-35469c3a17b8"

    ## Mounting the HDD under /hdd and making it permanent
    sudo mkdir /hdd
    sudo chown bjarni:bjarni /hdd
    echo "UUID=${HDD_UUID} /hdd ext4 defaults 0 2" | sudo tee -a /etc/fstab
    sudo mount -a

    ## Setting spindown time to 60*5 seconds = 5 minutes
    sudo hdparm -S 60 /dev/disk/by-uuid/${HDD_UUID}
    echo "/dev/disk/by-uuid/${HDD_UUID} {
        spindown_time = 60
    }" | sudo tee -a /etc/hdparm.conf

**Edit 2016-07-04:** If the HDD doesn't go to sleep as expected you may have to disable SMART monitoring tools with ``sudo smartctl --offlineauto=off /dev/sdX`` where X is the drive letter. This is a persistent change which survives reboots and (I think) drive formats. Thanks goes to [Stack Exchange](http://unix.stackexchange.com/a/58645/118840) as usual.

### Monitoring solution

I've been looking into a vast amount of tools to help me monitor and visualize the metrics I mentioned in my [last post]({filename}/2016-05-22-What-Im-aiming-for.md). The list includes time series logging and graphing tools such as [RRDtool](https://oss.oetiker.ch/rrdtool/) with [collectd](https://collectd.org/) and [sensord](http://manpages.ubuntu.com/manpages/xenial/en/man8/sensord.8.html) or [Grafana](http://grafana.org/) with [InfluxDB](https://influxdata.com/).

However, I decided do make some compromises and accept that the server wouldn't be perfect in this first setup so I chose the easy-to-install, configure-free-out-of-the-box-experience [netdata](https://my-netdata.io/). There is actually a lot of configable options (the configuration file on my computer is 6656 lines!), but the idea with netdata is that it simply works out-of-the-box. I didn't change a thing and my dashboard looks like this:

![My configure-free netdata dashboard]({filename}/static/netdata_screenshot.png)

Netdata runs in the background and monitors various metrics. Netdata is about *"real-time performance monitoring"* and doesn't write anyting to the disk. The default configuration is to keep metrics data for the last hour in memory and discard anything older than that. 

On my NUC netdata uses around 30MiB of RAM and causes ~2% CPU load. Netdata serves its own web server on port 19999 that I open on my laptop on ``http://localhost:19999`` through an SSH tunnel brought up with ``ssh -L 19999:127.0.0.1:19999 bjk.is`` (bjk.is is an entry in my ``~/.ssh/config`` file).

There is much more data on the dashboard than I usually look at and sometimes I have to scroll very far down to see the numbers that I'm interested in. Even so, there are a few metrics I'd like to have and theoretically I could write add-ons to gather them (which I'll maybe do one day). At least I should edit the configuration file and cut off some metrics to clean up the clutter and lower the load.

I installed netdata by following the [official instructions](https://github.com/firehol/netdata/wiki/Installation). In a nutshell, it goes like this:

    :::bash
    sudo apt install zlib1g-dev uuid-dev libmnl-dev gcc make git autoconf autogen automake pkg-config
    sudo git clone https://github.com/firehol/netdata.git --depth=1 /usr/src/netdata
    echo "alias update-netdata='pushd /usr/src/netdata && sudo git pull && sudo ./netdata-installer.sh && popd'" >> ~/.bash_aliases
    source ~/.bash_aliases
    update-netdata

and then I can use the alias ``update-netdata`` when new versions emerge.