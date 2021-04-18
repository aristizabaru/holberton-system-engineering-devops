# 0x09. Web infrastructure design

## About

This is an educational project to explore concepts about system design and web stack

### Background context

[![Web infrastructure](http://img.youtube.com/vi/lQNEW76KdYg/0.jpg)](http://www.youtube.com/watch?v=lQNEW76KdYg)

## Topics

-  You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
-  You must be able to explain what each component is doing
-  You must be able to explain system redundancy
-  Know all the mentioned acronyms: LAMP, SPOF, QPS

## Requirements

-  Ubuntu 16.04 LTS
-  Shellcheck 0.3.3

## Resourses

### Read or watch

-  [What is a database](https://searchsqlserver.techtarget.com/definition/database)
-  [What’s the difference between a web server and an app server?](https://www.youtube.com/watch?v=S97eKyv2b9M)
-  [DNS record types](https://pressable.com/2019/10/11/what-are-dns-records-types-explained-2/)
-  [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
-  [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
-  [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
-  [What is HTTPS](https://www.instantssl.com/http-vs-https)
-  [What is a firewall](https://www.webopedia.com/definitions/firewall/)

### Concept page

-  [DNS](https://intranet.hbtn.io/concepts/12)
-  [Monitoring](https://intranet.hbtn.io/concepts/13)
-  [Web Server](https://intranet.hbtn.io/concepts/17)
-  [Network basics](https://intranet.hbtn.io/concepts/33)
-  [Load balancer](https://intranet.hbtn.io/concepts/46)
-  [Server](https://intranet.hbtn.io/concepts/67)

## File Descriptions

This project is conceived to be carried out step by step, that is why the description of the files is presented as a statement.

### 0. Simple web stack

**[0-simple_web_stack](0-simple_web_stack)**

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a [LAMP stack](https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29).

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:

-  You must use:
   -  1 server
   -  1 web server (Nginx)
   -  1 application server
   -  1 application files (your code base)
   -  1 database (MySQL)
   -  1 domain name `foobar.com` configured with a `www` record that points to your server IP `8.8.8.8`
-  You must be able to explain some specifics about this infrastructure:
   -  What is a server
   -  What is the role of the domain name
   -  What type of DNS record www is in www.foobar.com
   -  What is the role of the web server
   -  What is the role of the application server
   -  What is the role of the database
   -  What is the server using to communicate with the computer of the user requesting the website
-  You must be able to explain what the issues are with this infrastructure:
   -  SPOF
   -  Downtime when maintenance needed (like deploying new code web server needs to be restarted)
   -  Cannot scale if too much incoming traffic

Please, remember that everything must be written in English to further your technical ability in a variety of settings.

### 1. Distributed web infrastructure

**[1-distributed_web_infrastructure](1-distributed_web_infrastructure)**

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.

Requirements:

-  You must add:
   -  2 servers
   -  1 web server (Nginx)
   -  1 application server
   -  1 load-balancer (HAproxy)
   -  1 set of application files (your code base)
   -  1 database (MySQL)
-  You must be able to explain some specifics about this infrastructure:
   -  For every additional element, why you are adding it
   -  What distribution algorithm your load balancer is configured with and how it works
   -  Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
   -  How a database Primary-Replica (Master-Slave) cluster works
   -  What is the difference between the Primary node and the Replica node in regard to the application
      You must be able to explain what the issues are with this infrastructure:
   -  Where are SPOF
   -  Security issues (no firewall, no HTTPS)
   -  No monitoring

Please, remember that everything must be written in English to further your technical ability in a variety of settings.

### 2. Secured and monitored web infrastructure

**[2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)**

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

Requirements:

-  You must add:
   -  3 firewalls
   -  1 SSL certificate to serve www.foobar.com over HTTPS
   -  3 monitoring clients (data collector for Sumologic or other monitoring services)
-  You must be able to explain some specifics about this infrastructure:
   -  For every additional element, why you are adding it
   -  What are firewalls for
   -  Why is the traffic served over HTTPS
   -  What monitoring is used for
   -  How the monitoring tool is collecting data
   -  Explain what to do if you want to monitor your web server QPS
-  You must be able to explain what the issues are with this infrastructure:
   -  Why terminating SSL at the load balancer level is an issue
   -  Why having only one MySQL server capable of accepting writes is an issue
   -  Why having servers with all the same components (database, web server and application server) might be a problem

Please, remember that everything must be written in English to further your technical ability in a variety of settings.

### 3. Scale up

**[3-scale_up](3-scale_up)**

Readme

-  [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)

Requirements:

-  You must add:
   -  1 server
   -  1 load-balancer (HAproxy) configured as cluster with the other one
   -  Split components (web server, application server, database) with their own server
-  You must be able to explain some specifics about this infrastructure:
   -  For every additional element, why you are adding it

Please, remember that everything must be written in English to further your technical ability in a variety of settings.
