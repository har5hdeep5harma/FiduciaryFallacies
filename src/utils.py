import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score

def plot_feature_distribution(df, column, title):
    """
    Generates a histogram to visualize the distribution of a numerical feature.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to plot.
        title (str): The title for the plot.
    """
    plt.figure(figsize=(8, 6))
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

def plot_confusion_matrix(y_true, y_pred, labels, title):
    """
    Plots a confusion matrix using a heatmap for better visualization.

    Args:
        y_true (list or np.array): The true labels.
        y_pred (list or np.array): The predicted labels.
        labels (list): A list of class labels.
        title (str): The title for the plot.
    """
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.title(title)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

def plot_roc_curve(y_true, y_pred_proba, model_name):
    """
    Plots a Receiver Operating Characteristic (ROC) curve.

    Args:
        y_true (list or np.array): The true labels.
        y_pred_proba (list or np.array): The predicted probabilities for the positive class.
        model_name (str): The name of the model for the legend.
    """
    fpr, tpr, _ = roc_curve(y_true, y_pred_proba)
    auc_score = roc_auc_score(y_true, y_pred_proba)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {auc_score:.4f})')
    plt.plot([0, 1], [0, 1], 'k--', label='Random Guessing')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'ROC Curve for {model_name}')
    plt.legend()
    plt.grid(True)
    plt.show()