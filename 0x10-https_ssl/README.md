# 0x03. AirBnB clone - Deploy static

## About

This is an educational project to explore several concepts about https protocol and TLS termination

### Background context

This project will guide you through the concepts and implementation of https protocol for the follow architecture

![AirBnb architecture](images/airbnb_architecture.png)

## Topics

-  What is HTTPS SSL 2 main roles
-  What is the purpose encrypting traffic
-  What SSL termination means

## Requirements

-  Ubuntu 16.04 LTS
-  Shellcheck 0.3.3

## Resourses

### Read or watch

-  [What is HTTPS?](https://www.instantssl.com/http-vs-https)
-  [What are the 2 main elements that SSL is providing](https://www.sslshopper.com/why-ssl-the-purpose-of-using-ssl-certificates.html)
-  [HAProxy SSL termination on Ubuntu16.04](https://devops.ionos.com/tutorials/install-and-configure-haproxy-load-balancer-on-ubuntu-1604/)
-  [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy)
-  [Bash function](https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php)
-  [Dig command](https://linuxize.com/post/how-to-use-dig-command-to-query-dns-in-linux/)
-  [Configure SSL in a HAProxy Load Balancer](https://medium.com/swlh/tutorial-to-configure-ssl-in-a-haproxy-load-balancer-b452d1be100f)
-  [The Four Essential Sections of an HAProxy Configuration](https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/)
-  [HAProxy redirecting http to https - stackoverflow](https://stackoverflow.com/questions/13227544/haproxy-redirecting-http-to-https-ssl)
-  [Redirecting HTTP Requests](https://www.haproxy.com/documentation/aloha/12-5/traffic-management/lb-layer7/http-redirection/)
-  [Redirect HTTP to HTTPS with HAProxy](https://www.haproxy.com/blog/redirect-http-to-https-with-haproxy/)
-  [HAProxy and HTTP Strict Transport Security (HSTS)](https://www.haproxy.com/blog/haproxy-and-http-strict-transport-security-hsts-header-in-http-redirects/)
-  [https://www.haproxy.com/blog/haproxy-ssl-termination/](https://www.haproxy.com/blog/haproxy-ssl-termination/)
-  [HAProxy Crash Course (TLS 1.3, HTTPS, HTTP/2 and more)](https://www.youtube.com/watch?v=qYnA2DFEELw)

### Concept page

-  [DNS](https://intranet.hbtn.io/concepts/12)
-  [Web stack debugging](https://intranet.hbtn.io/concepts/68)

## File Descriptions

This project is conceived to be carried out step by step, that is why the description of the files is presented as a statement.

### 0. World wide web

**[0-world_wide_web](0-world_wide_web)**

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

-  Add the subdomain www to your domain, point it to your `lb-01` IP (your domain name might be configured with default subdomains, feel free to remove them)
-  Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
-  Add the subdomain `web-01` to your domain, point it to your `web-01` IP
-  Add the subdomain `web-02` to your domain, point it to your `web-02` IP
-  Your Bash script must accept 2 arguments:
   -  domain:
      -  type: string
      -  what: domain name to audit
      -  mandatory: yes
   -  subdomain:
      -  type: string
      -  what: specific subdomain to audit
      -  mandatory: no
-  Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
-  When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
-  When passing `domain` and `subdomain` parameters, display information for the specified subdomain
-  Ignore `shellcheck` case `SC2086`
-  Must use:
   -  `awk`
   -  at least one Bash function
-  You do not need to handle edge cases such as:
   -  Empty parameters
   -  Nonexistent domain names
   -  Nonexistent subdomains

Example:

```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```

### 1. HAproxy SSL termination

**[1-haproxy_ssl_termination](1-haproxy_ssl_termination)**

“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`.

Requirements:

-  HAproxy must be listening on port TCP 443
-  HAproxy must be accepting SSL traffic
-  HAproxy must serve encrypted traffic that will return the / of your web server
-  When querying the root of your domain name, the page returned must contain `Holberton School`
-  Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `1-haproxy_ssl_termination` must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, [SSL termination](https://en.wikipedia.org/wiki/TLS_termination_proxy) is not available before v1.5.

Example:

```
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```

### 2. No loophole in your website traffic

**[100-redirect_http_to_https](100-redirect_http_to_https)**

A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

Requirements:

-  This should be transparent to the user
-  HAproxy should return a [301](https://en.wikipedia.org/wiki/HTTP_301)
-  HAproxy should redirect HTTP traffic to HTTPS
-  Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `100-redirect_http_to_https` must be your HAproxy configuration file

Example:

```
sylvain@ubuntu$ curl -sIL http://www.holberton.online
HTTP/1.1 301 Moved Permanently
Content-length: 0
Location: https://www.holberton.online/
Connection: close

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 02:19:18 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$
```
