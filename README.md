# Create the Service Connections
This may need system administrators as some information may need to come from Azure, etc.

1. Open Project Settings
Locate Service connections under Pipelines, Click on **New service connection**

   ![A screenshot of ADO information](media/image1.png)

2. Select Azure Resource Manager

   ![A screenshot of a service connection](media/image2.png)

3. Steps will vary based on whether a Service Connection or Managed
Identity is used.

4. Ensure that the Service Connection is verified / working and Save it.

   ![A green text on a white background](media/image3.png)

Repeat the process for the Production environment.

# Build the pipeline files within the repository

## Collect the pipeline files from the repo.

**Mandatory:**

Copy the entire Dependencies folder into your repository, leaving
Dependencies at the root level. This folder contains the Pipeline files
as well as the pipeline configuration files and the Databricks v.268 CLI
which is needed for Databricks deployments.

**Optional:**

Copy Databricks_bundle to the repository for testing. These files
demonstrate a Databricks bundle which may be deployed.

## Configure the pipeline for your environment
1. Update the Dev.variables.yml file

   Open the Dev.variables.yml file and update the host to point to the host
in the Dev environment.

   Update the subscription to use the name of the service connection for
the Dev environment.

   ![A screenshot of ADO information](media/image4.png)

2. Update the Prod.variables.yml file

   Open the Prod.variables.yml file and update the host to point to the
host in the Prod environment.

   Update the subscription to use the name of the service connection for
the Prod environment.
   ![A screenshot of ADO information](media/image5.png)

# Set up the Environments
## Create the Environments

1. Within Azure Devops, open Pipelines and click on **Environments**.

   ![A screenshot of ADO information](media/image6.png)

2. Click **New environment**.

   ![A screenshot of ADO information](media/image7.png)

3. Enter **Dev** as the Name, click **Create**

   ![A screenshot of ADO information](media/image8.png)

4. Click **New environment**.

5. Enter **Prod** as the Name, click **Create**

## Add Approval Check to Prod

1. Click on the Prod environment

   ![A screenshot of ADO information](media/image9.png)

2. Click on **Approvals and checks** and then click the **+** button

   ![A yellow line on a white background](media/image10.png)

3. Click **Approvals**

4. Add the approvers group OR add a list of approvers users to Approvers

   ![A screenshot of a computer screen](media/image11.png)

5. Click **Create**

# Create the CI/CD Pipeline

1. Click New Pipeline

   ![A screenshot of ADO information](media/image12.png)

2. Click **Azure Repos Git**

   ![A screenshot of ADO information](media/image13.png)

3. Select the Repo

   ![A screenshot of ADO information](media/image14.png)

4. Click **Existing Azure Pipelines YAML file**

   ![A yellow marker on a white background](media/image15.png)

5. Select **/Dependencies/Pipeline/azure-pipeline.yml**

   ![A screenshot of ADO information](media/image16.png)

6. At the next screen, select **Save**

   ![A screenshot of ADO information](media/image17.png)

7. Click the ellipse on the right side and then **Rename/move**

   ![A screenshot of a ADO information](media/image18.png)

8. Change the name to "Databricks CI/CD Pipeline" and click **Save**

# Test the pipeline

   Click into the pipeline and then click Run pipeline

   ![A screenshot of ADO information](media/image19.png)

   Observe the results and ensure that the pipeline completed successfully. There are 3 stages, a package and two deploy steps. The packaging should always succeed. If there are issues in the deployment, review the log and identify why the run failed.