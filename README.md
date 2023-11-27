<h1>NHS - Appointments in General Practice</h1>
  <h3> Topics Covered</h3>
  <p>
    Data Wrangling, Data Visualisation with Python (Plotlt, MatPlotLib, Seaborn), API calling, Web Scraping, Natural Language Processing, and Sentiment Analysis. 
 </p>

Grade: __86% (Distinction)__

<h2>Assignment Overview</h2> 
  <p>
The goal of this project was to explore NHS appointment data within primary care and determine what can be done to reduce and eliminate missed appointments by investigating two main areas of capacity and resource utilisation in the NHS.

Four datasets were used in this analysis and can be found in the repository. The first three datasets contain primary care appointment data in the NHS and the last dataset is health-related tweets scraped from Twitter.  

![Image](Figures/AA2_Datasets.png)
  </p>
  
<h2>Findings and Recommendations - Final Stakeholder Presentation</h2> 

<p align="center">
  <img src="Figures/Slide1.jpeg" alt="Image Description" width="720" height="405">
</p>

Welcome to this presentation on NHS Appointments in General Practice. 

![Image](Figures/Slide2.jpeg)

It is estimated that each missed appointment costs the NHS an average of £30 per person, which may not seem like a lot but adds up to over £290 million wasted in just half a year from people not attending their appointments. Additionally, it is estimated that in the second half of 2022, approximately 5% of all appointments were missed, highlighting a critical area for improvement in healthcare management.

![Image](Figures/Slide3.jpeg)

Our analysis aims to address the pressing issue of missed NHS appointments by exploring two key areas: the adequacy of staff and network capacity, and the actual utilisation of resources. This exploration is particularly relevant to NHS ICBs, who are directly impacted by these challenges. 

![Image](Figures/Slide4.jpeg)

Utilising three NHS-provided datasets on appointment data and a collection of healthcare-related tweets, we employed Python for its versatility in data processing and visualization. Collaboration was enhanced through the use of GitHub, a web-based platform that provides version control and collaborative features, ensuring efficient management and tracking of project developments

![Image](Figures/Slide5.jpeg)

The approach taken is highlighted here where the data was first imported and sense checked for duplicates and outliers to begin the initial stages of data exploration. 

The imported data was then analysed to try and find answers related to the business problem and gauge capacity and resource utilisation. Visualisations were then created to show trends in the data. Finally, any relevant findings and future recommendations are discussed. 

![Image](Figures/Slide6.jpeg)

To first get a better idea of the data, the different categories that were explored are highlighted here showing the corresponding number of values within each category. For example, there were a total of 5 service settings consisting of GP, Primary care network, other, unmapped and extended access provision. 3 context types, 18 total national categories and 3 appointment statuses. We also found that the data provided encompasses a total of 106 sub-ICB locations, providing a clearer understanding of the data landscape within the NHS.

![Image](Figures/Slide7.jpeg)

As we are investigating changes over time, almost all the data was grouped by month. Here are example data tables between August 2021 and June 2022 showing the number of appointments per month in descending order and the number of records per month in chronological order. The Average number of appointments per month recorded was found to be around 27 million while the average number of records a month at approximately 75 thousand. This data was crucial in assessing the monthly capacity and utilisation of NHS appointments.

![Image](Figures/Slide8.jpeg)

Moving onto our exploration of Twitter data, we were originally hoping that by identifying the top trending hashtags or identifying tweets that contained words such as “wait”, “missed” or  “Appointment” we would be able to attain greater context and insights into first-person accounts related to appointments. However, this was not the case as seen by the table on the left containing tweets with the word "wait" which provide no relevant insights into the problem. Instead, a sentiment analysis was conducted which provides a sentiment score between -1 (being negative) and 1 (being positive) for each tweet. This yielded an overall sentiment score of 0.25 indicating only a slightly positive public sentiment towards NHS services. 

![Image](Figures/Slide9.jpeg)

When analyzing data over time, a bias towards higher values in each category was observed, highlighted in the table showing the proportion of values in each category. This is to be expected as the NHS primarily delivers care through General Practice appointments and direct patient care, providing a clearer picture of service delivery patterns.

![Image](Figures/Slide10.jpeg)

This does mean that when investigating the different categories over time that the findings will be heavily affected by the count of the number of appointments for example here we can see the number of appointments per month for the time period between August 2021 and June 2022. 


![Image](Figures/Slide11.jpeg)

And here is the number of appointments for each service settings over the same time period. 


![Image](Figures/Slide12.jpeg)

And then for Context Type. All of the highest values of each category follow a similar trend to the number of appointments where it increases from August onwards towards the end of the year and decreases after the new year and begins to platue out for the remaining months. 

To mitigate this bias in the data, in some of the following figures, the change in the proportion of values is shown instead. 



![Image](Figures/Slide13.jpeg)

