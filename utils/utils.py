import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


def plot_countplot(dados, x, titulo, label_x: str, figsize: tuple = (8, 5), hue=None, small: bool = False):
    plt.figure(figsize=figsize)
    custom_params = {"axes.spines.right": False, "axes.spines.top": False,
                     "axes.spines.left": False, "axes.spines.bottom": False}

    sns.set_theme(style="ticks", rc=custom_params)
    ax = sns.countplot(x=x, hue=hue, data=dados, palette='viridis')

    ax.get_yaxis().set_visible(False)

    plt.title(titulo, fontsize=22, loc='left')
    plt.xlabel(label_x, fontsize=17)
    plt.xticks(fontsize=15)

    for container in ax.containers:
        if small:
            ax.bar_label(container, fontsize=15)
        else:
            ax.bar_label(container, fontsize=15, padding=-17, color='white')

    plt.show()


def heatmap_corr(df, figsize: tuple = (8, 6)):
    corr = df.corr()
    plt.figure(figsize=figsize)
    sns.heatmap(corr,
                xticklabels=corr.columns.values,
                yticklabels=corr.columns.values,
                annot=True,
                cmap='viridis')


def plot_matriz_confusao(y_true_teste, y_pred_teste, group_names=None,
                         categories='auto', count=True, cbar=True,
                         xyticks=True, sum_stats=True, figsize=None,
                         cmap='viridis', title=None):

    cf = confusion_matrix(y_true_teste, y_pred_teste)

    blanks = ['' for i in range(cf.size)]

    if group_names and len(group_names) == cf.size:
        group_labels = ["{}\n".format(value) for value in group_names]
    else:
        group_labels = blanks

    if count:
        group_counts = ["{0:0.0f}\n".format(value) for value in cf.flatten()]
    else:
        group_counts = blanks

    box_labels = [f"{v1}{v2}".strip()
                  for v1, v2 in zip(group_labels, group_counts)]
    box_labels = np.asarray(box_labels).reshape(cf.shape[0], cf.shape[1])

    if sum_stats:

        accuracy = accuracy_score(y_true_teste, y_pred_teste)
        precision = precision_score(y_true_teste, y_pred_teste)
        recall = recall_score(y_true_teste, y_pred_teste)
        f1_score_metric = f1_score(y_true_teste, y_pred_teste)

        stats_text = "\n\nAcurácia={:0.3f}\nPrecisão={:0.3f}\nRecall={:0.3f}\nF1 Score={:0.3f}".format(
            accuracy, precision, recall, f1_score_metric)
    else:
        stats_text = ""

    if figsize == None:
        figsize = plt.rcParams.get('figure.figsize')

    if xyticks == False:
        categories = False

    plt.figure(figsize=figsize)
    sns.set(font_scale=1.4)  # for label size
    sns.heatmap(cf, annot=box_labels, fmt="", cmap=cmap, cbar=cbar,
                xticklabels=categories, yticklabels=categories)
    plt.ylabel('Valores verdadeiros', fontsize=16)
    plt.xlabel('Valores preditos' + stats_text, fontsize=16)

    if title:
        plt.title(title, fontsize=20)


def compara_modelos_metricas(metrica, nomes_modelos, y_true_treino, y_pred_treinos, y_true_teste, y_pred_testes):
    """

    metrica: {'Acurácia Treino', 'Acurácia Teste', 'Precisão', 'Recall', 'F1-Score'}

    Returns:
        DataFrame ordenado de acordo com a métrica passada. 
    """

    acc = []
    precision = []
    recall = []
    f1 = []

    for y_pred_teste in y_pred_testes:
        acc.append(accuracy_score(y_true_teste, y_pred_teste))
        precision.append(precision_score(y_true_teste, y_pred_teste))
        recall.append(recall_score(y_true_teste, y_pred_teste))
        f1.append(f1_score(y_true_teste, y_pred_teste))

    acc_treino = []
    for y_pred_treino in y_pred_treinos:
        acc_treino.append(accuracy_score(y_true_treino, y_pred_treino))

    tabela = pd.DataFrame({'Modelo': nomes_modelos,  'Acurácia Treino': acc_treino,
                          'Acurácia Teste': acc, 'Precisão': precision, 'Recall': recall, 'F1-Score': f1})

    return tabela.sort_values(by=metrica, ascending=False).reset_index(drop=True)
