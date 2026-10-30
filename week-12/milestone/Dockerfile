# Write the Dockerfile for the service. It is built from the REPOSITORY ROOT:
#   docker build -f week-12/milestone/Dockerfile -t shop-ai .
#
# In this order:
#   1. Start from python:3.12-slim.
#   2. Work in /app.
#   3. Copy week-12/milestone/requirements-serve.txt and pip install it (--no-cache-dir)
#      BEFORE copying any code, so code changes do not reinstall torch.
#   4. Copy shoplab/, the milestone's .py files, and week-12/milestone/bundle/ to ./bundle/.
#   5. Create a user called shop and switch to it: never run a service as root.
#   6. EXPOSE 8000, a HEALTHCHECK that requests /health, and
#      CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]
