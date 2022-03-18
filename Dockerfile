FROM python:3.7-slim
WORKDIR /
COPY /singleCalculator/singleVersion.py /multipleCalculator/addition.py /multipleCalculator/division.py /multipleCalculator/multiplication.py /multipleCalculator/subtraction.py
ENTRYPOINT ["python"]
CMD ["/singleCalculator/singleVersion.py"]
