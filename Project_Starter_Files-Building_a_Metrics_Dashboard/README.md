**Note:** For the screenshots, you can store all of your answer images in the `answer-img` directory.

## Verify the monitoring installation

*TODO:* run `kubectl` command to show the running pods and services for the three components. Copy and paste the output or take a screenshot of the output and include it here to verify the installation

![Alt text](./screenshot/Pods.Services.png?raw=true "Optional Title")

## Setup the Jaeger and Prometheus source
*TODO:* Expose Grafana to the internet and then setup Prometheusas a data source. Provide a screenshot of the home page after logging into Grafana.

![Alt text](./screenshot/Grafana.Login.png?raw=true "Optional Title")

## Create a Basic Dashboard
*TODO:* Create a dashboard in Grafana that shows Prometheus as a source. Take a screenshot and include it here.

![Alt text](./screenshot/Prometheus-Dashboard1.png?raw=true "Optional Title")

## Describe SLO/SLI
*TODO:* Describe, in your own words, what the SLIs are, based on an SLO of *monthly uptime* and *request response time*.

- SLI or Service Level Indicators are metrics that indicate whether we achieved our SLOs (Service Level Objectives).
- In terms of monthly uptime, an SLI could be "The website and it services are available and functioning over 99.95% of time in June".
- In terms of request response time, and SLI could be "Average response time of an HTTP request to the website takes less than 100ms to complete".


## Creating SLI metrics.
*TODO:* It is important to know why we want to measure certain metrics for our customer. Describe in detail 5 metrics to measure these SLIs. 

- Latency, or the time taken to serve a request (usually measured in ms).
- Traffic, or the amount of stress on a system from demand (such as the number of HTTP requests/second).
- Errors, or the number of requests that are failing (such as number of HTTP 500 responses).
- Saturation, or the overall capacity of a service (such as the percentage of memory or CPU used).
- Uptime, or the percentage of time the website/webservices are available and functioning.

(Latency, Traffic, Errors, and Saturations are the Four Golden Signals, whose definition were taken from Nanodegree course page).


## Create a Dashboard to measure our SLIs
*TODO:* Create a dashboard to measure the uptime of the frontend and backend services We will also want to measure to measure 40x and 50x errors. Create a dashboard that show these values over a 24 hour period and take a screenshot.
![Alt text](./screenshot/UpTime.Panel.png?raw=true "Optional Title")
![Alt text](./screenshot/Prometheus.Target.png?raw=true "Optional Title")

## Tracing our Flask App
*TODO:*  We will create a Jaeger span to measure the processes on the backend. Once you fill in the span, provide a screenshot of it here.

## Jaeger in Dashboards
*TODO:* Now that the trace is running, let's add the metric to our current Grafana dashboard. Once this is completed, provide a screenshot of it here.

## Report Error
*TODO:* Using the template below, write a trouble ticket for the developers, to explain the errors that you are seeing (400, 500, latency) and to let them know the file that is causing the issue.

TROUBLE TICKET

Name:

Date:

Subject:

Affected Area:

Severity:

Description:


## Creating SLIs and SLOs
*TODO:* We want to create an SLO guaranteeing that our application has a 99.95% uptime per month. Name three SLIs that you would use to measure the success of this SLO.

## Building KPIs for our plan
*TODO*: Now that we have our SLIs and SLOs, create KPIs to accurately measure these metrics. We will make a dashboard for this, but first write them down here.

## Final Dashboard
*TODO*: Create a Dashboard containing graphs that capture all the metrics of your KPIs and adequately representing your SLIs and SLOs. Include a screenshot of the dashboard here, and write a text description of what graphs are represented in the dashboard.  
