import math
import numpy as np

def naive_bayes_yn(index, figures, feat_df, class_df):
    """
    Calculate P(class | features) = P(features | class) * P(class) / P(features)
    """
    row = feat_df.iloc[index]
    test_stats = []
    for f in figures:
        test_stats.append(row[f])
    probability = class_df.shape[0] / feat_df.shape[0]
    for i in range(len(test_stats)):
        stat = test_stats[i]
        stats = list(class_df[figures[i]])
        count = stats.count(stat) + 1
        probability *= (count / len(stats))
    return probability

def naive_classes(index, figures, feat_df, classes, class_dfs):
    """
    Calculate P(class | features) = P(features | class) * P(class) / P(features)
    for multiple related classes and return the class that yielded the highest
    P(class | features)
    """
    row = feat_df.iloc[index]
    test_stats = []
    for f in figures:
        test_stats.append(row[f])
    probabilities = []
    for j in range(len(classes)):
        current = class_dfs[j]
        probability = current.shape[0] / feat_df.shape[0]
        for i in range(len(test_stats)):
            stat = test_stats[i]
            current_stats = list(current[figures[i]])
            count = current_stats.count(stat) + 1
            probability *= (count / len(current_stats))
        probabilities.append(probability)
    p_max = max(probabilities)
    return classes[probabilities.index(p_max)]

def normpdf(index, figures, feat_df, class_df):
    """
    Calculate the probability density of a value for a given class
    """
    row = feat_df.iloc[index]
    test_stats = []
    for f in figures:
        test_stats.append(row[f])
    positions = list(class_df[figures[0]])
    probability = ((positions.count(test_stats[0]) + 1) / len(positions))
    for i in range(1, len(test_stats)):
        stat = test_stats[i]
        stats = list(class_df[figures[i]])
        mean = np.mean(stats)
        std = np.std(stats)
        var = float(std)**2
        denom = (2*math.pi*var)**.5
        num = math.exp(-(float(stat)-float(mean))**2/(2*var))
        probability *= num/denom
    return probability

def normpdf_multiple_classes(index, figures, feat_df, classes, class_dfs):
    """
    Calculate the probability densities of a value for given classes and return
    the class that yielded the highest probability
    """
    row = feat_df.iloc[index]
    test_stats = []
    for f in figures:
        test_stats.append(row[f])
    probabilities = []
    for j in range(len(classes)):
        probability = 1
        current = class_dfs[j]
        for i in range(1, len(test_stats)):
            stat = test_stats[i]
            current_stats = list(current[figures[i]])
            mean = np.mean(current_stats)
            std = np.std(current_stats)
            var = float(std)**2
            denom = (2*math.pi*var)**.5
            num = math.exp(-(float(stat)-float(mean))**2/(2*var))
            probability *= num/denom
        probabilities.append(probability)
    p_max = max(probabilities)
    return classes[probabilities.index(p_max)]

def correct(col, df):
    """
    Return the proportion of correct classifications to total classifications
    """
    correct_counter = 0
    for i in range(df.shape[0]):
        row = df.iloc[i]
        pred_col = col + ' Prediction'
        pred = list(row[pred_col])[0]
        correct = list(row[col])[0]
        if pred == correct:
            correct_counter += 1
    return correct_counter / df.shape[0]