When looking at the number of appointments for the full time period with the 5 busiest month shown in red. The large drop in the beginning of 2020 is due to the COVID pandemic. From march onwards there is ar apid increase in the number of appointments and in line with the first lockdown that begin in late March 2020, where the increase in appointments is most likely covid related.


It also becomes much more evident here that there is a general increase in the number of appointments building up towards the end of the year due to winter bugs, health conditions worsening with the cold, increased rates of flu, and more people attending to their health before the Christmas and New Years holiday. 



![Image](Figures/Slide14.jpeg)

If we look at the number of appointments per season, we can also see that there is a weekly cycle in the appointment numbers, where it peaks on Mondays and gradually declines towards Friday with few appointments taking place on sat and even less on Sunday but not 0. Plotting the seasonal variations also shows when the national holidays are as these days there is also a very low number of appointments taking place. 



![Image](Figures/Slide15.jpeg)

we now dive deeper into changes relating to the number of appointments per month to get a better idea of capacity and utilisation of NHS appointments for different categories.

The average monthly utilisation (as a % of maximum) was calculated based on the stat provided that maximum number of appointments the NHS can handle a day is 1.2 million., This is when divided by 30 days month to determine daily utilisation capacity, we can see that in the final months of the year the capacity does reach quite a high level of around 80%. 

However, this figure does not considerer the fact that on Saturdays and Sunday there are very few appointments that actually even take place.


![Image](Figures/Slide16.jpeg)

If we were to determine the capacity with a lower number of days say 24 days, from 6 days a week. There are many recent months when the NHS has gone over capacity for the number of appointments. 



![Image](Figures/Slide17.jpeg)

Changes in attendance follow a similar trend to the total number of appointments, with attendance increasing following Covid. There is also a trend seen in a decrease in the proportion of appointments attended from July to October each year which could be explained by people not attending as a result of summer holiday plans and missed appointments after the clocks move forward in spring for daylight saving.  

It would therefor be recommended that more reminders are sent out to during these months


![Image](Figures/Slide18.jpeg)

The stacked bar chart above shows the proportion of appointment modes over time. It indicates that before the pandemic face-to-face appointment generally accounted for 80% which then dropped to 50% until July. Although they have gradually increased since, it’s unlikely to return to pre-pandemic values due to the adoption of more telehealth and digital health options.


![Image](Figures/Slide19.jpeg)

in terms of appointment mode, the figure indicates the highest share of attended appointments are telephone appointments by far with an attendance rate of 95%, followed by video/ online. It therefor would be advisable to utilise these appointment modes wherever possible, which I believe the NHS is already doing urging patients to come forward through NHS 111 hotline and NHS 111 online. 



![Image](Figures/Slide20.jpeg)

Interestingly, when looking at the share of Did not attend appointments, face-to-face had the highest share of missed appointments which seems to be increasing over time, This further highlights the need to utilise telehealth and digital health options where possible. 


![Image](Figures/Slide21.jpeg)

Trends in time between booking an appointment show a slight increase in the number of same day appointments, and a recent decrease in  2 – 7 days and 8 to 14 days from October 2021 onwards showing some success in the NHS’s attempt to cut non-urgent care wait times. 

![Image](Figures/Slide22.jpeg)

After the initial drop of appointments at the start of Covid, an increase in proportion of same day appointments is seen by around 20% which returned to pre pandemic level relatively quickly from 2020-04 to 2020-10. In the more recent months, the longer wait times of 22 – 28 days and 28+ days have been increasing. 

This is in line with what the NHS has been reporting that they have been able to improve the number same day appointments, but medium to long wait times have gotten worse as a result of chronic understaffing and a huge backlog from the Covid Pandemic. 

![Image](Figures/Slide23.jpeg)

It is already well know the the NHS is severely understaffed, with capacity rates already pushing above 80% on some months, and over 100% when accounting for the low appointment numbers on weekends, it is essential that more staff are required. Recent data suggests that the NHS is already at if not over capacity delivering 14million appointments  in general practice in June of this year. 

More reminders sent out before and during the months with the lowest attendance

Also have Greater adoption of telehealth and other digital health options where possible, especially because its shown to have the highest attendance 

In terms of recommendations for future analysis, there needs to be data gathered to properly and more accurately calculate capacity and resource utilization such as number of GPs and patients and the proportion of available appointments that are actually used. Measurements for demand are also needed such as the volume of people attempting to book appointments. 

Variation in database management between the different sub ICBs need to be reduced through synchronous guidelines that are already in place. 

Finally, To better understand reasons for missed appointments, new measurements categories like reason for missed appointment or whether a mail, text, telephone reminder was given could be implemented into sub ICB data management systems.  




## The working order of how this project was approached is shown below and corresponds to chapters seen in the Jupyter Notebook
1. Setting Up the GitHub Repository
2. Importing and Exploring Data
3. Analysing the Data: Initial Exploration
4. Sentiment Analysis: NHS-related Twitter Data
5. Visualising and Identifying Initial Trends
6. Findings and Recommendations

