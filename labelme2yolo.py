import json
import os
import cv2

# Define the path to the LabelMe JSON directory and the output directory
json_dir = "~/datasets/train/labelme_json_dir"
out_dir = "~/datasets/train/yolo_format"

# Define the class names used in the dataset
classes = ["aluminum", "speaker", "motor", "pcb", "plastic case", "robot", "button", "unknown", "cart handle", "camera"]

# Iterate over each JSON file in the directory
for json_file in os.listdir(json_dir):
    # Check if the file is a JSON file
    if not json_file.endswith(".json"):
        continue

    # Get the path to the JSON file
    json_path = os.path.join(json_dir, json_file)

    # Check if the file is empty
    if os.path.getsize(json_path) == 0:
        print("Skipping empty file: %s" % json_path)
        continue

    # Load the JSON file as a dictionary
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except ValueError:
        print("Skipping invalid JSON file: %s (size=%d bytes)" % (json_path, os.path.getsize(json_path)))
        continue

    # Load the image using OpenCV
    img_path = os.path.join(os.path.dirname(os.path.join(json_dir, json_file)), data["imagePath"])
    img = cv2.imread(img_path)
    img_height, img_width, _ = img.shape

    # Create the output YOLO file path
    out_file = os.path.splitext(os.path.basename(json_file))[0] + ".txt"
    out_path = os.path.join(out_dir, out_file)

    # Open the output YOLO file and write the object annotations
    with open(out_path, "w") as f:
        for shape in data["shapes"]:
            # Get the class ID for this object
            try:
                class_id = classes.index(shape["label"])
            except ValueError:
                print("Skipping unknown class label '%s'" % shape["label"])
                continue

            # Get the bounding box coordinates
            x1 = shape["points"][0][0]
            y1 = shape["points"][0][1]
            x2 = shape["points"][1][0]
            y2 = shape["points"][1][1]

            # Convert the bounding box coordinates to YOLO format
            x_center = (x1 + x2) / (2.0 * img_width)
            y_center = (y1 + y2) / (2.0 * img_height)
            width = abs(x2 - x1) / img_width
            height = abs(y2 - y1) / img_height

            # Write the object annotation to the output file
            f.write("%d %f %f %f %f\n" % (class_id, x_center, y_center, width, height))