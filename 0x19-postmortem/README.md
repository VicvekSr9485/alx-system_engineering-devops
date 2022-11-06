Postmortem Report

The following is the incident report for the sudo-dev web services outage that occurred on October 19, 2022. We understand this service issue has impacted our valued users, and we apologize to the affected persons during this period.

Issue Summary

From 7:43 PM to 10:16 PM UTC, attempts to access sudo-dev web services resulted in a failure and about 320 errors were recorded within this time frame. At its peak, the issue affected 100% of traffic to this web infrastructure. All resources were unavailable to utilize within this period of time. The root cause of this downtime was some invalid configuration push to the codebase which broke the whole system down. 

Timeline (All Times Coordinated Universal Time)

7:41 PM: Configuration push begins
7:43 PM: Outage begins
7:43 PM: Pagers alerted teams
7:59 PM: Failed configuration change rollback started
8:07 PM: Configuration change rollback failed
8:09 PM: The issue was escalated to another team
9:45 PM: Senior Engineers aids were sought after
9:58 PM: Bugs identified and fixed
10:01 PM: Server restarts initiated
10:16 PM: 100% of traffic back online

Root Cause

The monitoring system alerted our engineers at 7:43 PM UTC, they swiftly started investigating the issue. After a series of debugging it was eventually discovered that some Invalid syntaxes were included in the change recently pushed to the codebase and this has disruption some other systems as there are gigantic infrastructure involved. Traffic was permanently queued and could not be processed. The servers were unable to handle requests and at 7:43 PM UTC, the service outage began.

Resolution and recovery

At 7:43 PM UTC, the monitoring systems alerted our engineers who investigated and quickly escalated the issue. By 7:53 PM, the incident response team identified that the monitoring system was exacerbating the problem caused by this bug.

At 7:59 PM, we attempted to rollback the problematic configuration change. This rollback failed due to complexity in the configuration system which caused our security checks to reject the rollback. These problems were addressed and we successfully rolled back at 9:58 PM.

Corrective and Preventative Measures

In the last few days, internal reviews and analysis of the outage have been conducted. The following are actions we are taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:
Disable the current configuration release mechanism until safer measures are implemented. (Completed.)
Change rollback process to be quicker and more robust.
Employ more tests and validations before any changes are pushed
Programmatically enforce staged rollouts of all configuration changes.
Improve process for auditing all high-risk configuration options.
Add a faster rollback mechanism and improve the traffic ramp-up process, so any future problems of this type can be corrected quickly.
Develop better mechanism for quickly delivering status notifications during incidents.

We are committed to continually and quickly improving our technology and operational processes to prevent outages and serving your best interests. We appreciate your patience and again apologize for all this might have caused you, your users, and your organization. We thank you for your business and continual support.

Sincerely,
Sudo-dev DevOps Team


Posted by Olamide Oso, Editor
