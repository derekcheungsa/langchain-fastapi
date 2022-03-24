FROM python:3.10.2

WORKDIR /code

# Update pip
RUN pip install --upgrade pip

# Copy resources
COPY . /code

# Install dependencies (prod/dev)
RUN pip install --no-cache-dir --upgrade -r /code/requirements-dev.txt

# Set up app CLI
RUN pip install --no-cache-dir --upgrade --user cli/dist/cli-0.1.0-py3-none-any.whl
ENV PATH="${PATH}:/root/.local/bin"

# Expose port
EXPOSE 80

# Execution command
CMD ["app-cli", "start", "--env", "prod"]
