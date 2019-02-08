![Overview](/images/overview.jpg)


![Static or Dynamic Request](/images/sord.jpg)

#Why Amazon S3:

##Amazon S3 Standard
S3 Standard offers high durability, availability, and performance object storage for frequently accessed data. Because it delivers low latency and high throughput. It is perfect for a wide variety of use cases including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and Big Data analytics.

For example, 
an application collecting user photo uploads. With unlimited storage, there will never be a disk size issue. S3 can also eliminate unsuccessful uploads, one less thing to worry about cleanup.

##Object Store:

Amazon S3 is a simple key, value store designed to store as many objects as you want

##Static Web Hosting:

Static Web Hosting is one of the most powerful features of the AWS S3. Single Page Applications or Pure JavaScript Applications are in trend nowadays and with AWS S3 we can easily deploy an application and start using immediately without setting up any machine anywhere.

##Backup & Recovery:
AWS S3 provides a simple mechanism to create a backup for data, Cross Region Replication. Cross-region Replication enables automatic and asynchronous copying of objects across buckets in different AWS regions. This is useful in case we want to fast access our data in different regions or create a general backup of the data.

##Security:

Data Access Security:
By default when you create a new bucket, only you have access to Amazon S3 resources they create. You can use access control mechanisms such as bucket policies and Access Control Lists (ACLs) to selectively grant permissions to users and groups of users. Customers may use four mechanisms for controlling access to Amazon S3 resources.

Identity and Access Management (IAM) policies:
IAM policies are applicable to specific principles like User, Group, and Role. The policy is a JSON document, which mentions what the principle can or can not do.


#Why Cloudfront?

1)HTTPS is supported by CloudFront, and you can use Amazon Certificate Manager (ACM) to manage SSL/TLS certificates and deploy to your CloudFront distribution.

2)Access logging can be configured to save logs to an S3 bucket you specify.

3)You can restrict access to your content using GeoRestrictions,Signed URLs and cookies, and AWS WAF, a managed Web Application Firewall service that supports CloudFront. You can create your own rules from scratch, use our AWS WAF Security Automations, and use Managed Rules from third-party vendors from the Marketplace.

#Why Amazon API Gateway?

1)Support for stateful (WebSocket) and stateless (REST) APIs

2)Integration with AWS services such as AWS Lambda, Amazon Kinesis, and Amazon DynamoDB

3)Ability to use IAM roles and policies, AWS Lambda Authorizers or Amazon Cognito user pools to authorize access to your APIs

4)Usage plans and API keys for selling your API as SaaS

5)Canary release deployments for safely rolling out changes

6)CloudTrail logging and monitoring of API usage and API changes

7)CloudWatch access logging and execution logging, including the ability to set alarms

8)Ability to use AWS CloudFormation templates to enable API creation

9)Support for custom domain names

##Throttling:
To prevent your API from being overwhelmed by too many requests, Amazon API Gateway throttles requests to your API using the token bucket algorithm, where a token counts for a request. Specifically, API Gateway sets a limit on a steady-state rate and a burst of request submissions against all APIs in your account. In the token bucket algorithm, the burst is the maximum bucket size.


#Why AWS Lambda?

1) It will grow based on your request. YOu dont have to think about scaling .AWS will do it .
2) Lot of runtime support.
3) A script or program that runs in AWS Lambda. Lambda passes invocation events to your function. The function processes an event and returns a response. (Lambda function) 


#Why AWS lambda?

##High Availability:
For your MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server database (DB) instances, you can use Amazon RDS Multi-AZ deployments. When you provision a Multi-AZ DB instance, Amazon RDS automatically creates a primary DB instance and synchronously replicates the data to a standby instance in a different Availability Zone (AZ). In case of an infrastructure failure, Amazon RDS performs an automatic failover to the standby DB instance.
##disaster recovery: