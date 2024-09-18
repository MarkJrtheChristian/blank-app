# Build and deploy

Command to build the application. PLease remeber to change the project name and application name
```
gcloud builds submit --tag gcr.io/testa-53w5j7/CommsCreatorTest  --project=testa-53w5j7
```

Command to deploy the application
```
gcloud run deploy --image gcr.io/testa-53w5j7/CommsCreatorTest --platform managed  --project=testa-53w5j7 --allow-unauthenticated