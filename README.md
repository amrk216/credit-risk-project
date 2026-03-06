# credit_risk

The basic idea of ​​the model is to predict whether a person will default on a loan based on their financial and personal data.

## Requirements

- Python 3.10

#### Install Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n credit-risk python=3.10
```
3) Activate the environment:
```bash
$ conda activate credit-risk
```


## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

## Run the FastAPI server (Development Mode)

```bash
$ uvicorn main:app --reload --port 5000
```