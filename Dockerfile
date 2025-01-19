FROM python:3.10.16-alpine3.21


WORKDIR /usr/src/nexhome

ENV DONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies using apk for Alpine
RUN apk update && apk add --no-cache netcat-openbsd
RUN pip install --upgrade pip

# Copy and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy entrypoint script and make it executable
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/nexhome/entrypoint.sh && \
    chmod +x /usr/src/nexhome/entrypoint.sh

# Copy the rest of the application
COPY . .

# Define the entrypoint for the container
ENTRYPOINT ["/usr/src/nexhome/entrypoint.sh"]