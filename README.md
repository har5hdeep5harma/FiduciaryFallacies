<div align="center">
  <img src="https://bfoot.ru/wp-content/uploads/2023/05/1706x1280_0xac120003_9992937111651741274.jpeg" alt="Project Banner" width="100%">
  <h1>💔 Fiduciary Fallacies</h1>
  <h3><em>A data-driven delving into dalliances and their denouements</em></h3>
  <h4>The Unspoken Code: Decoding the Psychology of Infidelity</h4>
  <p align="center">
    <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white"></a>
    <a href="https://pandas.pydata.org/"><img alt="pandas" src="https://img.shields.io/badge/pandas-Data%20Frames-150458?logo=pandas&logoColor=white"></a>
    <a href="https://numpy.org/"><img alt="NumPy" src="https://img.shields.io/badge/NumPy-Stats-013243?logo=numpy&logoColor=white"></a>
    <a href="https://scikit-learn.org/"><img alt="scikit-learn" src="https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white"></a>
    <a href="#"><img alt="Made by" src="https://img.shields.io/badge/Harshdeep%20Sharma-Analytical%20Mirror-8A2BE2"></a>
  </p>
</div>

> **Scope**: An interdisciplinary analysis of extramarital affairs through historical survey data.

>**Purpose**: Going beyond algorithms to surface the deeper social and psychological factors behind breaches of trust.

>Kaggle Dataset: [Fair's Extramarital Affairs Data](https://www.kaggle.com/datasets/utkarshx27/fairs-extramarital-affairs-data)

---

## Overview

This project is **not** a mere predictive model. It’s a forensic and psychological study of infidelity, a dive into a 1969 survey where each data point is a silent confession.

We move beyond judgement to **understanding** the web of personal, social, and situational factors behind breaches of trust.

---

## Multidisciplinary Perspective
The phenomenon of infidelity is too complex to be understood through a single lens. Our project integrates insights from various disciplines to provide a more holistic view:

* **From Psychology:** We explore the role of **unmet psychological needs**, a concept central to the work of Abraham Maslow. A low self-rated marital satisfaction may not indicate overt conflict but a deep, unfulfilled sense of self or a lack of emotional and intellectual intimacy.
* **From Sociology:** The data's 1969 origin provides a unique historical and sociological context. The sexual revolution was in full swing, and social norms around marriage and monogamy were being challenged. Our findings are therefore a snapshot of a particular socio-historical moment.
* **From Economics:** We frame the decision to have an affair as a **breach of the marital contract**, a "fiduciary fallacy." This perspective views marriage as a trust-based arrangement where each party's actions are governed by an unspoken code of mutual faith.

---

## The Data Speaks: Key Visualizations and Insights
<p align="center"> <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/confusion_matrix.png" width="45%" alt="Confusion Matrix"/>&nbsp; <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/distribution_cat.png" width="45%" alt="Categorical Variable Distribution"/> </p> <p align="center"> <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/distribution_num.png" width="70%" alt="Numerical Variable Distribution"/> </p> <p align="center"> <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/heatmap.png" width="70%" alt="Correlation Heatmap"/> </p> <p align="center"> <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/relevant_features.png" width="45%" alt="Relevant Features"/>&nbsp; <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/roc_curve.png" width="45%" alt="ROC Curve"/> </p> <p align="center"> <img src="https://raw.githubusercontent.com/har5hdeep5harma/FiduciaryFallacies/refs/heads/main/visualizations/performance_comparison.png" width="45%" alt="Performance Metrices"/>&nbsp; </p>

The core of our analysis is a comprehensive exploration of the data, which reveals profound and unexpected insights. Our visualizations are designed not just to show numbers but to tell a story.

**A Philosophical Look at Data Distribution**:
The distribution of variables like `age` and `religiousness` provides a crucial window into the demographics and mindset of the survey respondents. We see that the data is not uniformly distributed, revealing natural skews and imbalances that inform our entire modeling strategy. For example, the distribution of affairs is highly skewed, which is a key signal of an imbalanced classification problem we must handle. 

**The Hidden Threads: The Correlation Heatmap**:
A correlation heatmap is our first step in uncovering the hidden relationships between variables. It reveals the strength and direction of the linear relationships, providing a roadmap for which features are most likely to influence the outcome. Notice the strong inverse correlation between marital `rating` and `affairs`, a direct statistical confirmation of our core psychological hypothesis.

**The Signals of Betrayal - Mutual Information Analysis**:
To understand which features are most relevant to our target variable, we calculate the mutual information score. This metric, which is independent of linear relationships, measures the dependency between variables. It serves as our ultimate guide for feature selection. The chart below reveals that `yearsmarried` is the most powerful predictor, with its engineered interaction features also showing significant relevance. This highlights that the duration of a marriage is a central, driving force in this complex matter. 

---
## Insights and Solutions: From Prediction to Precaution

Our final objective transcends the mere classification of affairs. A cold, black-and-white prediction is insufficient and, frankly, misses the point. The true value of this analysis lies not in a score, but in the **insight** it provides. We aim to construct a model that can identify the **conditions** that correlate with infidelity. The "solution," therefore, is not an algorithmic answer but **a deeper understanding**. Our model is not a fortune teller for relationships; it is an analytical mirror, reflecting the patterns of behavior back to us so that we may learn from them. The final output is not a prediction, but a tool for introspection and, ultimately, a potential guide for healthier, more transparent communication within a partnership.

**Key Insights:**

* **The Power of Time:** Our analysis confirms that the duration of a marriage (`yearsmarried`) and its non-linear interactions with other features are the single most influential predictors of infidelity. This suggests that the slow, subtle erosion of novelty and fulfillment over time may be a primary driver.
* **Unhappiness as a Predictor:** The inverse correlation between marital `rating` and affairs is a powerful insight. It suggests that infidelity is not a random act but a symptom of underlying marital dissatisfaction.
* **The Need for Interpretability:** By identifying the most influential features, our models provide a tangible starting point for a deeper conversation about what makes relationships vulnerable. They offer a data-backed foundation for relationship counseling and personal reflection.

**Practical Solutions:**

* **Data-Driven Conversations:** The insights from this project could be used in a therapeutic context to help couples understand the objective risk factors within their relationship and to guide conversations about underlying dissatisfaction.
* **Preventative Counseling:** This analysis can inform preventative measures by highlighting key inflection points in a relationship's lifecycle (e.g., specific years of marriage) where couples may be more vulnerable to issues.
* **A Call for Deeper Data:** The project's most important "solution" is a call for richer, more comprehensive datasets on human behavior. The limitations of a 1969 survey underscore the need for more nuanced, longitudinal studies to truly understand the complexities of modern relationships.


---

## Metrics of Trust  

**Best Models:** Support Vector Machine & Random Forest  
**AUC:** > 0.84  
**Outcome:** Not a “fortune teller” but an analytical mirror for introspection and healthier communication.  

---

## Project Structure  

```bash
FiduciaryFallacies/
├── .gitignore
├── data/
│   └── Affairs.csv
├── src/
│   └── utils.py
├── visualizations/
├── affair.ipynb
└── config.yaml
├── README.md
└── requirements.txt
```

---

## Quickstart  

```bash
git clone https://github.com/har5hdeep5harma/FiduciaryFallacies  
cd FiduciaryFallacies 
pip install -r requirements.txt  
jupyter notebook affair.ipynb  
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center"> <sub>Made with 💡 and curiosity by <b>Harshdeep Sharma</b>. If you find this repository insightful, please ⭐ it to support the project.</sub> </p> 