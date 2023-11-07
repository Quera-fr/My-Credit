FROM continuumio/miniconda3

WORKDIR /home/app

COPY ./requirements.txt .

# RUN pip install annotated-types==0.5.0 anyio==3.7.1 certifi==2023.7.22 charset-normalizer==3.3.0 click==8.1.7 exceptiongroup==1.1.3 fastapi==0.103.2 h11==0.14.0 idna==3.4 joblib==1.3.2 numpy==1.26.0 pandas==2.1.1 pydantic==2.4.2 pydantic_core==2.10.1 python-dateutil==2.8.2 pytz==2023.3.post1 requests==2.31.0 scikit-learn==1.3.1 scipy==1.11.3 six==1.16.0 sniffio==1.3.0 starlette==0.27.0 threadpoolctl==3.2.0 typing_extensions==4.8.0 tzdata==2023.3 urllib3==2.0.6 uvicorn==0.23.2
RUN pip install -r requirements.txt
RUN pip install pytest
RUN pip install httpx
RUN pip install fastapi
COPY . .

#RUN python -m unittest test_api.py
#RUN python -m unittest test_api.py

# Define a custom entry point for running unit tests
#ENTRYPOINT ["pytest"]

CMD uvicorn app:app --host=0.0.0.0 --port=$PORT 