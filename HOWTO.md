# Welcome to Connect Extension project Email Service

## Next steps

You may open your favorite IDE and start working with your project, please note that this project runs using docker.
You may modify at any time the credentials used to authenticate to connect modifying the file:

*emailservice/.emailservice_dev.env*


In order to start your extension as standalone docker container you can access the project folder and run:

**$ docker compose up emailservice_dev**


please note that in this way you will run the docker container and if you do changes on the code you will need to stop it and start it again.
If you would like to develop and test at same time, we recommend you to run your project using the command

**$ docker compose run emailservice_bash**


Once you get the interactive shell, you can run your extension using the command `cextrun`, stopping the process (using ctrl+c) and starting it back will reload the changes.

Additionally, a basic boilerplate for writing unit tests has been created, you can run the tests using

**$ docker compose run emailservice_test**


## Scheduled Methods
In *emailservice/extension.json* file you can find the following section:
```
"schedulables": [
    {
      "name": "Schedulable method mock",
      "description": "It can be used to test DevOps scheduler.",
      "method": "execute_scheduled_processing"
    }
  ],
```
Please modify this section to add methods which you need to be executed periodically, i.e. you need to perform monthly usage collection etc.
If you do not have any scheduled methods, please remove this section. The method name specified in `method` property must be defined in your Extension class. 
The method definition is the following: 
``` 
def execute_scheduled_processing(self, schedule):
    ...
```
Details of a scheduled method above is just an example, you set your own name, description and method names. 


## Environment variables
You may add environment variables used by the extension on the descriptor file `extension.json`:

    "variables":[
        {
            "name": "SECURE_VAR",
            "secure": true
        },
        {
            "name": "NOT_SECURE_VAR",
            "initial_value": "https://example.com",
            "secure": false
        }
    ]

* *Secure variables*:
You can add secure variables just setting the attribute `secure` to **true**. These sort of variables are secret, then the value is stored encrypted and never is displayed.
* *Standard variables*:
They are standard ones, not storing sensible data.

## Community Resources

Please take note about this links in order to get additional information:

* https://connect.cloudblue.com/
* https://connect.cloudblue.com/community/modules/devops/
* https://connect.cloudblue.com/community/sdk/python-openapi-client/
* https://connect-openapi-client.readthedocs.io/en/latest/
