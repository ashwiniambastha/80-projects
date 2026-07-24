# Project Draft: Social Video Audience Sentiment Intelligence

## Project Overview
This project is an end-to-end machine learning application designed to analyze sentiment in Social Video Audience comments. It encompasses the entire ML lifecycle, from data ingestion to deployment, leveraging MLOps best practices.

## Key Features
- **Sentiment Analysis:** Classifies Social Video Audience comments into sentiment categories (likely Positive/Negative).
- **MLOps Pipeline:** Uses DVC (Data Version Control) to manage the ML pipeline, ensuring reproducibility and versioning of data and models.
- **API Service:** Provides a Flask-based REST API for serving predictions.
- **Chrome Extension:** Includes a frontend Chrome plugin to allow users to analyze sentiment directly on YouTube.
- **CI/CD & Deployment:** Automated deployment pipeline using GitHub Actions to deploy the Dockerized application to AWS EC2 via ECR.

## Technology Stack
- **Programming Language:** Python 3.11
- **Machine Learning:**
    - **Model:** LightGBM (LGBMClassifier)
    - **Feature Engineering:** TF-IDF Vectorizer
    - **Libraries:** Scikit-learn, Pandas, NumPy
- **MLOps & Versioning:**
    - **DVC:** For pipeline orchestration and data versioning.
    - **Git:** For code versioning.
- **Backend:** Flask
- **Frontend:** HTML, JavaScript (Chrome Extension)
- **Containerization:** Docker
- **Cloud Infrastructure (AWS):**
    - **EC2:** Virtual machine for hosting the application.
    - **ECR:** Elastic Container Registry for storing Docker images.
    - **IAM:** User management for deployment permissions.
- **CI/CD:** GitHub Actions (Self-hosted runner on EC2).

## ML Pipeline Stages (DVC)
The project follows a structured pipeline defined in `dvc.yaml`:

1.  **Data Ingestion (`data_ingestion`)**
    -   **Script:** `src/data/data_ingestion.py`
    -   **Output:** `data/raw` (train/test splits)
    -   **Params:** `test_size`

2.  **Data Preprocessing (`data_preprocessing`)**
    -   **Script:** `src/data/data_preprocessing.py`
    -   **Input:** Raw train/test data.
    -   **Output:** `data/interim` (processed data)

3.  **Model Building (`model_building`)**
    -   **Script:** `src/model/model_building.py`
    -   **Input:** Processed training data.
    -   **Output:** `lgbm_model.pkl`, `tfidf_vectorizer.pkl`
    -   **Params:** `max_features`, `ngram_range`, `learning_rate`, `max_depth`, `n_estimators`

4.  **Model Evaluation (`model_evaluation`)**
    -   **Script:** `src/model/model_evaluation.py`
    -   **Input:** Models and processed data.
    -   **Output:** `experiment_info.json`

5.  **Model Registration (`model_registration`)**
    -   **Script:** `src/model/register_model.py`
    -   **Input:** `experiment_info.json`

## API Endpoints
-   **POST /predict**
    -   Input: JSON object with a list of comments.
    -   Example:
        ```json
        {
            "comments": ["This video is awsome! I loved a lot", "Very bad explanation. poor video"]
        }
        ```

## Deployment Workflow
1.  **Build:** Docker image is built from the source code.
2.  **Push:** Image is pushed to AWS ECR.
3.  **Pull & Run:** AWS EC2 instance (configured as a self-hosted GitHub Actions runner) pulls the image from ECR and runs it.

