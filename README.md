# Local development

```sh
docker-compose build && docker-compose up
```

## Test Swagger UI
http://localhost:6060/krisenheldin/1.0.0/ui/

## Test per cURL
```
curl -X GET "http://localhost:6060/krisenheldin/1.0.0/employer" -H "accept: */*
```

should return

```json
[
  {
    "city": "Oberhummel",
    "firstName": "Hans",
    "houseNumber": "32a",
    "id": 1,
    "lastName": "Meister",
    "postalCode": "85354",
    "state": "Deutschland",
    "street": "Hinterhof 32"
  }
]
```




## Settings

- adjust SECRET_KEY, DATABASE, etc.

# Google Cloud

# Quickstart
https://cloud.google.com/run/docs/quickstarts/build-and-deploy

## 1. Installation
- Login with Google credentials
- New project in Google Cloud Console e.g. "krisenheldin"
- APIs: Add Google Cloud Run, Cloud SQL
- local installation of Google Cloud Tools 

```sh
export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
sudo apt-get update && sudo apt-get install google-cloud-sdk -y
sudo apt-get google-cloud-sdk-app-engine-python -y
# login with google account
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
gcloud config set project krisenheldin
```

- enable required Google APIs: (Storage, Cloud SQL, Cloud Run, Cloud Build, Container Registry)

```sh
gcloud services enable storage-component.googleapis.com
gcloud services enable sql-component.googleapis.com
gcloud services enable run.googleapis.com   
gcloud services enable cloudbuild.googleapis.com 
gcloud services enable containerregistry.googleapis.com
gcloud services enable compute.googleapis.com
```

- Go to project folder and execute build command

```sh
# for the first time:
gcloud auth login
# --substitutions $PORT=8080?
#gcloud builds submit --tag gcr.io/PROJECT-ID/helloworld
#gcloud builds submit --tag eu.gcr.io/krisenheldin/api 
```

- Deploy image
  
```sh
#gcloud run deploy --image gcr.io/PROJECT-ID/helloworld --platform managed
gcloud run deploy --image eu.gcr.io/krisenheldin/api --platform managed

Please specify a region:
 [1] asia-east1
 [2] asia-northeast1
 [3] europe-north1
 [4] europe-west1
 [5] europe-west4
 [6] us-central1
 [7] us-east1
 [8] us-east4
 [9] us-west1
 [10] cancel
Please enter your numeric choice:  5

To make this the default region, run `gcloud config set run/region europe-west5`.

Service name (app):  krisenheldin

Allow unauthenticated invocations to [krisenheldin] (y/N)?  y

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
PORT=8080 && docker run -p 8080:${PORT} -e PORT=${PORT} eu.gcr.io/krisenheldin/api
```

- build with google cloud
  - create cloudbuild.yml

```yaml
steps:   
    # build the app image
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '-t', 'eu.gcr.io/krisenheldin/api', '.']

# image is pushed to Container Registry
images:
- 'eu.gcr.io/krisenheldin'
```

invoke build now with

```sh
gcloud builds submit --config cloudbuild.yml
```

- first few request may return HTTP 502

- Create PostgreSQL Cloud instance

```sh
# test instance with public IP
gcloud sql instances create XXX --database-version=POSTGRES_11 --tier db-f1-micro --region europe-west4 
```

- Add DB 'XXX'
- Add DB User 'XXX'
- Add password for 'XXX'
- Deploy a new revision 
  - with the following environment variables:
  
  ```
     POSTGRES_DB
     POSTGRES_USER
     POSTGRES_PASSWORD
     CLOUD_SQL_CONNECTION_NAME
  ```

  - Add Cloud SQL connection to previous created DB instance

- Enable PostGIS extension

```sh
gcloud sql connect krisenheldindb1 --user=postgres
CREATE EXTENSION postgis;
```

- Test URL https://krisenheldin-ocdqbzyzwa-ez.a.run.app/krisenheldin/1.0.0/employer
  
 - Trouble shooting: see Logs in Google Cloud Run!
   - Maybe enable the access to the Cloud SQL Admin API?
     https://console.developers.google.com/apis/api/sqladmin.googleapis.com/overview?project=XXXX