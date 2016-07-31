import os 
import settings 
import pandas  as pd
from sklearn import cross_validation 
from sklearn.linear_model import LogisticRegression 
from sklearn import metrics 


def cross_validate(train, seed=42):
     clf = LogisticRegression(random_state=1, class_weights="balanced")

     predictors = train.columns.tolist()
     predictors = [p for p in predictors if p not in settings.CONFIG.NON_PREDICTORS]
   
     predictions = cross_validation.cross_val_predict(clf,
          train["predictors"], trian[settings.CONFIG.TARGET]), 
          cv = settings.CONFIG.CV_FOLDS)
     return predictions


def compute_error(target, predictions):
    return metrics.accuracy_score(target, predictions)


def compute_false_negative(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 1) & (df["predictions"] == 0)].shape[0] / (df[(df["target"] == 1)].shape[0] + 1)


def compute_false_positive(target, predictions):
    df = pd.DataFrame({"target": target, "predictions": predictions})
    return df[(df["target"] == 0) & (df["predictions"] == 1)].shape[0] / (df[(df["target"] == 0)].shape[0] + 1)


def read():
    train = pd.read_csv(os.path.join(settings.GLOBAL_DIR.PROCESSED_DIR, "train.csv"))


if __name__ == "__main__":
    train = read()
    predictions = cross_validate(train)
    acc_score = compute_error(train[settings.CONFIG.TARGET], predictions)
    fn = compute_false_negative(train[settings.CONFIG.TARGET], predictions)
    fp = compute_false_positive(train[settings.CONFIG.TARGET], predictions)

    print("Accuracy Score: {:.3f}".format(acc_score))
    print("False Negatives: {:.3f}".format(fn))
    print("False Positives: {:.3f}".format(fp))

    