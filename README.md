# Local development

```sh
docker-compose build && docker-compose up
```
[Docker & Django](https://docs.docker.com/compose/django/)

```sh
# Install django locally for init of start project
# may be removed afterwards
conda create -n django python=3.6
source activate django
conda install django
django-admin startproject app
```

## Settings

- adjust django settings.py: SECRET_KEY, DATABASE, etc.

# Google Cloud

# Quickstart
https://cloud.google.com/run/docs/quickstarts/build-and-deploy

## 1. Installation
- Login with Google credentials
- New project in Google Cloud Console e.g. "krisenheldinnen"
- APIs: Add Google Cloud Run, Cloud SQL
- local installation of Google Cloud Tools 

```sh
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-sdk -y
sudo apt-get google-cloud-sdk-app-engine-python -y
gcloud init
# Update components
gcloud components update
```

- Check container runtime contract

https://cloud.google.com/run/docs/reference/container-contract

>The container must listen for requests on 0.0.0.0 on the port defined by the PORT environment variable. In Cloud Run container instances, the PORT environment variable is always set to 8080, but for portability reasons, your code should not hardcode this value.


## 2. Build and deploy docker image
- Set Project ID

```sh
#gcloud config set project VALUE
gcloud config set project krisenheldinnen
```

- Go to project folder and execute build command

```sh
# for the first time:
gcloud auth login
# --substitutions $PORT=8080?
#gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld
gcloud builds submit --tag eu.gcr.io/krisenheldinnen/api 
```

- Deploy image
  
```sh
#gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
gcloud run deploy --image eu.gcr.io/krisenheldinnen/api --platform managed

Please specify a region:
 [1] asia-northeast1
 [2] europe-west1
 [3] us-central1
 [4] us-east1
 [5] cancel
Please enter your numeric choice:  2

To make this the default region, run `gcloud config set run/region europe-west1`.

Service name (app):  krisenheldinnen

Allow unauthenticated invocations to [krisenheldinnen] (y/N)?  y

```

- Configure gcloud for docker

```sh
gcloud auth configure-docker
The following settings will be added to your Docker config file 
located at [/home/jsommer/.docker/config.json]:
 {
  "credHelpers": {
    "gcr.io": "gcloud", 
    "us.gcr.io": "gcloud", 
    "eu.gcr.io": "gcloud", 
    "asia.gcr.io": "gcloud", 
    "staging-k8s.gcr.io": "gcloud", 
    "marketplace.gcr.io": "gcloud"
  }
}

Do you want to continue (Y/n)?  y
```

- Check image locally

```sh
#PORT=8080 && docker run -p 8080:${PORT} -e PORT=${PORT} gcr.io/[PROJECT_ID]/[IMAGE]
PORT=8080 && docker run -p 8080:${PORT} -e PORT=${PORT} eu.gcr.io/krisenheldinnen/api
```

- build with google cloud
  - create cloudbuild.yaml

```yaml
steps:   
    # build the app image
    - name: 'eu.gcr.io/cloud-builders/docker'
      args: ['build', '-t', 'eu.gcr.io/krisenheldinnen', '.']

# image is pushed to Container Registry
images:
- 'eu.gcr.io/krisenheldinnen'
```

invoke build now with

```sh
gcloud builds submit --config cloudbuild.yaml
```

- Warm up of cloud service (first few requests return HTTP 502)

```sh
# Apache Benchmark 'ab'
ab -c 100 -n 500 https://krisenheldinnen-vqwbton3pq-ew.a.run.app/
```