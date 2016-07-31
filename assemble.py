import os 
import pandas as pd 
import settings # project information


# ============================================
# define variables to house column information
# ============================================
HEADERS = {
    "Acquisition": [
        "id",
        "channel",
        "seller",
        "interest_rate",
        "balance",
        "loan_term",
        "origination_date",
        "first_payment_date",
        "ltv",
        "cltv",
        "borrower_count",
        "dti",
        "borrower_credit_score",
        "first_time_homebuyer",
        "loan_purpose",
        "property_type",
        "unit_count",
        "occupancy_status",
        "property_state",
        "zip",
        "insurance_percentage",
        "product_type",
        "co_borrower_credit_score"
    ],
    "Performance": [
        "id",
        "reporting_period",
        "servicer_name",
        "interest_rate",
        "balance",
        "loan_age",
        "months_to_maturity",
        "adj_months_to_maturity", # updated
        "maturity_date",
        "msa",
        "delinquency_status",
        "modification_flag",
        "zero_balance_code",
        "zero_balance_date",
        "last_paid_installment_date",
        "foreclosure_date",
        "disposition_date",
        "foreclosure_costs",
        "property_repair_costs",
        "recovery_costs",
        "misc_costs",
        "tax_costs",
        "sale_proceeds",
        "credit_enhancement_proceeds",
        "repurchase_proceeds",
        "other_foreclosure_proceeds",
        "non_interest_bearing_balance",
        "principal_forgiveness_balance", 
        "repurchase_whole_proceeds_flag" # updated
    ]
}

SELECT = {
    "Acquisition": HEADERS["Acquisition"],
    "Performance": [
        "id",
        "foreclosure_date"
    ]
}


# =============================
# custom function
# =============================
def concatenate(prefix):
    """load mutilple data files and combine them into
       a single one
    """
    data_dir = settings.GLOBAL_DIR.DATA_DIR
    processed_dir = settings.GLOBAL_DIR.PROCESSED_DIR

    files = os.listdir(data_dir)
    full_data = []
    for ii, file in enumerate(files):
        if not file.startswith(prefix):
            continue
        
        data = pd.read_csv(os.path.join(data_dir, file), sep="|", 
                           header=None, names=HEADERS[prefix], 
                           index_col=False)
        data = data[SELECT[prefix]]
        full_data.append(data)
    
    full_data = pd.concat(full_data, axis=0)
    
    outfile_path = os.path.join(processed_dir, prefix + '.csv')
    full_data.to_csv(outfile_path, header=True, index=False, sep=",")

    print("{} data files had been created and export to: \n{}".format(prefix, outfile_path))

# ========================
# integrating data files 
# ========================
# acquisition data: consildiation and exporting to processed/*.csv
concatenate(prefix = "Acquisition")
concatenate(prefix = "Performance")


    
