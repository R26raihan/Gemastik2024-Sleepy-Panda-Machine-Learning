

Gemastik 2024 🌟
Gemastik (Gema Teknologi Informasi) is a prestigious competition held in Indonesia, aimed at encouraging innovation and technological development among students. This competition covers various categories, including software development, artificial intelligence, and information technology. Gemastik serves as a platform for participants to showcase their creativity and skills in creating impactful solutions for society. 🏆💻

Sleepy Panda 🐼💤
Sleepy Panda is a sleep monitoring application designed to help users understand their sleep patterns and detect sleep disorders. This application utilizes the XGBoost model to analyze sleep data and provide predictions regarding the likelihood of sleep disturbances such as sleep apnea, insomnia, and normal sleep patterns. 🌙🔍

With a user-friendly interface, Sleepy Panda offers easy-to-understand insights into users' sleep quality. The app aims to raise awareness about sleep health and provide recommendations that can help users improve their sleep quality. Through accurate analysis and data-driven predictions, Sleepy Panda strives to be an effective solution for addressing common sleep issues. 🌟🛌

![output](https://github.com/user-attachments/assets/3829f587-ad81-4f62-af0e-b9130ab31c9f)

🌟 Confusion Matrix Analysis 🌟
Confusion matrices are essential tools for evaluating the performance of classification models. They provide a visual representation of the true positive, false positive, true negative, and false negative classifications made by the models. Below, we analyze the confusion matrices for five different algorithms used to predict sleep disorders: Logistic Regression, XGBoost, Gradient Boosting, Random Forest, and AdaBoost.

1. Logistic Regression 🤔
True Positives (TP) for Sleep Apnea: 61 ✅
True Negatives (TN) for None: 51 ✅
False Positives (FP) for None: 6 ❌
False Negatives (FN) for Sleep Apnea: 3 ❌
Insomnia Cases: 5 correctly predicted as Insomnia. 💤
Logistic Regression shows reasonable performance, but some cases of sleep apnea are missed, indicating a need for improvement! 📉

2. XGBoost 🚀
TP for Sleep Apnea: 60 ✅
TN for None: 52 ✅
FP for None: 4 ❌
FN for Sleep Apnea: 3 ❌
Insomnia Cases: 4 correctly predicted as Insomnia. 💤
XGBoost performs admirably, maintaining a low false positive rate and high true positive rate. Well done! 🎉

3. Gradient Boosting 🌈
TP for Sleep Apnea: 59 ✅
TN for None: 52 ✅
FP for None: 4 ❌
FN for Sleep Apnea: 4 ❌
Insomnia Cases: 2 correctly predicted as Insomnia. 💤
Gradient Boosting is strong but has slightly more false negatives compared to XGBoost. A little more refinement could enhance its performance! 🔍

4. Random Forest 🌳
TP for Sleep Apnea: 60 ✅
TN for None: 52 ✅
FP for None: 4 ❌
FN for Sleep Apnea: 3 ❌
Insomnia Cases: 2 correctly predicted as Insomnia. 💤
Random Forest matches XGBoost’s performance, showing excellent balance between true positives and false negatives. Great job! 👍

5. AdaBoost 🥺
TP for Sleep Apnea: 60 ✅
TN for None: 28 ❌
FP for None: 26 ❌
FN for Sleep Apnea: 3 ❌
Insomnia Cases: 4 correctly predicted as Insomnia. 💤
AdaBoost is lagging behind the others, with a high false positive rate. It definitely needs some extra tuning and optimization! 🔧

🚀 Summary 🚀
Overall Best Performers: XGBoost, Random Forest, and Logistic Regression show strong predictive capabilities for Sleep Apnea, with low false positive rates and high true positive rates. 🎯
Area for Improvement: AdaBoost requires further validation and tuning, as it underperforms compared to other models. 🚧
Recommendation: Let’s refine the top-performing models and explore hyperparameter tuning to enhance predictive power, especially in detecting sleep apnea and insomnia. 🔍💡




