 # AWS Continuous Integration Demo Guideline

**Step 1**: 
## Set Up GitHub Repository

To get started with our Continuous Integration (CI) process, we'll need to set up a GitHub repository to store the source code for our Python application. If you already have one, you can skip this part. Otherwise, here’s how to create a new repository on GitHub:
- Head over to github.comand log into your account.
- Click the "+" icon in the top-right corner and select "New repository."
- Assign a name to your repository and optionally add a description.
- Select the visibility setting that fits your requirements.
- Initialize the repository by adding a README file.
- Hit the "Create repository" button to finalize the setup.
Awesome! With your repository now set up, we can proceed to the next step.


**Step 2:**
## Create an AWS CodePipeline
Creating an AWS CodePipeline to automate the continuous integration of our Python app involves several key steps. Here’s a breakdown:

- Access AWS CodePipeline through the AWS Management Console.
- Click "Create pipeline" to begin the setup.
- Name your pipeline and proceed by clicking "Next".
- For the source stage, choose "GitHub" as the source provider.
- Link your GitHub account to AWS CodePipeline and select the desired repository.
- Choose the branch to be used for the pipeline.
- For the build stage, pick "AWS CodeBuild" as the build provider.
- Create a CodeBuild project by clicking "Create project".
- Set up the CodeBuild project with necessary settings (build environment, build commands, artifacts) for your Python app.
- Save the CodeBuild project and return to CodePipeline.
- Configure remaining pipeline stages, such as deploying the app using AWS Elastic Beanstalk or another suitable option.
- Review your pipeline configuration and complete the setup by clicking "Create pipeline".
- 
Once your pipeline is created, it will streamline the flow from your GitHub repository to the deployment of your application.

Great work! Our pipeline is now up and running. Let's proceed to the next phase, where we'll configure AWS CodeBuild.


**Step 3:**
## Configure AWS CodeBuild

In this step, we'll configure AWS CodeBuild to build our Python app according to the specifications we set. CodeBuild will handle the building and packaging for deployment. Here’s how to do it:

- Open the AWS Management Console and go to the AWS CodeBuild service.
- Click on “Create build project”.
- Enter a name for your build project.
- For the source provider, select "AWS CodePipeline".
- Choose the pipeline you set up in the previous step.
- Configure the build environment by specifying the operating system, runtime, and compute resources needed for your Python app.
- Define the build commands, such as installing dependencies and running tests, tailored to your application’s requirements.
- Set up the artifacts configuration to produce the necessary build output for deployment.
- Review all settings for the build project and click “Create build project” to finalize it.

Wonderful! With AWS CodeBuild now configured, we’re ready to see continuous integration in action.


**Final Step 4:**
## Trigger the CI Process

To initiate the CI process, we’ll start by making a change in our GitHub repository:

- Access your GitHub repository and modify the source code of your Python application. This could be a bug fix, a new feature, or any other change you wish to implement.
- Commit and push your changes to the branch that is configured in your AWS CodePipeline.
- Go to the AWS CodePipeline console and locate your pipeline.
- The pipeline will automatically start once it detects changes in the repository.
- Relax while AWS CodePipeline handles everything: it will pull the latest code, initiate the build process with AWS CodeBuild, and deploy the application if the deployment stage is configured.

With this setup, your CI process is now automated and ready to roll!
