![Overview](/images/final.jpg)


## Assign a public static IP
Elastic IPs provide a public endpoint whose IP doesn't change on reboot
Helps with failover, just point the domain to a new IP
## Use a DNS
Add a DNS such as Route 53 to map the domain to the instance's public IP

## Secure the web server
Open up only necessary ports
Allow the web server to respond to incoming requests from:
    
    80 for HTTP
    443 for HTTPS
    22 for SSH to only whitelisted IPs
    
Prevent the web server from initiating outbound connections

## Store static content separately
   Consider using a managed Object Store like S3 to store static content.It is Highly scalable and reliable.
   Move static content to S3
   
        User files
        JS
        CSS
        Images
        Videos
        
        
## Secure the system

   1) Encrypt data in transit and at rest
   2) Use a Virtual Private Cloud
   3) Create a public subnet for the single Web Server so it can send and receive traffic from the internet
   4) Create a private subnet for everything else, preventing outside access
   5) Only open ports from whitelisted IPs for each component

## Scaling

1) Use Horizontal Scaling to handle increasing loads and to address single points of failure
2) Add a Load Balancer such as Amazon's ELB or HAProxy.
3) Use multiple Web Servers spread out over multiple availability zones
4) Use multiple MySQL instances in Master-Slave Failover mode across multiple availability zones to improve redundancy
5) Web Servers can run as a Reverse Proxy
6) Move static (and some dynamic) content to a Content Delivery Network (CDN) to reduce load and latency

## Mysql Read And Write Replicas:

Depends on read and write ratio

1) Add MySQL read replicas
2) In addition to adding and scaling a Memory Cache, MySQL Read Replicas can also help relieve load on the MySQL Write Master
3) Add logic to Web Server to separate out writes and reads


## Client caching

Caches can be located on the client side (OS or browser), server side, or in a distinct cache layer.

1) Web server caching:

    Reverse proxies and caches such as Varnish can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.

2) Database caching:
    Your database usually includes some level of caching in a default configuration, optimized for a generic use case. Tweaking these settings for specific usage patterns can further boost performance.



## AutoScaling:

Consider a managed service such as AWS Autoscaling
    1) Create one group for each Web Server and one for each Application Server type, place each group in multiple availability zones
    2) Set a min and max number of instances
  
Metrics over a time period:

        CPU load
        Latency
        Network traffic
        Custom metric


