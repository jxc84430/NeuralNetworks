
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import os
import pandas as pd

# Store the video frames in the specified path
def find_details(file_path,
                 keys=["dominant_race",
                       "dominant_emotion",
                       "age", "dominant_gender"]):
    try:
       pixels = cv2.imread(file_path)
       predictions = []
       try:
            if pixels is not None:
                predictions = DeepFace.analyze(pixels)
       except ValueError:
               predictions = ""
                
    except TypeError:
            predictions = ""
        
    required_predictions = []
    res=[]
    for i in predictions:
        for key in keys:
            res.append(predictions[0][key])
    [required_predictions.append(x) for x in res if x not in required_predictions]
    return  required_predictions
    
def get_content_list(path):
    return os.listdir(path)


def check_race(base_path,
               required_predictions=["dominant_race",
                                     "dominant_emotion",
                                     "age", "dominant_gender"]):
    folder_list = get_content_list(base_path)
    for folder in folder_list:
        file_list = get_content_list(f"{base_path}/{folder}")
        cur_dict = {}
        
        for file in file_list:
            cur_dict[file] = find_details(f"{base_path}/{folder}/{file}",
                                          keys=required_predictions)
       
        df = pd.DataFrame.from_dict(cur_dict, orient="index", 
                                    columns=required_predictions).reset_index().rename(columns={"index":"frame"})
        df.dropna(inplace = True)
        df["age"] = df['age'].astype('int')
        df.to_csv(f"{base_path}/{folder}/{folder}.csv", index=False)
              
def main():
    check_race(base_path="/Users/janu/Documents/UCM/Spring_2023/NeuralNetworks/project/Frames")
    
    
if __name__ == "__main__":
    main()
