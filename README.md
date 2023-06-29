# DeveleapCI ([DeveleapCD repo](https://github.com/shay79il/DeveleapGitops))

Requirements:

1. CI/CD Pipeline using Jenkins:
   - Set up a Jenkins pipeline that automates the build and deployment process for the chosen application.
   - Ensure the pipeline includes the necessary stages for building the application and publishing the Docker image to a container registry (specifically, Amazon Elastic Container Registry - ECR).
   - The pipeline should be triggered automatically upon changes in the application's source code repository.

2. Dockerfile:
   - Create a Dockerfile for containerizing the application.
   - The Dockerfile should define the necessary steps to build a Docker image that can run the application.

3. GitOps Deployment using Argo CD:
   - Utilize Argo CD to implement the GitOps approach for deploying the application to a Kubernetes cluster.
   - Set up the Argo CD application using the manifests stored in a Git repository.
   - Ensure the application is continuously synchronized and deployed based on changes in the Git repository.

Bonus Tasks:

4. Helm Chart:
   - Enhance your solution by incorporating Helm charts for managing the Kubernetes deployment of the application.
   - Create a Helm chart that encapsulates the necessary Kubernetes manifests and provides a consistent and reproducible way to deploy the application.

5. Infrastructure Provisioning with Terraform:
   - Extend the exercise by automating the provisioning of the Kubernetes cluster using Terraform.
   - Utilize Terraform to define the necessary infrastructure resources (e.g., virtual machines, networking) required for the Kubernetes cluster.
   - Ensure the provisioned infrastructure aligns with best practices and can support the deployment of the application.

Deliverables:

1. Jenkins Pipeline:
   - Provide the Jenkins pipeline script (Jenkinsfile) that defines the complete CI/CD process, including build and deployment stages.

2. Dockerfile:
   - Share the Dockerfile used to containerize the application.

3. Argo CD Application:
   - Share the Argo CD application definition, including the configuration that points to the Git repository and ensures continuous deployment.

4. Bonus Deliverables (if attempted):
   - Helm Chart: Share the Helm chart used for deploying the application to Kubernetes.
   - Terraform Configuration: Share the Terraform configuration files used for provisioning the Kubernetes infrastructure.

Feel free to use any additional tools or technologies that you believe will enhance the solution and showcase your expertise in the DevOps domain.


Thank you for your effort!
And Best of luck!
