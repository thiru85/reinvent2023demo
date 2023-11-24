FROM alpine:latest
RUN apk add --update python3 py3-pip libpq-dev python3-dev gcc wget aws-cli curl 
RUN mkdir app
COPY app.py app/
COPY requirements.txt app/
WORKDIR app
RUN pip3 install -r requirements.txt
RUN opentelemetry-bootstrap --action=install
ENV OTEL_PROPAGATORS xray
ENV OTEL_PYTHON_ID_GENERATOR xray
EXPOSE 8080
ENTRYPOINT ["opentelemetry-instrument", "python3", "app.py"]