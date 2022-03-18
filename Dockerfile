FROM python:3.7-slim

WORKDIR /singleCalculator
COPY singleVersion.py /singleCalculator/singleVersion.py
ENTRYPOINT ["python"]
CMD ["/singleCalculator/singleVersion.py"]
