# Use a minimal Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /workspace

# Install git and system dependencies for building wheels
RUN apt-get update && \
    apt-get install -y git build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app into the container
COPY . .

# Expose the Streamlit default port
EXPOSE 8501

# Default command
CMD ["streamlit", "run", "job_tracker_ui.py", "--server.port=8501", "--server.address=0.0.0.0"]

# Install bash and add color support
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/magicmonty/bash-git-prompt.git /root/.bash-git-prompt --depth=1 && \
    echo "GIT_PROMPT_ONLY_IN_REPO=1" >> /root/.bashrc && \
    echo "source ~/.bash-git-prompt/gitprompt.sh" >> /root/.bashrc
