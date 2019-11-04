FROM python:3

ADD src /src

CMD [ "python", "./src/CalculatorUnitTests.py" ]
#CMD [ "python", "./src/CsvUnitTests.py" ]
#CMD ["python", "-m", "unittest", "discover", "-s","Tests"]