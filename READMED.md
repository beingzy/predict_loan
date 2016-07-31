Predict Loan
------------
*Objective*: A practice to learn how to manage an operational data science project, by following [tutorial](https://www.dataquest.io/blog/data-science-portfolio-machine-learning/)

*Description*:  Predict whether or not loans acquired by Fannie Mae will go into foreclosure.  Fannie Mae acquires loans from other lenders as a way of inducing them to lend more.  Fannie Mae releases data on the loans it has acquired and their performance afterwards [here](http://www.fanniemae.com/portal/funding-the-market/data/loan-performance-data.html).


Summary:
--------
1. error correction: there are typos had been corrected, 
e.g. HEADERS["Performance"] had been originally defined with 27 columns. The actual columns
in performance data files downloaded from Fannie Mea has 29 columns;

2. this is a very good tutorial to showcase the structure of operational machine lerning project.
This project is designed to be easily updated with arriving new data files. 

3. This project is emphasized on the end-to-end workflow of building a model. Therefore, below
are steps had been overlooked intentionally:
    * simplified processing of model selection (only Logistic Regression had been tried, no hyper-parameter tuning,
and no alternative algorithms either)
    * no coverage on deploying the production 
        a) for batch fashion, utilizing trained model to screen loan data base periodically 
    to highlight the current status of models. 
        b) Or, buidling a API to communicate with predict method of trained model, 
    it can query for assessment of an individual loan. 

4. some insights regarding statistics summary and visualization reports could be made to buidl contextualized
understanding of the data. 
