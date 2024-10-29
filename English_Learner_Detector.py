class_names = ["academic eld 1b", # English Learner
               "english1clapvl",
               "english1clbpvl",
               "Eng 2C L A P VL",
               "Eng 2C L A P VL",
               "Int.Math1LA VL",
               "Int.Math1LB VL",
               "Int.Math 2LAVL",
               "Economics C L P",
               "Academic ELD 1A",
               "Eng4ERWC CL A",
               "Int. Math 3 L A",
               "Chem 1C L A P",
               "US Hist C L A P", #trans_redacted_1... ?
               "Academic ELD 1A",
               "Eng 3C L A P",
               "Int. Math 2 L A",
               "Physio C L A P",
               "Dance 1A P", # ?????
               "US Hist C L B P",
               "Academic ELD 1B",
               "Eng 3C L B P",
               "Int. Math 2 L B",
               "Physio C L B P",
               "Am Govt CL P",
               "Academic ELD 1A"
               "Eng4ERWC CL A",
               "Economics C L P",
               "Academic ELD 1B",
               "Eng4ERWC CL B",
               "WldHist C L A P", # trans_redacted_2
               "Eng 2C L A P",
               "Academic ELD 1A",
               "Int. Math 2 L A",
               "Chem 1C L A P",
               "WldHist C L B P",
               "Eng 2C L B P",
               "Aademic ELD 1B",
               "Int. Math 2 L B",
               "Chem 1C L B P",
               "US Hist C L A P",
               "Academic ELD 2A",
               "Eng 3C L A P",
               "Int. Math 3 L A",
               "Biology1C L A P",
               "Physics CLAP",
               "US Hist C L B P",
               "Academic ELD 2B",
               "Eng 3C L B P",
               "Int. Math 3 L B",
               "Biology1C L B P",
               "Physics CLBP",
               "Economics C L P",
               "Academic ELD 3A",
               "Eng4ERWC CL A",
               "Am Govt CL P",
               "Academic ELD 3B",
               "Eng4ERWC CL B",
               "US Hist C L A P", # trans_redacted_3
               "Academic ELD 1A", # Reading, Oral & W... ?
               "Eng 3C L A P",
               "Am Govt CL P",
               "Eng 2C L A P",
               "Academic ELD 1A",
               "Eng4ERWC CL A",
               "Int. Math 2 L A",
               "Biology1C L A P",
               "US Hist C L B P",
               "Economics C L P",
               "Pre AP Eng2CLB",
               "Academic ELD 1B",
               "Eng4ERWC CL",
               "Economics C L P",
               "Pre AP Eng2CLB",
               " Academic ELD 1B",
               "Eng4ERWC CL B",
               "Int. Math 2 L B",
               "Biology1C L B P",
               "US Hist C L A P",
               "Academic ELD 1A",
               "Eng 3C L A P",
               "Int. Math 2 L A",
               "Physio C L A P",
               "US Hist C L B P",
               "Academic ELD 1B",
               "Eng 3C L B P",
               "Int. Math 2 L B",
               "Physio C L B P",
               "Eng 2C L A P VL",
               "Int.Math1LA VL",
               "Int. Math2LBVL",
               "Wld HistoryA VL",
               "Economics C L P",
               "Academic ELD 1A",
               "Eng4ERWC CL A",
               "Int. Math 3 L A",
               "Chem 1C L A P",
               "Am Govt CL P",
               "Academic ELD 1B",
               "Eng4ERWC CL B",
               "Chem 1C L B P",
               "English1C L A P", # trans_4_redacted
               "Academic ELD 3A",
               "English1C L B P",
               "Academic ELD 3B",
               "Eng 2C L A P",
               "Eng 2C L B P",
               "Academic ELD 2B",
               "Academic ELD 3A",
               "Eng 3C L A P",
               "Academic ELD 3B",
               "Eng 3C L B P",
               "Am Govt CL P", # ???
                "Academic ELD 3A",
                "Eng4ERWC CL A",
                "Am Govt CL P",
                "Academic ELD 3A",
                "Eng4ERWC CL A",
                "Int. Math 3 L A",
                "Wld Hist C B P VL C",
                "Wld HistoryA VL C",
                "Economics C L P",
                "Academic ELD 3B",
                "Eng4ERWC CL B",
                "Int. Math 3 L B",
                "English1C L A P", # trans_redacted_5
                "Academic ELD 3A",
                "PLTW-PrinBioMA", # ??
                "English1C L B P",
                "Academic ELD 3B",
                "PLTW-PrinBioMB", # ??
                "Eng 2C L A P",
                "Academic ELD 2A",
                "Eng 2C L B P",
                "Academic ELD 2B",
                "Academic ELD 3A",
                "Eng 3C L A P",
                "Academic ELD 3B",
                "Eng 3C L B P",
                "Am Govt CL P",
                "Academic ELD 3A",
                "Eng4ERWC CL A",
                "Int. Math 3 L A",
                "Wld Hist C B P VL",
                "Wld HistoryA VL",
                "Economics C L P",
                "Academic ELD 3B",
                "Eng4ERWC CL B",
                "Int. Math 3 L B",   
                "English1C L A P", # trans_redacted_6
                "Academic ELd 2A",
                "English1C L B P",
                "Academic ELD 2B",
                "Academic ELD 3A",
                "Eng 3C L A P",
                "Academic ELD 3B",
                "Eng 3C L B P",
                "Int. Math 2B VL", # ?
                "Int. Math 3A VL", # ?
                "Int. Math 3B VL",
                "Academic ELD 3A",
                "Eng4ERWC CL A",
                "Physics CLAP", # ?
                "Economics C L P",
                "Academic ELD 3B"
               ] 



def check_for_english_learner(rows):
    english_learner = False
    for row in rows:
        current_row = ""
        for text in row["text"]:
            current_row += " " +str(text)
        for class_title in class_names:
            if class_title in current_row:
                # print()
                # print("~English Learner Match~")
                # print("Current row:")
                # print(current_row)
                # print("matching course:")
                # print(class_title)
                english_learner = True
    return english_learner