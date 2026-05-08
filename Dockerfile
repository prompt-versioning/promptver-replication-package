FROM python:3.11-slim
WORKDIR /artifact
COPY . /artifact
RUN pip install --no-cache-dir -r requirements.txt
CMD ["bash", "scripts/run_all_analysis.sh"]
