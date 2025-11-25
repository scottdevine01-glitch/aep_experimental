# AEP Containerized Environments

This directory contains containerized environments for reproducible execution of AEP analyses across different domains.

## Available Containers

### Basic Python Environment
```bash
docker build -t aep-validation .
docker run -it aep-validation
