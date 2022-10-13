# Workflow overview

## Implementation

### Workflow file
The workflow here is just a saved copy of the one we're trying to implement in the backend repository.
It will not run without the backend app which is not saved in this repo (currently)

### Tests
The tests we run in this workflow are found in the ```test/``` directory. 

- To add more tests simply add the files in the test folder directly or in their own folders.
- We have put them in separate folders to make it easier to run specific tests. 
for example we currently only run the backend tests since the others are not yet implemented.

- See these lines in the ```backend-CI.yml``` file
- ```
    # Executes the tests within the /backend_tests folder 
    - name: Run PyTest
      run: python -m pytest ./test/backend_tests --junit-xml=report.xml ```
 
 ### In order to run new tests you can either:
 - Add additional tasks similar to the one above. 
 - Add additional tests in the file already run.
 - Use the pipe functionality to run multiple calls in one task, see below.
 - ```
    # Executes the tests in /backend_tests & /user_tests folders
    - name: Run PyTest
      run: |
          python -m pytest ./test/backend_tests
          python -m pytest ./test/user_tests ```

### The .env File
  The environment file should not be publicly available, we therefor want to use github secrets. 
  Secrets can be used in a github action to obfuscate the sensitive data.
  - a secret can be called by invoking this syntax in a workflow ``` ${{ secrets.NAME_OF_SECRET }}``` where NAME_OF_SECRET is the name specified when the secret was created in github
  - We have a template .env file called .env.example which should specify all variables that need to be set in order for the backend app to function properly
  - These variables are set in our workflow and a .env file is created by the action: <a href="https://github.com/marketplace/actions/create-env-file">Create .env File</a>
  - For example this line ``` #envkey_ADMIN_POOL_SECRET: ${{ secrets.ADMIN_POOL_SECRET }} ``` creates the key: ADMIN_POOL_SECRET with the value stored in the the respective secret.

### host.docker.internal:host-gateway
- inside our branch in the backend repo we have added this line to the ```docker-compose.yml ``` file
- ``` 
    extra_hosts:
        - "host.docker.internal:host-gateway"
- This line adds the ability to understand that localhost calls should refer to the runners localhost. Without this specified the tests in the workflow will be unable to connect to the local backend app.
