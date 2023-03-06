Issue Summary:
Duration: 6 hours, from 8:00 AM to 2:00 PM PST Impact: User authentication service was down, preventing users from accessing their accounts. 30% of users were affected.
Root Cause: A recent code deployment introduced a bug that caused the user authentication service to crash.
Timeline:
8:00 AM: Issue detected through monitoring alerts.
8:05 AM: Engineering team notified and began investigation.
8:20 AM: Initial assumption was that the issue was related to a recent database update.
9:00 AM: Investigation of database update completed, issue was not found.
9:30 AM: Another assumption was that the issue was related to the load balancer, which was causing the service to fail.
10:00 AM: Load balancer investigation completed, issue was not found.
11:00 AM: Debugging revealed that a recent code deployment introduced a bug in the user authentication service.
12:00 PM: The incident was escalated to senior engineering management.
1:00 PM: The issue was resolved by rolling back the code deployment.
2:00 PM: Service was fully restored and incident was declared resolved.
Root Cause and Resolution:
The root cause of the issue was a bug introduced during a recent code deployment. The bug caused the user authentication service to crash, preventing users from accessing their accounts. The issue was resolved by rolling back the code deployment to the previous stable version of the service.
Corrective and Preventative Measures:
To prevent similar incidents from occurring in the future, the following measures will be taken:
Implement more thorough testing procedures prior to code deployment to catch potential bugs.
Implement a canary deployment strategy to gradually deploy new code changes to ensure stability.
Increase monitoring and alerting for critical services to quickly detect and respond to issues.
Schedule regular code reviews to catch potential issues and improve overall code quality.
Tasks:
Review and improve testing procedures for code deployments.
Implement canary deployment strategy for new code changes.
Increase monitoring and alerting for critical services.
Schedule regular code reviews with engineering team.


