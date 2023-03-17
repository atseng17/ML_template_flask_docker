FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt
# pre download nltk when building image
RUN python -c "import nltk; nltk.download('omw-1.4'); nltk.download('wordnet')"
# copy every thing in the docker dir
COPY . .

EXPOSE 5000

# if using flask
# CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
# if using gunicorn
CMD ["gunicorn", "--bind=0.0.0.0:5000", "--reload", "--workers=3", "--threads=8", "--timeout=0", "app:app"]