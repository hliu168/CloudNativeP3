from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash

from jaeger_client import Config
from jaeger_client.metrics.prometheus import PrometheusMetricsFactory
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchExportSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleExportSpanProcessor,
)
from prometheus_flask_exporter import PrometheusMetrics
import logging

trace.set_tracer_provider(TracerProvider())
trace.get_tracer_provider().add_span_processor(
    SimpleExportSpanProcessor(ConsoleSpanExporter())
)

logging.basicConfig(level=logging.INFO)
logging.info("Setting LOGLEVEL to INFO")
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

metrics = PrometheusMetrics(app)
metrics.info("app_info", "App Info, this can be anything you want", version="1.0.0")


#config = Config(
#        config={},
#        service_name='your-app-name',
#        validate=True,
#        metrics_factory=PrometheusMetricsFactory(service_name_label='your-app-name')
#)
#tracer = config.initialize_tracer()

def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('first-service')

@app.route('/')
def homepage():
    return render_template("main.html")
    with tracer.start_span('get-python-jobs') as span:
        homepages = []
        res = requests.get('https://jobs.github.com/positions.json?description=python')
        span.set_tag('first-tag', len(res.json()))
        for result in res.json():
            try:
                homepages.append(requests.get(result['company_url']))
            except:
                return "Unable to get site for %s" % result['company']
        


    return jsonify(homepages)

@app.route('/healthz')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
        )
    return response


if __name__ == "__main__":
    app.run(debug=True,)
