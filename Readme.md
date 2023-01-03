# Network Intro

This is a configuration that will spin up a training center for an introduction to networking in CTFs.
The internal network is 172.28.0.0/16, where 172.28.1.0/24 contains the services and 172.28.2.0/24 contains the students.
The gateway is configured as 172.28.0.1.
We use fqdn as a placeholder for the domain name chosen, in our case `netintro.updownup.de`.
It consists of :

| Service Name  | Container Name | Tool      | IP               | DNS                 |
| ------------- | -------------- | --------- | ---------------- | ------------------- |
| Wireguard VPN | wireguard      | wireguard | 172.28.1.1       | -                   |
| VPN config    | vpnconfig      | Nginx     | external (31338) | vpnconfig.fqdn      |
| Slides        | slides         | revealjs  | external (31337) | slides.fqdn         |
| Challenge 0   | chal0          | Nginx     | 172.28.1.2       | chal0.internal.fqdn |

## Service explanations

### Wireguard VPN

The students can connect to the internal network through this.

### VPN Config

Entry point to the network, students should be assigned a number and they can then download their config.

### Slides

Slides for the students to see.
This is external, so these connections don't clutter Wireshark.

### Challenge 0

Webserver, that outputs the flag via HTTP on Port 80.
The flag is in flag.css.
