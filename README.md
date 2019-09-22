# match_blood_donor

Problem Statement:

Blood crisis has been a serious issue in the United States. Recently, American Red Cross a humanitarian organization that provides emergency assistance, disaster relief, and disaster preparedness education in the United States issued an emergency call to address a shortage of blood across the country. The organization, which generally keeps a five day supply of all blood types on hand, had less than a three-day supply of types A and B blood and less than a two-day supply of type O. 

Given the short shelf life of blood (~40 days) and the storage conditions required to keep it intact (~40F), it becomes a difficult task to manage blood samples even if there is an increase in the amount of donors. 

Solution:

    In order to address this issue, we built an application that would make it easier for hospitals or blood banks to locate potential donors at times of emergency. 
  
Methodology:
  1. Based on the historical data of donors, we implemented a classifcation model using Gradient Boosting to identify people who are likely to donate blood in the immediate future
  2. Implemented an E2E application with interactive geographical maps that allows the stakeholders to look for donors in the vicinity based on the requirements such as blood group, immediacy, etc.
  3. Provide contact information of potential donors to the stakeholders

Technologies used:
  1. Front-end:
        ESRI ArcGIS
  2. Back-end:
        Django, SQLite, AWS EC2
  3. Data Science:
        NumPy, Pandas, Scikit-learn
    
