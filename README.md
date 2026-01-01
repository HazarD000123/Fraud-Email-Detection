# Fraud-Email-Detection
Fraud Email Detection with Explainable Machine Learning Using a Linear SVM and Generative AI

Links to data sets:
https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=Enron.csv
https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset?select=phishing_email.csv

## How to Reproduce the Results

1. Download the datasets from the links above.
2. Download all the files as a zip, extract it, and place the data sets in the same folder.
3. In the file 'training_svm_model.ipynb', replace df and df2 with your own paths to the datasets.
4. In the 8th code block, it requires an OpenAI key in line 2, you can get that from https://platform.openai.com/api-keys.
5. Open your terminal, and paste this in {export OPENAI_API_KEY="your_api_key_here".}
6. Then just run {python app.py}
7. Click the link that shows up in the terminal and open it in your browser. You can now start using it!
