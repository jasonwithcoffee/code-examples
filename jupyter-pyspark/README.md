

```
gcloud beta dataproc clusters create my-cluster --enable-component-gateway 
--bucket {your-bucket} --region us-central1 --subnet default --zone us-central1-c --master-machine-type n1-standard-4 --master-boot-disk-size 100 --num-workers 2 --worker-machine-type n1-standard-4 --worker-boot-disk-size 100 --image-version 1.5-debian10 --optional-components ANACONDA,JUPYTER --max-idle 21600s --scopes 'https://www.googleapis.com/auth/cloud-platform' --project {your-project-name}
```
