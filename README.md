# Development and Implementation of an Analytical Framework to Predict Unemployment Patterns in India over the Last Decade using Machine Learning Techniques.

A Streamlit-based research dashboard for exploring unemployment patterns in India and presenting a short-horizon, state-level machine-learning analysis.

## Project modules

- Unemployment Trends
- State Intelligence
- Demographic Patterns
- Economic Drivers
- Survey & Skill Gap
- ML Prediction
- Decision & Policy
- Data & Methodology

## Data coverage

The project includes PLFS indicators for 2017-18 to 2023-24, state-level indicators, demographic and economic datasets, model evaluation outputs, and an exploratory survey dataset.

## Run locally

1. Install Python (a version supported by the packages in `requirements.txt`).
2. Create and activate a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. From this project directory, start the app:

   ```bash
   streamlit run Introduction.py
   ```

## Model interpretation

The selected model is a Lag-Only Linear Regression model. Its temporal-validation metrics and final 2023-24 test metrics are recorded in `data/model_metadata.json`. The metadata also records that the Persistence Baseline slightly outperformed Linear Regression on the final unseen test period. Treat the model as a short-horizon estimation exercise, not a causal model or long-term forecast.

## Data privacy note

`data/Survey_Cleaned_Responses.csv` contains row-level survey responses. It does not show direct identifier columns in its current schema, but combinations of demographic and employment attributes may still be sensitive. Before making this repository public, confirm that respondents gave permission for public sharing. Otherwise, keep the repository private or remove/replace the row-level survey file and update the Survey & Skill Gap page accordingly.

## Notes

- Do not upload `.venv`, `__pycache__`, `.pyc` files, passwords, API keys, or personal credentials.
- This repository archive excludes the local virtual environment and empty placeholder files.
- Check the app locally after installing dependencies before deploying it.
