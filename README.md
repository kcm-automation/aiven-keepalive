# Aiven Keepalive

Aiven is a cloud data platform that provides databases, data infrastructure, and application services.

They have a free tier with a hobby PostgreSQL instance (1 CPU, 1 GB RAM, 1 GB storage), which is perfect for some of the lightweight projects that I am working on.

However, Aiven powers down free-tier databases if you don't log into the _**console**_ within a few days -- not due to database inactivity or lack of direct connections. Which means you need to login _to the console, not the database,_ at least once every 2-3 days to keep your database online.

I'm not really of fan that the inactivity is based on console login, not database activity. 

So I wrote this script, which uses [playwright](https://pypi.org/project/playwright/) to log into the console once a day.

## Required environment variables

```
AIVEN_SERVICES = {
    "services": [
        {
            "service_name": "AAA",
            "email_address": "BBB",
            "password": "CCC"
        }
    ]
}
```

> [!IMPORTANT]  
> Must be a single line json string. Shown as multi-line here for better readability.