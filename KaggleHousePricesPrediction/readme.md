Kaggle House Price prediction using a pipeline
https://www.kaggle.com/drscarlat/house-prices-all-done-via-pipeline
https://www.kaggle.com/kabure/houseprices-pipeline-featuretools-tpot

[Dataset transformations with scikit](https://scikit-learn.org/stable/data_transforms.html)
[Sklearn-pandas](https://github.com/scikit-learn-contrib/sklearn-pandas)

Project structure. For more details see https://drivendata.github.io/cookiecutter-data-science/

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Folder for more polished work.
|   └── exploratory    <- Naming convention is a number (for ordering),
|                         the creator's initials, and a short `-` delimited description, e.g.
|                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- Make this project pip installable with `pip install -e`
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
```

**Notes:**

## Notebooks are for exploration and communication
Notebook packages like the `Jupyter notebook` are very effective for exploratory data analysis. However, these tools can be less effective for reproducing an analysis. Consider subdividing the notebooks folder. For example, notebooks/exploratory can contain initial explorations, whereas notebooks root folder is for more polished work that can be exported as html to the reports directory.

Since notebooks are challenging objects for source control (e.g., diffs of the json are often not human-readable and merging is near impossible), recommended not collaborating directly with others on Jupyter notebooks. There are two steps to use notebooks effectively:
1. Follow a naming convention that shows the owner and the order the analysis was done in. We use the format `step-ghuser-description.ipynb` (e.g., `0.3-bull-visualize-distributions.ipynb`).

2. Refactor the good parts. Don't write code to do the same task in multiple notebooks. If it's a data preprocessing task, put it in the pipeline at `src/data/make_dataset.py` and load data from `data/interim`. If it's useful utility code, refactor it to src.

[Another advise how to work with `notebooks` folder:](https://medium.com/swlh/how-to-structure-a-python-based-data-science-project-a-short-tutorial-for-beginners-7e00bff14f56)

**Jupyter notebooks**: All experimental code is kept in the notebooks folder. When completed, code is put into a function and migrated to the appropriate subfolder under `src` and read back into a new notebook. Below is a sample pipeline for simple project workflow.

See also: [Pipelines and Project Workflow](https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow) *The original article describing the workflow mentioned above*