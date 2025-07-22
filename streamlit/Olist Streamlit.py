import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
import os
import category_encoders as ce
from streamlit_option_menu import option_menu

# List of date columns for each Olist dataset:
# This dictionary maps each dataset filename to a list of columns that should be parsed as dates.
date_cols = {
    'olist_orders_dataset.csv': [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
    ],
    'olist_order_items_dataset.csv': [
        'shipping_limit_date',
    ],
    'olist_order_reviews_dataset.csv': [
        'review_creation_date',
        'review_answer_timestamp',
    ],
    # The following datasets have NO date columns:
    # 'olist_customers_dataset.csv'
    # 'olist_geolocation_dataset.csv'
    # 'olist_order_payments_dataset.csv'
    # 'olist_products_dataset.csv'
    # 'olist_sellers_dataset.csv'
    # 'product_category_name_translation.csv'
    'master_olist_dataset.csv': [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
        'shipping_limit_date',
        'review_creation_date',
        'review_answer_timestamp',
    ],
}

def read_olist_csv(path):
    """
    Reads an Olist CSV and parses dates for the correct columns.
    Args:
        path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataframe with date columns parsed as datetime.
    """
    # Extract just the filename, e.g., 'olist_orders_dataset.csv':
    filename = os.path.basename(path)
    # Get the correct date columns for this file, or an empty list:
    parse_dates = date_cols.get(filename, [])
    # Read the CSV, parsing the specified date columns (if any):
    return pd.read_csv(path, parse_dates=parse_dates)

# Load dataset:
df = read_olist_csv('../data/cleaned_data/olist_ml_ready_dataset.csv')

# Split features and target:
X = df.drop(columns=['is_late'])
y = df['is_late']

# Assign to X_train and y_train:
X_train, y_train = X, y

# Load pipeline:
model_pipeline = joblib.load('best_rf_pipeline.pkl')

