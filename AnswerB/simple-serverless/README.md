# simple-serverless
**simple-serverless** is a serverless RESTful api backed by **PostgreSQL(AWS RDS)**, can easily be deployed using **AWS Lambda**

![serverless](https://github.com/shajalahamedcse/itech-exam/blob/master/AnswerB/simple-serverless/diagram/server.jpg)

### Serverless deployment using AWS Lambda
We are using [*Zappa*](https://github.com/Miserlou/Zappa) python package to automate the process of serverless deployment.

Follow these simple steps to deploy this Flask application serverless mode

```bash
$ pip install zappa
$ zappa init
```


#### **You will be asked some questions like**

1.
```
Your Zappa configuration can support multiple production stages, like 'dev', 'staging', and 'production'.
What do you want to call this environment (default 'dev'):
```

As we are in **`development`** phase, we will set the environment to **`dev`**

2.
```
Your Zappa deployments will need to be uploaded to a private S3 bucket.
If you don't have a bucket yet, we'll create one for you too.
What do you want to call your bucket? (default 'zappa-7m8gnjbl8'):
```
Your entire application/code will be uploaded to Amazon S3(Storage service provided by Amazon). Zappa wants to create a bucket to store you application there and wants to know you want to set any custom name for the bicket.

Just simple hit **Enter** and our bucket will be named *zappa-7m8gnjbl8*

3.
```
It looks like this is a Flask application.
What's the modular path to your app's function?
This will likely be something like 'your_module.app'.
We discovered: flask_app.app
Where is your app's function? (default 'flask_app.app'): main.app
```
Zappa automatically detects the framework we are using, Flask. It asks where the Flask application instance is located.
We instantiated out `app` in `flask_app.py` file but then we registered our routes in controller file and then we imported the app from `controller.py` and run in from `main.py` file.
So we write `main.app` here and hit Enter

4.
```
You can optionally deploy to all available regions in order to provide fast global service.
If you are using Zappa for the first time, you probably don't want to do this!
Would you like to deploy this application ?[1mglobally?[0m? (default 'n') [y/n/(p)rimary]:
```
The description is self explanatory. We would not like to deploy it globally so we just hit Enter and decline the offer.

5.
```
Okay, here's your zappa_settings.json:

{
    "dev": {
        "app_function": "main.app",
        "aws_region": "ap-southeast-1",
        "profile_name": "default",
        "project_name": "simple-serverle",
        "runtime": "python3.6",
        "s3_bucket": "zappa-7m8gnjbl8"
    }
}

Does this look ?[32m?[1mokay?[0m? (default 'y') [y/n]:
```
Zappa will write this JSON in a file if you confirm that all the information are correct.
It seems everything is in place and we will hit Enter to confirm. If you want to change anything, type `n` and Zappa will let you edit the configuration.


After this step Zappa will create a file named `zappa_settings.json` in the working directory, where all your configs are stored.

Additionally we will add some environment variables for our app to work properly. As you can see the `config.py` file,
``SQLALCHEMY_DATABASE_URI`` and ``SECRET_KEY`` are loaded from environment variable. So we need to define those in our `zappa_settings.json` file.

It will look like this:
```json
{
  "dev": {
    "app_function": "main.app",
    "aws_region": "ap-southeast-1",
    "profile_name": "default",
    "project_name": "simple-serverle",
    "runtime": "python3.6",
    "s3_bucket": "zappa-yourbucketname",
    "environment_variables": {
      "SQLALCHEMY_DATABASE_URI": "postgres://postgres:dbpassword@host:5432/dbname",
      "SECRET_KEY": "very_strong_security_key"
    }
  }
}
```
We are using Postgres as out database.

We are not ready to deploy the application.

Simply execute this command:
```bash
$ zappa deploy dev
```
Zappa will take care of all the configuration, install dependencies, package the project, upload it to S3 and create API Gateway.
On completion Zappa will give you the URL where your app is deployed.
```http
Deployment complete!: https://fjsefutow9.execute-api.ap-southeast-1.amazonaws.com/dev
```

We are done with Python app serverless deployment!

### Checking the deployed API
The RESTful api we have deployed has 4 endpoints, listed bellow

- `POST /user` -> Create new User

    Example POST json body
    ```json
    {
	    "name": "shajal",
	    "email": "shajal@gmail.com",
	    "password": "123456"
    }
    ```

    In reponse it will create a new User and returns the detail with status code `201`.
    ```json
    {
        "email": "shajal@gmail.com",
        "id": 1,
        "name": "shajal"
    }
    ```

- `GET /user/:id` -> Get user detail using UserID

    Responds `200` with User detail
    ```json
    # /user/1
    {
        "email": "shajal@gmail.com",
        "id": 1,
        "name": "shajal"
    }
    ```

- `GET /user` -> Get a list of all users in database

    *NO Security!*, I know. We are just demonstrating, no worries :)

    Responds with a list of all users
    ```json
    [
        {
            "email": "shajal@gmail.com",
            "id": 1,
            "name": "shajal"
        },
        {
            "email": "zerin@gmail.com",
            "id": 2,
            "name": "zerin"
        }
    ]
    ```

- `POST /user/login` -> Check user credentials and log them in

    Example POST json body
    ```json
    {
	    "email": "shajal@gmail.com",
	    "password": "123456"
    }
    ```

    Valid credentials will return user detail with a status code of `200`
    ```json
    {
        "email": "shajal@gmail.com",
        "id": 1,
        "name": "shajal"
    }
    ```
    *Spoiler: It just redirects to `/user/:id` with UserID ;)*

    Example with invalid credentials
    ```json
    {
        "error": {
            "msg": "invalid email, password combination"
        }
    }
    ```
