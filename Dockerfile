FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "twilio", "/bin/bash", "-c"]


# The code to run when container is started:
COPY src/main.py .
COPY src/methods.py .

ENTRYPOINT ["conda", "run", "-n", "twilio", "python", "main.py"]