# Sidebar navigation for multipage:
with st.sidebar:
    selected = option_menu(
        "Olist in Motion",
        ["Home", "Prediction Tool", "Disclaimer"],
        icons=["house", "truck", "exclamation-triangle"],
        menu_icon="box-seam",
        default_index=0,
        orientation="vertical"
    )

    # Space:
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Creator info at the bottom:
    st.markdown(
        """
        <div style='
            margin-top: 35vh;
            text-align: center;
            color: #FFFFFF;
            font-size: 14px;
            font-weight: italic;
        '>
            Courtesy of Alpha Team
        <div style='margin-top:8px;'>
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-rocket" viewBox="0 0 16 16">
                <path d="M8 8c.828 0 1.5-.895 1.5-2S8.828 4 8 4s-1.5.895-1.5 2S7.172 8 8 8"/>
                <path d="M11.953 8.81c-.195-3.388-.968-5.507-1.777-6.819C9.707 1.233 9.23.751 8.857.454a3.5 3.5 0 0 0-.463-.315A2 2 0 0 0 8.25.064.55.55 0 0 0 8 0a.55.55 0 0 0-.266.073 2 2 0 0 0-.142.08 4 4 0 0 0-.459.33c-.37.308-.844.803-1.31 1.57-.805 1.322-1.577 3.433-1.774 6.756l-1.497 1.826-.004.005A2.5 2.5 0 0 0 2 12.202V15.5a.5.5 0 0 0 .9.3l1.125-1.5c.166-.222.42-.4.752-.57.214-.108.414-.192.625-.281l.198-.084c.7.428 1.55.635 2.4.635s1.7-.207 2.4-.635q.1.044.196.083c.213.09.413.174.627.282.332.17.586.348.752.57l1.125 1.5a.5.5 0 0 0 .9-.3v-3.298a2.5 2.5 0 0 0-.548-1.562zM12 10.445v.055c0 .866-.284 1.585-.75 2.14.146.064.292.13.425.199.39.197.8.46 1.1.86L13 14v-1.798a1.5 1.5 0 0 0-.327-.935zM4.75 12.64C4.284 12.085 4 11.366 4 10.5v-.054l-.673.82a1.5 1.5 0 0 0-.327.936V14l.225-.3c.3-.4.71-.664 1.1-.861.133-.068.279-.135.425-.199M8.009 1.073q.096.06.226.163c.284.226.683.621 1.09 1.28C10.137 3.836 11 6.237 11 10.5c0 .858-.374 1.48-.943 1.893C9.517 12.786 8.781 13 8 13s-1.517-.214-2.057-.607C5.373 11.979 5 11.358 5 10.5c0-4.182.86-6.586 1.677-7.928.409-.67.81-1.082 1.096-1.32q.136-.113.236-.18Z"/>
                <path d="M9.479 14.361c-.48.093-.98.139-1.479.139s-.999-.046-1.479-.139L7.6 15.8a.5.5 0 0 0 .8 0z"/>
            </svg>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

def home():
    st.markdown(
        """
        <div style='
            background-color:#0092C2;
            color:#FFFFFF;
            padding:10px;
            border-radius:10px;
            font-size:40px;
            font-weight:bold;
            text-align:center;
        '>
            Welcome to Olist in Motion!
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    > **E-commerce is booming**, and timely delivery is more important than ever. In the competitive world of online retail, a late delivery doesn't just frustrate customers, it can also lead to churn, negative reviews, and costly refunds or vouchers.  
    >  
    > That's where **Olist in Motion** comes in. Instead of guessing which orders might be delayed, this app uses machine learning to analyse key order and shipping features to **predict late deliveries before they happen**. This empowers the operations team to take proactive steps like adjusting logistics or setting better customer expectations.  
    >
    > **Ready to stay ahead of delays? Let's get moving with Olist in Motion!**
    """)

def predictor():
    st.markdown(
        """
        <div style='
            background-color:#0092C2;
            color:#FFFFFF;
            padding:10px;
            border-radius:10px;
            font-size:40px;
            font-weight:bold;
            text-align:center;
        '>
            Olist Delivery Predictor
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    > Input delivery details manually or upload your own dataset for batch predictions.
    """)

    # Timeline Features:
    st.markdown("### Order Timeline")
    time_col1, time_col2, time_col3 = st.columns(3)
    with time_col1:
        purchase_to_approve_hrs = st.number_input("Purchase to Approve (Hours)", min_value=0.0, value=1.0)
    with time_col2:
        approve_to_estimated_days = st.number_input("Approve to Estimated Delivery (Days)", min_value=0, value=3)
    with time_col3:
        approve_to_shipping_limit_days = st.number_input("Approve to Shipping Limit (Days)", min_value=0, value=2)

    # Purchase Info:
    st.markdown("### Purchase Info")
    purchase_col1, purchase_col2, purchase_col3 = st.columns(3)
    with purchase_col1:
        purchase_hour = st.slider("Purchase Hour", 0, 23, value=12)
    with purchase_col2:
        purchase_dow = st.slider("Purchase Day of Week", 0, 6, value=3)
    with purchase_col3:
        purchase_month = st.slider("Purchase Month", 1, 12, value=6)

    # Flags and Distance:
    st.markdown("### Location & Flags")
    flag_col1, flag_col2, flag_col3 = st.columns(3)
    with flag_col1:
        is_weekend = st.selectbox("Weekend?", [0, 1])
    with flag_col2:
        is_brazil_holiday = st.selectbox("Brazil Holiday?", [0, 1])
    with flag_col3:
        customer_is_remote = st.selectbox("Remote Area?", [0, 1])

    st.markdown("### Delivery & Geography")
    geo_col1, geo_col2 = st.columns(2)
    with geo_col1:
        distance_km = st.number_input("Distance (km)", min_value=0.0, value=50.0)
        same_state = st.selectbox("Same State?", [0, 1])
    with geo_col2:
        freight_ratio = st.number_input("Freight Ratio", min_value=0.0, value=0.2)

    # Seller Info:
    st.markdown("### Seller Metrics")
    seller_col1, seller_col2 = st.columns(2)
    with seller_col1:
        seller_dispatch_hub = st.selectbox("Seller from Dispatch Hub?", [0.0, 1.0])
        seller_30d_order_count = st.number_input("30d Order Count", min_value=0.0, value=15.0)
        seller_30d_late_raw = st.number_input("30d Raw Late Rate", min_value=0.0, value=0.05)
        seller_30d_late_smooth = st.number_input("30d Smoothed Late Rate", min_value=0.0, value=0.04)
    with seller_col2:
        seller_90d_order_count = st.number_input("90d Order Count", min_value=0.0, value=40.0)
        seller_90d_late_raw = st.number_input("90d Raw Late Rate", min_value=0.0, value=0.06)
        seller_90d_late_smooth = st.number_input("90d Smoothed Late Rate", min_value=0.0, value=0.05)

    # Financials:
    st.markdown("### Order Value Info")
    finance_col1, finance_col2 = st.columns(2)
    with finance_col1:
        total_order_lifetime = st.number_input("Total Order Lifetime (days)", min_value=0, value=5)
        sum_freight_value = st.number_input("Total Freight Value", min_value=0.0, value=20.0)
    with finance_col2:
        price = st.number_input("Product Price", min_value=0.0, value=100.0)
        total_payment_value = st.number_input("Total Payment Value", min_value=0.0, value=120.0)

    # Categorical Inputs:
    st.markdown("### Categorical Inputs")
    cat_col1, cat_col2 = st.columns(2)
    with cat_col1:
        customer_state = st.selectbox("Customer State", df['customer_state'].unique().tolist())
        product_category = st.selectbox("Product Category", df['product_category_name_english'].unique().tolist())
    with cat_col2:
        seller_state = st.selectbox("Seller State", df['seller_state'].unique().tolist())
        payment_types = st.selectbox("Payment Type", df['payment_types'].unique().tolist())

    if st.button("Predict Late Delivery"):
        input_df = pd.DataFrame([{
            "purchase_to_approve_hrs": purchase_to_approve_hrs,
            "approve_to_estimated_days": approve_to_estimated_days,
            "approve_to_shipping_limit_days": approve_to_shipping_limit_days,
            "purchase_hour": purchase_hour,
            "purchase_dow": purchase_dow,
            "purchase_month": purchase_month,
            "is_weekend": is_weekend,
            "is_brazil_holiday": is_brazil_holiday,
            "distance_km": distance_km,
            "same_state": same_state,
            "freight_ratio": freight_ratio,
            "customer_is_remote": customer_is_remote,
            "seller_dispatch_hub": seller_dispatch_hub,
            "seller_30d_dispatch_late_rate_raw": seller_30d_late_raw,
            "seller_30d_dispatch_late_rate_smoothed": seller_30d_late_smooth,
            "seller_30d_order_count": seller_30d_order_count,
            "seller_90d_dispatch_late_rate_raw": seller_90d_late_raw,
            "seller_90d_dispatch_late_rate_smoothed": seller_90d_late_smooth,
            "seller_90d_order_count": seller_90d_order_count,
            "total_order_lifetime": total_order_lifetime,
            "sum_freight_value": sum_freight_value,
            "price": price,
            "total_payment_value": total_payment_value,
            "customer_state": customer_state,
            "seller_state": seller_state,
            "freight_value": sum_freight_value,
            "product_category_name_english": product_category,
            "payment_types": payment_types
        }])
    
        prediction = model_pipeline.predict(input_df)[0]
        if prediction:
            st.markdown("""
                <div style="padding: 1rem; border: 2px solid red; border-radius: 10px; background-color: #ffe6e6;">
                    <h3 style="color:red;">
                        <i class="bi bi-exclamation-triangle-fill"></i> Late Delivery Predicted
                    </h3>
                    <p style="color:red;">Try adjusting fulfillment or shipping strategy.</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="padding: 1rem; border: 2px solid green; border-radius: 10px; background-color: #e6ffe6;">
                    <h3 style="color:green;">
                        <i class="bi bi-check-circle-fill"></i> On-Time Delivery Predicted
                    </h3>
                    <p style="color:green;">No delay expected. Proceed as usual.</p>
                </div>
            """, unsafe_allow_html=True)


    # Batch predictions section:
    st.markdown("### Batch Predictions")
    st.markdown("> Upload a CSV file to get predictions for multiple orders.")

    uploaded_file = st.file_uploader("Upload Your File:", type=["csv"])

    if uploaded_file is not None:
        try:
            # Load uploaded data:
            user_data = pd.read_csv(uploaded_file)

            # Basic clean-up if needed:
            if 'order_approved_at' in user_data.columns and 'order_purchase_timestamp' in user_data.columns:
                # Convert to datetime:
                user_data['order_approved_at'] = pd.to_datetime(user_data['order_approved_at'])
                user_data['order_purchase_timestamp'] = pd.to_datetime(user_data['order_purchase_timestamp'])

                # Derive duration feature:
                user_data['purchase_to_approve_hrs'] = (
                    user_data['order_approved_at'] - user_data['order_purchase_timestamp']
                ).dt.total_seconds() / 3600

            # Make predictions:
            predictions = model_pipeline.predict(user_data)

            # Add predictions to DataFrame:
            user_data['predicted_late'] = predictions

            st.markdown("### Predictions")
            st.dataframe(user_data)

            # Prepare download button:
            csv = user_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Predictions as CSV",
                data=csv,
                file_name="delivery_predictions.csv",
                mime='text/csv'
            )

        except Exception as e:
            st.error(f"Error processing your file: {e}")

def disclaimer():
    st.markdown(
        """
        <div style='
            background-color:#0092C2;
            color:#FFFFFF;
            padding:10px;
            border-radius:10px;
            font-size:40px;
            font-weight:bold;
            text-align:center;
        '>
            Disclaimer
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("### Model Purpose")
    st.markdown("""
    This model is built to **predict the risk of late deliveries** using a Random Forest Classifier trained on historical delivery and seller behaviour data.
    """)

    st.markdown("### Model Limitations")

    st.markdown("""
    > - **No Real-Time Factors**  
    The model doesn't account for real-time issues like traffic, weather, or sudden carrier strikes.

    > - **Historical Bias**  
    Predictions are based on past behaviour. New sellers or recent policy changes may not be reflected accurately.

    > - **Ethical Use**  
    Model outputs should support human decision-making, not replace it. Use results to inform strategy, not penalise sellers directly without review.
    """)

    st.markdown("### Final Note")
    st.markdown("""
    These insights and actions are **model-guided**, not deterministic. Continuous monitoring, human judgment, and A/B testing are essential to refine performance over time.
    """)

# Page router:
if selected == "Home":
    home()
elif selected == "Prediction Tool":
    predictor()
elif selected == "Disclaimer":
    disclaimer()