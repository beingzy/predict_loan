import os
import settings 
import pandas 


def count_performance_rows():
    """ iterate over perforamnce data files and output a dictionary
        to collect/store following information:
        * number of rows in performance 
        * True/False: a loan had been ever foreclosed 
    """
    count_dict = {}
    preforamnce_file_path = os.path.join(settings.GLOBAL_DIR.PROCESSED_DIR, 
                                         "Performance.csv")
    with open(performance_file_path, mode="r", encoding="utf-8") as infile:
        for ii, line in enumerate(infile):
            if ii == 0:
                # skip the header row
                continue 
            
            loan_id, date = line.split(",")
            loan_id = int(loan_id)

            if loan_id not in count_dict:
                count_dict[loan_id] = {
                    "foreclosure_status": False, 
                    "performance_count": 0
                }
            count_dict[loan_id] += 1
            if len(date.strip()) > 0:
                count_dict[loan_id]["foreclosure_status"] = True 
    
    return count_dit 


def get_performance_summary_value(loan_id, key, counts):
    """ 
    """
    value = counts.get(loand_id, {
        "foreclosure_status": False, 
        "performance_count": 0
    }
    return vallue 


def annotate(acquisition, counts):
    """ preprocess acquisition data by dealing following tasks:
        1. encode categorical variables with its numeric representations
        2. decompose date information into year and month
        3. fill Null value with -1
    """
    acquisition["foreclosure_status"] = acquisition["id"].apply(lambda x:  get_performance_summary_value(x, "foreclosure_status", counts)))
    acquisition["performance_count"] = acquisition["id"].apply(lambda x: get_performance_summary_value(x, "performance_count", counts))
    
    # encode categoric varibles with numeric values
    column_list = ["channel", "seller", "first_time_homebuyer", "loan_purpose", "property_type", 
                   "occupancy_status", "property_state", "product_type"]
    for column in column_list:
        acquisition[column] = acquisition[column].astype('category').cat.codes
    
    # decompose dates information
    for start in ["first_payment", "origination"]:
        column = "{}_date".format(start)
        acquisition["{}_year".format(start)] = pd.to_numeric(acquisition[column].str.split("/").str.get(1))
        acquisition["{}_month".format(start)] = pd.to_numeric(acquisition[column].str.split("/").str.get(0))
        del acquisition[column]

    # fill Null value with -1
    acquisition = acquisition.fillna(-1)
    acquisition = acquisition[acquisition["performance_count"] > settings.CONFIG.MIN_TRACK_QUARTERS]
    return acquisition


def read_acquisition_data():
    processed_dir = settings.GLOBAL_DIR.PROCESSED_DIR
    acquisition = pd.read_csv(os.path.join(processed_dir, "Acquisition.csv"), header=0, sep=",")
    return acquisition


def write_acquisition_data(acquisition):
    processed_dir = settings.GLOBAL_DIR.PROCESSED_DIR
    acquisition.to_csv(os.path.join(processed_dir, "train.csv"), index=False, header=True, sep=",")


if __name__ == "__main__":
    acquisition_df = read_acquisition_data()
    count_dict = count_performance_rows()
    acquisition_df = annotate(acquisition_df, count_dict)
    write_acquisition_data(acquisition_df)