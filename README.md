![image info](./images/logo.png)

## About

The point of these exercises is to give you the chance to show us what you know, 
can do and how you approach problem-solving.

When you feel you are ready, please email us your code solution and how we can run it.
In your email you must include that this is your original work and was completed only by you.

## Project setup

1. Create a virtual environment
    
    ```shell
    virtualenv -p python3 <name of virtualenv>
    source <name of virtualenv>/bin/activate
    ```

1. Install all requirements

    ```shell
    pip install -r requirements.txt
    ```

1. Run the server

    ```shell
    python manage.py run
    ```
   
1. Run the test cases

    ```shell
    python -m pytest -v
    ```


## Code exercises

#### Draw a text box inside the image

In this part, we want you to determine the suitable font size that will make the **content** fit inside 
a predefined box based on a particular font, and draw this **text box** on an image provided by user.

We should be able to make the request to this endpoint: `[POST] /api/v1/draw/`.

The input data should look like this:

```json
{
    "font_url": "https://storage.googleapis.com/dipp-massimo-development-fonts/4f2cf2b6b99d96ca.ttf",
    "image_url": "https://storage.googleapis.com/dipp-massimo-development-images/1f1282fef735f349.jpg",
    "text": {
        "content": "Dipp inc, thinking out of how to draw a text on the box.",
        "text_color": "#000000",
        "border_color": "#000000"
    },
    "box": {
        "x": 40,
        "y": 100,
        "width": 500,
        "height": 180
    }
}
```

The API should respond with an output similar to the following:

```json
{
    "resource": "http://localhost:8080/api/v1/images/82a78a5d46b443cd.jpg",
    "splits": [
        {
            "content": "Dipp inc, thinking",
            "font_size": 57,
            "x": 40,
            "y": 100
        },
        {
            "content": "out of how to draw",
            "font_size": 57,
            "x": 40,
            "y": 157
        },
        {
            "content": "a text on the box.",
            "font_size": 57,
            "x": 40,
            "y": 214
        }
    ],
    "box": {
        "x": 40,
        "y": 100,
        "width": 500,
        "height": 180
    }
}
```

As you may have noticed, you may need to break the **content** into multiple lines or splits to fit a box.


#### Get one image from the server

You need to use previous API `[POST] /api/v1/draw/` to generate an image and save it 
to the file system. Afterwards, users can get an image by the url link located in the server.

We should be able to make the request to this endpoint: `[GET] /api/v1/images/<filename>/`. 

The output image should look like this:

![Output](images/sample.png)


### Important notes:

- There is no **right** or **wrong** answer. We are interested in how you approach problem-solving.
- Please fill free to use any library you want but don't forget to add it in `requirements.txt`
- Please fill free to refactor the code if the structure does not fit your needs.
- Please don't hesitate email us if you have any questions.


### Good luck !!!
