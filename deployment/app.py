import tkinter as tk
from tkinter import ttk
import pandas as pd
import joblib

# Sample data
my_data = {'Age': 30,
           'BusinessTravel': 'Travel_Rarely',
           'Gender': 'Male',
           'Department': 'Sales',
           'DistanceFromHome': 20,
           'Education': "Bachelor",
           'EnvironmentSatisfaction': 0,
           'Gender': 'Male',
           'JobInvolvement': 0,
           'JobRole': 'Healthcare Representative',
           'JobSatisfaction': 0,
           'MaritalStatus': "Divorced",
           "MonthlyIncome": 0,
           "NumCompaniesWorked": 0,
           "WorkLifeBalance": 0,
           "OverTime": "Yes"}


def get_businesstravel_values():
    return ['Travel_Rarely', 'Travel_Frequently', 'Non-Travel']

def get_gender_values():
    return ['Male', 'Female']

def get_department_values():
    return ['Sales', 'Research & Development', 'Human Resources']

def get_education_values():
    education_map = {'Bachelor': 3, 'Master': 4, 'College': 2, 'Below College': 1, 'Doctor': 5}
    return list(education_map.keys())

def get_jobrole_values():
    return ['Healthcare Representative', 'Research Scientist', 'Laboratory Technician',
            'Manufacturing Director', 'Manager', 'Sales Executive', 'Sales Representative',
            'Research Director', 'Human Resources']

def get_maritalstatus_values():
    return ["Single", "Married", "Divorced"]

def get_overtime_values():
    return ["Yes", "No"]

def get_prediction():
    # Get data from entries
    data = {
        'Age': int(entries['Age'].get()),
        'BusinessTravel': entries['BusinessTravel'].get(),
        'Gender': entries['Gender'].get(),
        'Department': entries['Department'].get(),
        'DistanceFromHome': int(entries['DistanceFromHome'].get()),
        'Education': entries['Education'].get(),
        'EnvironmentSatisfaction': int(entries['EnvironmentSatisfaction'].get()),
        'JobInvolvement': int(entries['JobInvolvement'].get()),
        'JobRole': entries['JobRole'].get(),
        'JobSatisfaction': int(entries['JobSatisfaction'].get()),
        'MaritalStatus': entries['MaritalStatus'].get(),
        "MonthlyIncome": int(entries['MonthlyIncome'].get()),
        "NumCompaniesWorked": int(entries['NumCompaniesWorked'].get()),
        "WorkLifeBalance": int(entries['WorkLifeBalance'].get()),
        "OverTime": entries['OverTime'].get()
    }

    education_map = {'Bachelor': 3, 'Master': 4, 'College': 2, 'Below College': 1, 'Doctor': 5}
    data['Education'] = education_map[data['Education']]
   
    global my_data_df
    my_data_df = pd.DataFrame([data])

    # Load the model
    loaded_model = joblib.load('log_reg_model2.joblib')

    # Make predictions
    predictions = loaded_model.predict(my_data_df)

    if predictions[0] == 1:
        prediction_text = "Attrition"
    else:
        prediction_text = "Not Attrition"

    prediction_label.config(text= prediction_text)

root = tk.Tk()
root.title("Attrition Prediction")

labels = ['Age', 'BusinessTravel', 'Gender', 'Department', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',
          'JobInvolvement', 'JobRole', 'JobSatisfaction', 'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked',
           'WorkLifeBalance', 'OverTime']

entries = {}

for i, label in enumerate(labels):
    ttk.Label(root, text=label + ":").grid(row=i, column=0, padx=5, pady=5)
    if label in ['Age', 'DistanceFromHome', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobSatisfaction',
                 'MonthlyIncome', 'NumCompaniesWorked',  'WorkLifeBalance']:
        entry = ttk.Entry(root)
        entry.grid(row=i, column=1, padx=5, pady=5)
        if label in my_data:
            entry.insert(0, str(my_data[label]))
        entries[label] = entry
    else:
        values_function = globals()["get_" + label.lower() + "_values"]
        values = values_function()
        combobox = ttk.Combobox(root, values=values, state="readonly")
        combobox.grid(row=i, column=1, padx=5, pady=5)
        if label in my_data:
            combobox.set(my_data[label])
        entries[label] = combobox

predict_button = ttk.Button(root, text="Predict", command=get_prediction)
predict_button.grid(row=len(labels), columnspan=2, padx=5, pady=10)

prediction_label = ttk.Label(root, text="")
prediction_label.grid(row=len(labels)+1, columnspan=2, padx=5, pady=5)

root.mainloop()
