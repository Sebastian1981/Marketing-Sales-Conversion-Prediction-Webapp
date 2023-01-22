# Marketing Engagement Prediction Model to Maximize ROI: Implementation of an End-to-End Machine Learning Solution 

<br><br>
## **Motivation:**  
Marketing conversion prediction adds tremendous value to any marketing campaign. By leveraging data and predictive analytics, marketers are able to anticipate and measure the likelihood of a customer or user completing a desired action. This gives marketers the opportunity to strategically target the most valuable customers and maximize their ROI. 

<br><br>
## **Data Source:**  
This demo project is based on the publicly available dataset from the UCI machine learning repository: 
https://archive.ics.uci.edu/ml/datasets/bank+marketing

<br><br>
## **Project Goal:**  
The goal of this project is to  
1. identify the key drivers to marketing engagement, 
2. evaluate engagement prediction model,
3. implement web app using streamlit
3. transform web app into highly efficient software using Docker
4. deployed model in streamlit cloud: [streamlit cloud](https://sebastian1981-marketing-sales-conversion-pre-web-appmain-y81hcx.streamlit.app/)
 
<br><br>
## **Solution Approach:**  
The project is developed according to the well-known CRISP-DM
[CRISP-DM Model](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining).

<img src="images/crisp_dm.png" 
width="400" 
style="object-fit: contain;">

- "Business Understanding", "Data Understanding", "Data Preparation", "Modeling" & "Evaluation": see Jupyter Notebook "/experiment/01_bank_customer_conversion_prediction_poc.ipynb". 
- "Deployment": see Jupyter Notebook "/experiment/02_bank_customer_conversion_prediction_scoring_pipeline.ipynb" and "/web_app". 

<br><br>
## **Tools:**  
vscode, python, jupyter, pandas, numpy, sklearn, shap, docker, streamlit

<br><br>
## **Solution Steps:**
1. undestanding and exploring the historical dataset of marketing campaigns using different data visualisation techniques using jupyter notebook
2. preparing the data for statistical modeling using jupyter notebook
3. training and tuning the best machine learning model using jupyter notebook
4. extract the diving features of marketing conversion exploiting novel methods of explainable artificial intelligence using jupyter notebook
5. implementing a web app to predict individual conversion probabilities using streamlit 
6. deployment of the web app using docker and streamlit cloud 

<br><br>
## **Key Findings - Average Engagement Rate:**

<img src="images/engagement_rate.jpg" 
width="600" 
style="object-fit: contain;">

The average engagement rate among all customers is 12%. Hence, not leveraging the power of AI to focus targeting only the customers with the highest conversion rate is very ineffective.

<br><br>
## **Key Findings - Drivers to Marketing Engagement:**

<p style="text-align:center;"><strong>Distribution Plots for Age</strong></p>
<img src="images/age_dist.jpg" 
width="800" 
style="object-fit: contain;">


Apparently there is a clear age effect on the engagement rate. The age groups around 20 years and between 60-70 years are more likely to engage than the mid-agers.

<p style="text-align:center;"><strong>Distribution Plots for Month</strong></p>
<img src="images/month_dist.jpg" 
width="800" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Pie-Plots of the monthly-distributions for the Non-Converters (left) and the Converters (right).</strong></p>

There is a clear seasonal effect on engagement rate. E.g. in the non-converters group, the largest proportion of customers is found in the month of May whereas in the converters group the proportion of customers in May is clearly smaller. Therefore, the month of May seems to have an unfavorable effect on the success of a marketing campaign.

<p style="text-align:center;"><strong>Decision Tree Analysis</strong></p>
<img src="images/decision_tree_analysis.png" 
width="800" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Prescriptive Analytics using a Simple Decision Tree.</strong></p>

The simple decision tree analysis shows that features "p_outcome", "contact" and "age" are among the key engagement drivers. The "p_outcome" variable represents whether the last marketing campaign was successful with a particular customer or not. The "contact" and "age" variables represent the type of contact and the customer ́s age, respectively. If we take a closer look at the decision tree, we can see, for example, that the conversion rate is 91% if the last marketing campaign was successful (“p_outcome_successfull”) and the customer is in the younger age group (“age<17.5”). In comparison, the global conversion rate is only 12%. Hence, focusing on this young-age group would already lift the conversion rate by a factor of more than 7. The decision tree analysis remarkably shows the value this data-based analysis can add for optimizing marketing campaigns. However, we would like a more comprehensive insight into the key drivers and their effect on engagement rates. Therefore, we applied a state-of-the-art explainable artificial intelligence approach to gain complete insight to what drives marketing success.

<p style="text-align:center;"><strong>Shap Bar Plot</strong></p>
<img src="images/shap_values_bar.jpg" 
width="800" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Key marketing engagement drivers detected by applying high performance complex machine 
learning models in combination with state-of-the-art explainable artificial intelligence methods.</strong></p>

The bar-plot of the shap-values show that the top-5 key drivers to marketing engagement are the features “contact_telephone”, “month_may”, “default_unkknown”, “age” and “poutcome_success”. The x-axis shows the likelihood of conversion affected by each feature. E.g. the features “contact_telephone” and “age” affect the likelihood of conversion on average by approx. 28% and 11%, respectively.

<p style="text-align:center;"><strong>Shap Violin Plot</strong></p>
<img src="images/shap_values_violin.jpg" 
width="800" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Key drivers and their explicit effect on the likelihood on engagement for each customer.</strong></p>

The shap value violine plot yields a deeper insight into the key drivers to engagement and their explicit affects on the likelihood on the conversion rate. Thereby each datapoint represents one customer. The impressive feature of this state-of-the-art explainable artificial intelligence approach is that the engagement probabilities can simply be linearly added up. E.g. contacting the customers not via telephone leads to a conversion probability of around 18% on 
average (center of blue distribution). The conversion probability is further increased by around 15% if the customer are not contacted in the month of May. Focusing on the customers with a known credit-default history increases the probability of engagement by further 10% approx. Hence, targeting this group, we end up with a net engagement probability of approx. 43%, which is significantly higher than the global conversion rate of 12%. Note that based on that powerful state-of-the-art explainable artificial intelligence approach, you can simply estimate the effective engagement probability for any target group! 

<p style="text-align:center;"><strong>Shape Dependence Plot for Age</strong></p>
<img src="images/shap_dependence_plot_age.jpg" 
width="800" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Age Effect on Engagement Probability.</strong></p>

The figure above explicitly shows how the customers age relates to engagement probability.

<br><br>
## **Key Findings - Engagement Prediction Model Evaluation:**

<p style="text-align:center;"><strong>Conusion Matrix on Test Data</strong></p>
<img src="images/confusion_matrix_gb.jpg" 
width="400" 
style="object-fit: contain;">

The confusion matrix shows the model performance in the form of the confusion matrix of the test dataset (i.e. data the model has not seen during training). It shows that the recall and the precision of the ml-model are both around 40%. But what does the accuracy of the model translate into increasing the effectiveness of the marketing campaign based on the ml-model?

<p style="text-align:center;"><strong>CAP and Lift Curve on Test Data</strong></p>
<img src="images/cap_lift_curves_gb.jpg" 
width="800" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Cumulative gain curve (left) and lift curve (right).</strong></p>

The cumulative gain and the lift curves show that contacting only the top 20% of the customers with the highest conversion probabilities predicted by the model yields around 50% engagement. This corresponds to a lift of around 2.5 compared to randomly picking customers i.e. not using any predictive model.

<br><br>
## **Model Deployment**
Based on the marketing engagement prediction model a web app was developed and deployed on [Docker-Hub](https://hub.docker.com/r/63531981/conversion_prediction_app) and in the [Streamlit-Cloud](https://sebastian1981-marketing-sales-conversion-pre-web-appmain-y81hcx.streamlit.app/)

<br><br>
<img src="images/streamlit_app.jpg" 
width="400" 
style="object-fit: contain;">
<p style="text-align:center;"><strong>Screenshot of the Marketing Engagement Prediction App.</strong></p>