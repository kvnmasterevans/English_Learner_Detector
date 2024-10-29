# import libraries
import os
import argparse
import json
from utils import standardize_image, removeText, removeTop, removeStateID, \
    run_ocr, convert_OCR_result_to_json, \
        openJpgImage, remove_extension, \
        save_image, \
        createBlackPixelProjectionProfile, remove_img_bottom
from rowUtilsNew import findTextRows
from FinalizeColumns import check_predicted_column_values
from English_Learner_Detector import check_for_english_learner
import cv2
import numpy as np

def process_single_image(file_name, input_folder_path):
    redacted_image = process_image(file_name, input_folder_path)

    filename = os.path.basename(remove_extension(file_name))
    redacted_img_path = "Redacted/" + str(filename) + '.png'
    save_image(redacted_image, redacted_img_path)

    


# should return boolean for english learner status - ( turn into .txt file / files later... )
# return un-tilted image  with tilt degrees in name
# return column edges image
#   col top, col edges, col bottoms?
def process_image(filename, input_folder_path):

    def remove_temporary_files():
        # Remove temporary image file
        OUTPUT_IMAGE_PATH = "Temp/temp.png"
        if os.path.exists(OUTPUT_IMAGE_PATH):
            os.remove(OUTPUT_IMAGE_PATH)
        # Remove temporary OCR_DATA .png
        if os.path.exists(OCR_Data_Path):
            os.remove(OCR_Data_Path)


    print("processing transcript " + str(filename) + " in folder " + str(input_folder_path))

    file_path = os.path.join(input_folder_path, filename)
    file_extension = os.path.splitext(filename)[1]


    # standardize image format
    standardized_png_path, width, height = standardize_image(file_path)
    # print("width " + str(width))
    # print("height " + str(height))

    # do ocr read if necessary
    result = run_ocr(standardized_png_path)
    OCR_Data_Path = convert_OCR_result_to_json(result, filename)

    with open(OCR_Data_Path, 'r') as json_file:
        OCR_Data = json.load(json_file)



    originalImg = openJpgImage(standardized_png_path)
    textlessImg = removeText(standardized_png_path, OCR_Data)
    toplessImg, coursesHeaderRow = removeTop(textlessImg, OCR_Data)

    # column row stuff:
    bottomlessImg = remove_img_bottom(toplessImg, coursesHeaderRow, height, width)

    projection_profile = np.sum(bottomlessImg, axis=0)

    blackPixProjProfile = createBlackPixelProjectionProfile(projection_profile)

    columns = check_predicted_column_values(blackPixProjProfile, standardized_png_path, height) # stand png path var????

    col1Rows, col2Rows, col3Rows = findTextRows(OCR_Data, columns, coursesHeaderRow)

    rows = []
    for row in col1Rows:
        rows.append(row)
    for row in col2Rows:
        rows.append(row)
    for row in col3Rows:
        rows.append(row)

    english_learner = check_for_english_learner(rows)

    print(f"english learner for {filename} = {english_learner}")
    # end column row stuff ^


    # REDACTED IMAGE
    cleanImage = cv2.imread(standardized_png_path, cv2.IMREAD_GRAYSCALE)
    semi_redacted_image, coursesHeaderRow = removeTop(cleanImage, OCR_Data)
    redacted_image = removeStateID(semi_redacted_image, OCR_Data, coursesHeaderRow)

    remove_temporary_files()

    return redacted_image, english_learner




def process_images_in_folder(folder_path):
    print("processing all images in " + str(folder_path) + " folder")
    # scan in image
     # List all files in the folder
    
    output_file_path = "output.txt"
    

    with open(output_file_path, "a") as file:
        file.write("English Learner Statuses: \n\n")
        for filename in os.listdir(folder_path):
            try:
                print()
                print(filename)
                # Construct the full file path
                file_path = os.path.join(folder_path, filename)
                
                _, eng_status = process_image(filename, folder_path)
                file.write(f"{filename} = {eng_status}\n")
                file.flush()
                print(f"finished with {filename}")
                

                # fileName = os.path.basename(remove_extension(filename))
                # redacted_img_path = "Redacted/" + str(fileName) + ".png"
                
                # save_image(redacted_image, redacted_img_path)
            except:
                print(f"some problem in processing {filename}")


def main():
    parser = argparse.ArgumentParser(description="Run OCR on images.")
    parser.add_argument('command', choices=['run'], help="The command to run.")
    parser.add_argument('target', help="The target to process: 'all' for all images in the folder or the specific image filename.")
    parser.add_argument('folder', help="The path to the folder containing images.")
    
    args = parser.parse_args()
    
    if args.command == 'run':
        if args.target == 'all':
            process_images_in_folder(args.folder)
        else:
            # image_path = os.path.join(args.folder, args.target)
            # if os.path.isfile(image_path):
            #     process_single_image(args.target, args.folder)
            # else:
            #     print(f"File {args.target} not found in folder {args.folder}")
            print("Error: Can only run for all files. haven't implemented single file yet")

if __name__ == "__main__":
    main()




