"""
Controller responsible for manipulate the images
"""
import uuid
import pathlib
import requests
import textwrap

from app.result import Response
from app.schema import schema_validate, draw_schema

from PIL import Image, ImageDraw, ImageFont
from flask import Blueprint, jsonify, request, current_app, send_file

bp_image = Blueprint(name=__name__, import_name=__name__)


@bp_image.route("/images/<filename>", methods=["GET"])
def retrieve_image(filename):
    """
    Blueprint method to get one image from the server
    """
    return send_file(f"{current_app.config['IMAGES_DIR']}/{filename}")


@bp_image.route("/draw", methods=["POST"])
@schema_validate(draw_schema)
def draw_text_box():
    """
    Blueprint method to draw a text box on the image
    """
    json = request.get_json()

    font_file = _save_remote_file(file_url=json["font_url"], extension="ttf")
    image_file = _save_remote_file(file_url=json["image_url"], extension="jpg")
    text_splits = _font_box_fit(box_size=json["box"], box_text=json["text"]["content"], font_file=str(font_file))

    resource = _generate_image(json, text_splits, str(font_file), str(image_file))
    font_file.unlink()
    image_file.unlink()  # remove temp files

    return jsonify({"box": json["box"], "splits": text_splits, "resource": resource})


def _save_remote_file(file_url: str, extension: str) -> pathlib.Path:
    """
    Helper method to save a local file form the remote url
    """
    try:
        file_resp = requests.get(file_url)

    except requests.exceptions.RequestException:
        return Response(code=400, message="Can not get file's data from url").raise_exception()

    if file_resp.status_code != 200:
        return Response(code=400, message="Can not get file's data from url").raise_exception()

    file_path = pathlib.Path(f"{current_app.config['IMAGES_DIR']}/{uuid.uuid4().hex[:16]}.{extension}")
    file_path.write_bytes(file_resp.content)

    return file_path


def _font_box_fit(box_size: dict, box_text: str, font_file: str) -> list:
    """
    Helper method to fit the content inside a predefined box
    """
    width, height = box_size["width"] * 0.95, box_size["height"] * 0.95
    shift_x, shift_y = box_size["width"] * 0.02, box_size["height"] * 0.025

    longest_word_len = len(max(box_text.split(), key=len))
    total_text_len = len(box_text)

    for font_size in range(120, 6, -1):
        font = ImageFont.truetype(font_file, font_size)  # assume that the ideal font size is between 6 - 120

        for text_width in range(longest_word_len, total_text_len, 1):
            split_text = []
            font_weight, font_height = 0, 0

            for line in textwrap.wrap(box_text, width=text_width):
                split_text.append(line)
                font_height += font.getsize(line)[1]
                font_weight = max(font_weight, font.getsize(line)[0])

            if font_weight >= width:  # one word is longer than box width
                break

            if font_height + len(split_text) * 2 < height:  # words are shorter than box height
                return _box_fit_response(box_size, split_text, font_size, shift_x, shift_y)

    return Response(code=400, message="Can not make a text fit in a box").raise_exception()


def _box_fit_response(box_size: dict, split_text: list, font_size: int, shift_x: float, shift_y: float) -> list:
    """
    Helper method to build one splits result
    """
    splits, y_value = [], box_size["y"] + shift_y

    for content in split_text:
        split = {
            "content": content, "font_size": font_size,
            "x": int(box_size["x"] + shift_x), "y": int(y_value),
        }
        splits.append(split)
        y_value += font_size

    return splits


def _generate_image(json: dict, text_splits: list, font_file: str, image_file: str) -> str:
    """
    Helper method to generate one image and save in the local
    """
    source_img = Image.open(image_file)
    draw = ImageDraw.Draw(source_img)

    x, y, w, h = json["box"]["x"], json["box"]["y"], json["box"]["width"], json["box"]["height"]
    draw.rectangle(((x, y), (x + w, y + h)), outline=json["text"]["border_color"])

    for split in text_splits:
        font = ImageFont.truetype(font_file, split.get("font_size"))
        draw.text((split["x"], split["y"]), split["content"], font=font, fill=json["text"]["text_color"])

    filename = f"{uuid.uuid4().hex[:16]}.jpg"
    source_img.save(f"{current_app.config['IMAGES_DIR']}/{filename}", "JPEG")

    image_url = f"{current_app.config['API_BASE_URL']}images/{filename}"
    current_app.logger.info(f"Generate one image url - {image_url}")

    return image_url
