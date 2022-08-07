# Table of contents

## Getting Started

* [Introduction](./getting-started/introduction.md)
* [Core Concepts](./getting-started/core-concepts.md)
* [Installation](./getting-started/installation.md)
* [Quickstart](https://github.com/zenml-io/zenml/tree/main/examples/quickstart)

## Examples & Use-Cases

* [Learn MLOps with ZenML (ZenBytes)](https://github.com/zenml-io/zenbytes)
* [See Full ZenML Examples (ZenFiles)](https://github.com/zenml-io/zenfiles)
* [See Integration Examples](https://github.com/zenml-io/zenml/tree/main/examples)

## Developer Guide

* [Steps & Pipelines](./developer-guide/steps-pipelines/steps-and-pipelines.md)
  * [Configure Pipelines at Runtime](./developer-guide/steps-pipelines/runtime-configuration.md)
  * [Choose Functional vs. Class-Based API](./developer-guide/steps-pipelines/functional-vs-class-based-api.md)
  * [Inspect Pipeline Runs](./developer-guide/steps-pipelines/inspecting-pipeline-runs.md)
  * [Configure Automated Caching](./developer-guide/steps-pipelines/caching.md)
  * [Visualize Data Lineage](./developer-guide/steps-pipelines/pipeline-visualization.md)
* [Stacks, Profiles, Repositories](./developer-guide/stacks-profiles-repositories/stacks-profiles-repositories.md)
  * [Stacks: Configure MLOps Tooling and Infrastructure](./developer-guide/stacks-profiles-repositories/stack.md)
  * [Profiles: Manage Stack Configurations](./developer-guide/stacks-profiles-repositories/profile.md)
  * [Repositories: Link Stacks to Code](./developer-guide/stacks-profiles-repositories/repository.md)
* [Advanced Usage](./developer-guide/advanced-usage/advanced-usage.md)
  * [Write Custom Stack Component Flavors](./developer-guide/advanced-usage/custom-flavors.md)
  * [Manage Stack Component States](./developer-guide/advanced-usage/stack-state-management.md)
  * [Pass Custom Data Types through Steps](./developer-guide/advanced-usage/materializer.md)
  * [Access the Active Stack within Steps](./developer-guide/advanced-usage/step-fixtures.md)
  * [Access Global Info within Steps](./developer-guide/advanced-usage/environment.md)
  * [Specify Step Resources](./developer-guide/advanced-usage/specify-step-resources.md)
  * [Manage External Services](./developer-guide/advanced-usage/manage-external-services.md)
  * [Manage Docker Images](./developer-guide/advanced-usage/docker.md)
  * [Set Stacks and Profiles with Environment Variables](./developer-guide/advanced-usage/stack-profile-environment-variables.md)

## MLOps Stacks

* [Categories of MLOps Tools](./mlops-stacks/categories.md)
* [Integration Overview](./mlops-stacks/integrations.md)
* [Orchestrators](./mlops-stacks/orchestrators/orchestrators.md)
  * [Local Orchestrator](./mlops-stacks/orchestrators/local.md)
  * [Kubeflow Orchestrator](./mlops-stacks/orchestrators/kubeflow.md)
  * [Kubernetes Orchestrator](./mlops-stacks/orchestrators/kubernetes.md)
  * [Google Cloud VertexAI Orchestrator](./mlops-stacks/orchestrators/gcloud-vertexai.md)
  * [Github Actions Orchestrator](./mlops-stacks/orchestrators/github-actions.md)
  * [Airflow Orchestrator](./mlops-stacks/orchestrators/airflow.md)
  * [Develop a Custom Orchestrator](./mlops-stacks/orchestrators/custom.md)
* [Artifact Stores](./mlops-stacks/artifact-stores/artifact-stores.md)
  * [Local Artifact Store](./mlops-stacks/artifact-stores/local.md)
  * [Amazon Simple Cloud Storage (S3)](./mlops-stacks/artifact-stores/amazon-s3.md)
  * [Google Cloud Storage (GCS)](./mlops-stacks/artifact-stores/gcloud-gcs.md)
  * [Azure Blob Storage](./mlops-stacks/artifact-stores/azure-blob-storage.md)
  * [Develop a Custom Artifact Store](./mlops-stacks/artifact-stores/custom.md)
* [Metadata Stores](./mlops-stacks/metadata-stores/metadata-stores.md)
  * [SQLite Metadata Store](./mlops-stacks/metadata-stores/sqlite.md)
  * [MySQL Metadata Store](./mlops-stacks/metadata-stores/mysql.md)
  * [Kubeflow Metadata Store](./mlops-stacks/metadata-stores/kubeflow.md)
  * [Kubernetes Metadata Store](./mlops-stacks/metadata-stores/kubernetes.md)
  * [Develop a Custom Metadata Store](./mlops-stacks/metadata-stores/custom.md)
* [Container Registries](./mlops-stacks/container-registries/container-registries.md)
  * [Default Container Registry](./mlops-stacks/container-registries/default.md)
  * [DockerHub](./mlops-stacks/container-registries/dockerhub.md)
  * [Amazon Elastic Container Registry (ECR)](./mlops-stacks/container-registries/amazon-ecr.md)
  * [Google Cloud Container Registry](./mlops-stacks/container-registries/gcloud.md)
  * [Azure Container Registry](./mlops-stacks/container-registries/azure.md)
  * [GitHub Container Registry](./mlops-stacks/container-registries/github.md)
  * [Develop a Custom Container Registry](./mlops-stacks/container-registries/custom.md)
* [Secrets Managers](./mlops-stacks/secrets-managers/secrets-managers.md)
  * [Local Secrets Manager](./mlops-stacks/secrets-managers/local.md)
  * [AWS Secrets Manager](./mlops-stacks/secrets-managers/aws.md)
  * [Google Cloud Secrets Manager](./mlops-stacks/secrets-managers/gcp.md)
  * [Azure Secrets Manager](./mlops-stacks/secrets-managers/azure.md)
  * [Github Secrets Manager](./mlops-stacks/secrets-managers/github.md)
  * [HashiCorp Vault Secrets Manager](./mlops-stacks/secrets-managers/hashicorp-vault.md)
  * [Develop a Custom Secrets Manager](./mlops-stacks/secrets-managers/custom.md)
* [Data Validators](mlops-stacks/data-validators/data-validators.md)
  * [Great Expectations](mlops-stacks/data-validators/great-expectations.md)
  * [Deepchecks](mlops-stacks/data-validators/deepchecks.md)
  * [Evidently](mlops-stacks/data-validators/evidently.md)
  * [Whylogs](mlops-stacks/data-validators/whylogs.md)
  * [Develop a Custom Data Validator](mlops-stacks/data-validators/custom.md)
* [Experiment Trackers](./mlops-stacks/experiment-trackers/experiment-trackers.md)
  * [MLflow](./mlops-stacks/experiment-trackers/mlflow.md)
  * [Weights & Biases](./mlops-stacks/experiment-trackers/wandb.md)
  * [Develop a Custom Experiment Tracker](./mlops-stacks/experiment-trackers/custom.md)
* [Model Deployers](./mlops-stacks/model-deployers/model-deployers.md)
  * [MLflow](./mlops-stacks/model-deployers/mlflow.md)
  * [Seldon](./mlops-stacks/model-deployers/seldon.md)
  * [KServe](./mlops-stacks/model-deployers/kserve.md)
  * [Develop a Custom Model Deployer](./mlops-stacks/model-deployers/custom.md)
* [Step Operators](./mlops-stacks/step-operators/step-operators.md)
  * [Amazon SageMaker](./mlops-stacks/step-operators/amazon-sagemaker.md)
  * [Google Cloud VertexAI](./mlops-stacks/step-operators/gcloud-vertexai.md)
  * [AzureML](./mlops-stacks/step-operators/azureml.md)
  * [Develop a Custom Step Operator](./mlops-stacks/step-operators/custom.md)
* [Alerters](./mlops-stacks/alerters/alerters.md)
  * [Slack Alerter](./mlops-stacks/alerters/slack.md)
  * [Develop a Custom Alerter](./mlops-stacks/alerters/custom.md)
* [Feature Stores](./mlops-stacks/feature-stores/feature-stores.md)
  * [Feast](./mlops-stacks/feature-stores/feast.md)
  * [Develop a Custom Feature Store](./mlops-stacks/feature-stores/custom.md)
* [Annotators](./mlops-stacks/annotators/annotators.md)
  * [Label Studio](./mlops-stacks/annotators/label-studio.md)
  * [Develop a Custom Annotator](./mlops-stacks/annotators/custom.md)

## Cloud Guide

* [Overview: Options for Deploying Infrastructure](./cloud-guide/overview.md)
* [AWS](./cloud-guide/aws/aws.md)
  * [Set Up a Minimal MLOps Stack on AWS](./cloud-guide/aws/aws-guide.md)
* [GCP](./cloud-guide/gcp/gcp.md)
  * [Set Up a Minimal MLOps Stack on GCP](./cloud-guide/gcp/gcp-guide.md)
* [Azure](./cloud-guide/azure/azure.md)
  * [Set Up a Minimal MLOps Stack on Azure](./cloud-guide/azure/azure-guide.md)

## Collaborate

* [Collaborate with ZenML](./collaborate/collaborate-with-zenml.md)
* [Export/Import Stacks](./collaborate/stack-export-import.md)
* [Share Stacks and Profiles via ZenStores](./collaborate/zenml-store.md)
* [Organization-Wide Collaboration with ZenServer](./collaborate/zenml-server.md)

## Resources

* [Join the Slack Community](https://zenml.io/slack-invite/)
* [Community Events](https://www.eventbrite.de/o/zenml-44751230043)
* [Blog](https://blog.zenml.io/)
* [Podcast](https://podcast.zenml.io/)
* [YouTube](https://www.youtube.com/channel/UCi79n61eV2sVyYxJOqk\_bMw)
* [Newsletter](https://zenml.substack.com/)
* [Roadmap](https://zenml.io/roadmap)
* [Contribution Guide](resources/contributing.md)
* [External Integration Guide](resources/integrating.md)
* [Best Practices](resources/best-practices.md)
* [Global Configuration](resources/global-config.md)
* [System Environmental Variables](resources/system-environmental-variables.md)
* [Usage Analytics](resources/usage-analytics.md)
* [FAQ](resources/faq.md)

## Reference

* [Glossary](reference/glossary.md)
* [CLI Cheat Sheet](reference/cheat-sheet.md)
* [CLI Reference](https://apidocs.zenml.io/latest/cli/)
* [API Reference](https://apidocs.zenml.io/latest/)