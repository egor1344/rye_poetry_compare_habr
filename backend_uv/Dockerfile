FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:0.6.5 /uv /uvx /bin/

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONWARNINGS ignore
ENV CURL_CA_BUNDLE ""
ENV POETRY_VIRTUALENVS_CREATE true
ENV PATH "${PATH}:/root/.local/bin"

# Expose port 8000
EXPOSE 8000/tcp

# Set the working directory for the application
WORKDIR /app

# Copy just the dependencies installation from the current directory to the Docker image
COPY . /app/

RUN time -v uv lock
RUN time -v uv sync

# Copy wait-for script and give it necessary permissions
COPY wait-for /usr/bin/
RUN chmod +x /usr/bin/wait-for

# Give necessary permissions to entrypoint
RUN chmod +x entrypoint.*
