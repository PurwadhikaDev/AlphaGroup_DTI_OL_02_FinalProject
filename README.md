# Breaking Bottlenecks: Delivery Gameplan for Olist

Courtesy of **Team Alpha (DTIDSOL-02)**  
- Josephine Rahma Gunawan  
- Rio Pramana  
- Risma Widiya Puspadevi

## About Olist

[Olist](https://pt.wikipedia.org/wiki/Olist) is a Brazilian e-commerce technology startup founded in February 2015 in Curitiba by Tiago Dalvi. It spun off from his earlier marketplace venture, Solidarium (est. 2007).  

Olist is not a traditional marketplace, it operates as a **commerce enabler**. Small and medium-sized retailers upload their product catalogs to Olist, which manages the listings across major marketplaces (Amazon, Mercado Livre, B2W), handles logistics, and provides financial services.

By 2018, Olist was:
- Backed by **Series B venture capital**, including **SoftBank Vision Fund**, Redpoint e.ventures, and 500 Startups  
- Supporting **12,000+ merchants** and connecting them to **13 marketplaces**  
- Expanding its scope beyond marketplace integration into **logistics and merchant capital** services  

In short, **2018 Olist was a growth-stage, VC-backed startup** prioritizing scale and customer retention, making it reasonable to optimize for **long-term satisfaction over short-term operational cost**.

**Sources**:  
- [Wikipedia: Olist](https://pt.wikipedia.org/wiki/Olist)  
- [Digitopia – Digital Change in Brazil](https://digitopia.co/blog/digital-change-for-brazilians/)  
- [CanvasBusinessModel – Brief History of Olist](https://canvasbusinessmodel.com/blogs/brief-history/olist-brief-history)

## **Data Analysis**

**Understanding the Business Problems**

### Background and Business Objective

E-commerce has rapidly transformed how people shop, especially in Brazil, where convenience, price, and speed play crucial roles in consumer decisions. According to a report by **NielsenIQ**, Brazilian shoppers cited the following top reasons for choosing online platforms:

- **77%** – Best price  
- **57%** – Delivery time  
- **54%** – Product variety  
- **39%** – Special promotions (e.g., free shipping, discounts, loyalty programmes)

The fact that *delivery time* ranks second highlights just how important a fast, reliable shipping experience is to customers (nearly as important as pricing itself).

For **Olist**, a startup in 2018 still in its aggressive growth phase after securing **Series B funding** (with backing from SoftBank, Redpoint e.ventures, and 500 Startups), this is a critical threat. At that point, Olist had:

- A low **customer retention rate** of just **3%**
- A rising **late delivery rate** that exceeded the commonly accepted benchmark of 5%
- A high volume of **negative reviews** directly tied to lateness

This meant that every failed delivery was a **lost growth opportunity** and **damage to long-term customer value**. As a startup prioritizing **scale and customer experience over short-term cost**, Olist needed a solution to protect its reputation and maximize retention, even if the underlying logistics couldn’t be fully fixed.

#### Why Focus on On-Time Delivery (OTD)?

To evaluate delivery performance, we focus on the industry-standard metric: **On-Time Delivery (OTD)**. OTD measures the percentage of orders delivered within the promised timeframe and is calculated as:

> **OTD (%) = (Number of on-time deliveries / Total deliveries in the period) × 100**

As highlighted in a blog by **[Delage](https://delage.com.br/blog/otd-on-time-delivery-saiba-tudo-sobre-um-dos-principais-indicadores-para-o-e-commerce/)**, OTD has become one of the most relevant indicators in e-commerce logistics today. It reflects the efficiency of the entire order fulfilment process from the time an order is picked and packed to when it’s handed off by the courier.

Importantly, a survey by **Reclame Aqui** showed that **18.6% of consumers abandon their online shopping carts** if the estimated delivery time doesn’t meet their expectations. While this figure may seem modest at first glance, nearly **1 in 5 lost sales** can severely impact an e-commerce company’s bottom line, especially at scale.

Furthermore, an article by **[Gazeta do Povo](https://www.gazetadopovo.com.br/economia/e-commerce-brasileiro-busca-alternativas-a-correiodependencia-an1xq7tj25k1nnxytsml2tb4q/)** noted that logistics companies proudly advertise achieving **95% OTD** as a sign of operational excellence. While not a formal industry standard, this 95% mark is widely regarded as a benchmark for competitive performance in Brazil’s e-commerce landscape.

E-commerce giants typically operate at **95% On-Time Delivery Rate (OTDR)**. In contrast, Olist’s OTDR dropped to as low as nearly **80% in 2018**, especially in high-volume periods. At this level:

- **7.92% of orders are late**
- **Late deliveries are 3x more likely to receive a 1-star review**
- **18% of customers are less likely to reorder after a late experience**

### Project Objective

Given the critical role that delivery time plays in consumer satisfaction and conversion rates, the objective of this project is to:

> **Improve Olist's delivery performance by increasing its On-Time Delivery (OTD) rate, aiming for a minimum benchmark of 95%.**

In addition to descriptive and diagnostic analysis, this project also leverages **machine learning to predict whether a delivery will be late or on time** based on various features available at the time of order. The goal is to take **preventive action** on high-risk deliveries such as prioritising processing or flagging for courier follow-up before issues occur.

> **The Machine Learning solution aims to improve Olist's delivery performance by predicting which orders are at risk of being delivered late, allowing the company to take proactive action to reduce dissatisfaction, negative reviews, and churn.**

Rather than attempting to fix the physical delivery system (which Olist might not fully control), the solution focuses on **early detection and mitigation**, such as notifying customers, recalibrating expectations, and offering small compensations where appropriate.

The model’s business value lies in **turning a potentially negative experience into a neutral or even positive one**, without waiting for the damage to happen.

So, through data-driven insights and predictive modelling, this project aims to help Olist optimise its logistics performance, meet customer expectations, and improve overall business outcomes.

### Summary of Exploratory Data Analysis 
The EDA reveals several key associations and patterns : 

We have found that late delivery and longer delivery days have association with customer's satisfaction that result in bad review scores. Also, this will impact the brand and business evaluation including potential income revenue of the Olist, since late delivary has association with lower customer retention rate.

![Homepage](images/output.png)

**1. Delivery Performance, Customer Satisfaction, and Retention**
- From all orders, the late delivery and on-time delivery percentage is 7.92% vs 92.08%, respectively. 
- The Median delivery duration: 9 days (on-time) vs. 29 days (late), which has a statistical difference at p=0.00.
- Customer satisfaction is closely tied to delivery speed:
    - Longer delivery durations are correlated with lower review scores (Spearman’s ρ = -0.22).
    - Median review score for late orders is 2, compared to 5 for on-time orders.
    - The association between late delivery and lower review scores is statistically significant (Chi-Square, p=0.00).
    - Customer retention is measurably lower among those experiencing late first orders: 2.51% retention vs. 3.04% for on-time, a significant difference (Chi-Square, p<0.01).

**2. Operational and Structural Factors Affecting Delivery**
- The platform’s On-Time Delivery (OTD) rate averaged 84.9% overall, with a high of 94.85% in 2016–2017 and 90% in 2018, indicating variability during increased volume season.
- Order volume is negatively correlated with OTD (Spearman’s ρ = -0.63), suggesting logistical challenges scale with demand.
- Both seller and logistics locations contribute to delays. Regional analysis shows the Northeast, including cities like Fortaleza and Salvador, experiences higher rates of late deliveries, highlighting potential infrastructure or process bottlenecks.
- Product category influences delay: Large, seasonal, or poorly structured categories (including “unknowns”) are more likely to be late. 
- Higher freight value, a proxy for product size or shipping distance, also correlates positively with longer delivery duration (ρ = 0.42).

![Homepage](images/Screenshot%202025-07-22%20at%2023.41.02.png)

- Order timestamp an holidays: Orders placed at midnight show a spike in late deliveries; meanwhile holidays themselves do not significantly increase delay risk, though order volume increases prior to major holidays.
- Payment method and use of installments do not show significant associations with late delivery.


## **Machine Learning**
Aim : to create a machine learning model that can predict an order will be delivered late or not
##### Futures Engineering 
We have built new features engineering : 
1. purchase_to_approve_hrs                 
2. approve_to_estimated_days               
3. approve_to_shipping_limit_days           
4. purchase_hour                            
5. purchase_dow                             
6. purchase_month                          
7. is_weekend                              
 8. is_brazil_holiday                       
 9. distance_km                             
 10.  same_state                              
 11. freight_ratio                           
 12. customer_is_remote                      
 13. seller_dispatch_hub                     
 14. seller_30d_dispatch_late_rate_raw       
 15. seller_30d_dispatch_late_rate_smoothed  
 16. eller_30d_order_count                  
 17. seller_90d_dispatch_late_rate_raw       
 18. seller_90d_dispatch_late_rate_smoothed  
 19. seller_90d_order_count 

##### Model Building 

##### Deliverables
- Tableau Dashboard: https://public.tableau.com/app/profile/risma.w.p./viz/OlistDeliveryPerformanceDashboard/Dashboard1#1
![Homepage](images/Screenshot%202025-07-22%20at%2023.04.21.png)
- Streamlit app: https://olist-delivery-predictor-alpha-team.streamlit.app
![Homepage](images/Screenshot%202025-07-22%20at%2023.05.04.png)