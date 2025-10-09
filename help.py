import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder,JsCode
import plotly.graph_objects as go
import streamlit as st

hide_streamlit_style = """
    <style>
    /* Hide hamburger menu */
    #MainMenu {visibility: hidden;}
    
    /* Hide default Streamlit header */
    header {visibility: hidden;}
    
    /* Hide footer */
    footer {visibility: hidden;}
    
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- DARK THEME AND STYLING ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@600&display=swap');

[data-testid="stAppViewContainer"] {background-color: #272D3A; color: white;}
div[data-testid="stDataFrameContainer"] table {
    background-color: #232834 !important;  /* Table background */
    color: white;                     /* Text color */
}
div[data-testid="stDataFrameContainer"] th {
    background-color: #232834 !important;  /* Header background */
    color: white;
}   
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}    
.element-container {
    margin: 0 !important;
    padding: 0 !important;
    padding-top: 0rem;
}  

</style>
""", unsafe_allow_html=True)

# Hide Streamlit default menu and header
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
#st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def tile(title, 
    value,
    bg="#333",     
    value_color="#4CAF50",
    value_size="32px",
    title_color="#FFFFFF"
):
    st.markdown(f"""
    <div style="
        background-color: {bg};
        display: flex; border-radius:8px;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2);padding:5px
    ">
        <div style="font-size: 14px; color: {title_color};text-align: left;margin-top:0rem">{title}</div>
        <div style="font-size: {value_size}; text-align: center;color: {value_color};height:140px;width:140px;margin-left:10px">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def tile_content(title, value, 
         bg="#222", 
         title_color="white", title_size="16px", 
         value_color="white", value_size="32px",
         padding="0px", border_radius="10px", margin_bottom ="5px"):
    
    return f'<div style="background:{bg};border-radius:{border_radius};text-align:left;font-family:Segoe UI Semibold"> <div style="margin-left:5px;margin-bottom:{margin_bottom};font-size:{title_size}; color:{title_color}; opacity:0.8;">{title}</div> <div style="font-size:{value_size};text-align:center;padding:{padding};color:{value_color}; font-weight:bold;font-family: Segoe UI Semibold">{value}</div>  </div>'
st.set_page_config(layout="wide")
# ----------------------------
# Page header
# ----------------------------
st.markdown("<h3 style='text-align:center; margin-top:0;border-radius:5px;background-color:#27283A; font-size: 28px;'>SALHN CareFlow Board</h3>", unsafe_allow_html=True)

ed_data = {
    'Hour': ["0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"],
    'Occupancy': [52,78,80,73,72,68,72,75,75,85,92,85,96,95,98,100,93,86,84,73,76,80,76,57],
    'Presentations': [5,8,7,7,6,9,5,7,21,23,15,26,20,18,22,20,16,23,13,19,19,16,12,12],
    'Departures':[11,9,13,5,11,5,4,2,5,12,14,13,19,10,20,22,20,16,24,13,9,10,26,12]
}
sas_data = {
    'Time': ["00:00","00:15","00:30","01:15","01:45","02:00","02:15","02:30","02:45","03:00","03:15","03:30","04:00","04:15","04:30","04:45","05:00","05:15","05:30","05:45","06:00","06:15","06:30","07:00","07:30","07:45","08:00","08:15","08:30","08:45","09:00","09:15","09:45","10:00","10:15","10:30","10:45","11:00","11:15","11:30","12:00","12:15","12:30","13:00","13:15","13:30","13:45","14:00","14:15","14:30","14:45","15","15:30","15:45","16:00","16:15","16:30","16:45","17:00","17:15","17:30","17:45","18:00","18:30","18:45","19:00","19:15","19:30","19:45","20:00","20:15","20:30","21:00","21:15","21:30","21:45","22:00","22:15","22:30","22:45","23:00","23:15","23:30","23:45"],
    'Arrivals':     [1,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,3,0,1,1,0,0,1,1,1,0,1,2,4,0,1,2,4,1,0,0,1,0,3,1,2,1,3,1,2,1,0,0,1,0,1,2,0,1,3,0,0,1,1,1,4,0,0,2,1,1,0,1,1,3,1,0,2,1,2,2,1,1,3,0,0,1,1,2],
    'Departures':   [0,1,0,2,1,2,0,0,0,3,0,1,2,1,0,0,1,1,0,1,2,2,0,1,0,2,0,1,0,2,0,2,2,2,1,2,0,2,2,2,2,1,1,3,1,2,1,1,0,1,0,1,1,0,1,1,2,1,1,0,0,1,5,0,0,2,2,0,0,1,1,2,1,1,1,0,0,2,1,4,1,1,1,1,]
}

ip_data = {
    'Hour': ["0:00","1:00","2:00","3:00","4:00","5:00","6:00","7:00","8:00","9:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00","17:00","18:00","19:00","20:00","21:00","22:00","23:00"],
    'Admissions': [6,7,3,6,1,5,10,23,16,8,10,7,10,13,19,18,14,10,8,10,11,6,6,8],
    'Separations': [4,0,4,2,2,4,0,2,6,9,15,20,32,24,24,9,24,7,20,11,5,3,6,2]
}
ed_df = pd.DataFrame(ed_data)
sas_df = pd.DataFrame(sas_data)
ip_df = pd.DataFrame(ip_data)


with st.container():
    chart_col1, chart_col2 =  st.columns([1,1],gap="small", border=False, width="stretch") 
    with chart_col1:
        col1, col2 = st.columns([1,4],gap="small", vertical_alignment="top", border=False, width="stretch")
        with col1:
            tile("Flow Health", "85", bg="#3E475C", value_color="#4CAF50", value_size="80px",title_color="#FFFFFF") 
        with col2:
            st.markdown(f"""
        <div style="
            display: grid;
            grid-template-columns: repeat(4, 100px);  /* 2 columns of 65px */
            gap: 5px;     margin-top: 75px;                          
        ">
            {tile_content("Critical","5", bg="#3E475C", value_color="#D9534F", value_size="50px",title_size="10px",margin_bottom="0px")}
            {tile_content("High","1", bg="#3E475C", value_color="#E5804F", value_size="50px",title_size="10px",margin_bottom="0px")}
            {tile_content("Medium","7", bg="#3E475C", value_color="#F0AD4E", value_size="50px",title_size="10px",margin_bottom="0px")}            
            {tile_content("Normal","16", bg="#3E475C", value_color="#5CBB5C", value_size="50px",title_size="10px",margin_bottom="0px")}
        </div>
        """, unsafe_allow_html=True)
        #chart_col1.subheader("Emergency Department")
        st.markdown('<div style="font-family:Segoe UI Semibold"><br/><h3>Emergency Department</h3></div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="
            display: grid;
            grid-template-columns: repeat(9, 85px);  /* 9 columns of 80px */
            grid-template-rows: repeat(2, 85px);     /* 2 rows of 80px */
            gap: 8px;                               /* space between tiles */  
        ">
            {tile_content("#Amb on Ramp","7", bg="#F0AD4E", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="5px")}
            {tile_content("Hours on Ramp","14hrs", bg="#F0AD4E", value_color="#FFFAFA", value_size="22px",title_size="9px",margin_bottom="10px")}
            {tile_content("Longest on Ramp","3hrs 30", bg="#F0AD4E", value_color="#FFFAFA", value_size="22px",title_size="9px",margin_bottom="10px")}
            {tile_content("Occupancy","98", bg="#F0AD4E", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="5px")}
            {tile_content("WTBS (Waiting to be seen)","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="5px")}
            {tile_content("Resus Capacity","1", bg="#F0AD4E", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="5px")}
            {tile_content("Avg Time Waiting room","1hr 27", bg="#5CBB5C", value_color="#FFFAFA", value_size="22px",title_size="9px",margin_bottom="0px")}
            {tile_content("WFB Total","25", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="4x")}
            {tile_content("WFB Side Room Demand","4", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="0px")}
            {tile_content("#Patient over 24 hours","7", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="0px")}
            {tile_content("Allocated to Bed","9", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="8px")}
            {tile_content("CARE Capacity","4", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("TIP to AAB","3.6 hrs", bg="#5CBB5C", value_color="#FFFAFA", value_size="22px",title_size="9px",margin_bottom="12px")}
            {tile_content("RWT to ED Departure","4.7 hrs", bg="#E5804F", value_color="#FFFAFA", value_size="22px",title_size="9px",margin_bottom="2px")}
            {tile_content("AAB to RWT","2.4 hrs", bg="#5CBB5C", value_color="#FFFAFA", value_size="22px",title_size="9px",margin_bottom="12px")}
            {tile_content("Waiting for CT","5", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("Waiting for X-Ray","12", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("Waiting for US","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
        </div>
        """, unsafe_allow_html=True)
        with st.container():
            st.markdown(f"<br/>", unsafe_allow_html=True)
            sl_col1, sl_col2= st.columns([1,1]) 
            with sl_col1:
                st.markdown('<div style="font-family:Segoe UI Semibold"><h3>Inpatient Capacity</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                    <div style="
                        display: grid;
                        grid-template-columns: repeat(3, 85px);  /* 2 columns of 70px */
                        grid-template-rows: repeat(2, 85px);     /* 2 rows of 70px */
                        gap: 8px;                               /* space between tiles */
                    ">
            {tile_content("ICU Capacity","1", bg="#F0AD4E", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("EECU Capacity","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("ED Accessible Bed","0", bg="#D9534F", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("Side Rooms","0", bg="#D9534F", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("Flex Beds","0", bg="#D9534F", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("Emergency Surgery","8", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            </div>
                    """, unsafe_allow_html=True)
                st.markdown('<div style="font-family:Segoe UI Semibold"><h3>Staffing Levels</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                    <div style="
                        display: grid;
                        grid-template-columns: repeat(6, 85px);  /* 2 columns of 70px */
                        gap: 8px;                               /* space between tiles */
                    ">
            {tile_content("ED Nursing","0", bg="#3E475C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("ED Medical","0", bg="#3E475C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("ED Allied Health","0", bg="#3E475C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("IP Nursing","0", bg="#3E475C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("IP Medical","0", bg="#3E475C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("IP Allied Health","0", bg="#3E475C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            </div>
                    """, unsafe_allow_html=True)
            
            
            with sl_col2:  
                st.markdown('<div style="font-family:Segoe UI Semibold"><h3>Inpatient Flow</h3></div>', unsafe_allow_html=True)
                st.markdown(f"""
                <div style="
                    display: grid;
                    grid-template-columns: repeat(3, 85px);  /* 2 columns of 70px */
                    grid-template-rows: repeat(2, 85px);     /* 2 rows of 70px */
                    gap: 8px;                               /* space between tiles */
                ">
            {tile_content("ICU Pts ready for DC","3", bg="#F0AD4E", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="0px")}
            {tile_content("Side rooms Pt ready DC","0", bg="#D9534F", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="0px")}
            {tile_content("RACF Pts","10", bg="#D9534F", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="12px")}
            {tile_content("Transfer out Ready","39", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}
            {tile_content("SIFT","25", bg="#5CBB5C", value_color="#FFFAFA", value_size="30px",title_size="9px",margin_bottom="10px")}                </div>
                """, unsafe_allow_html=True)
    
    with chart_col2:

        fig = go.Figure()

        # Bar 1: Presentations
        fig.add_trace(go.Bar(
            x=ed_df["Hour"],
            y=ed_df["Presentations"],
            name="Presentations",
            marker_color="#6495ED"
        ))

        # Bar 2: Departures
        fig.add_trace(go.Bar(
            x=ed_df["Hour"],
            y=ed_df["Departures"],
            name="Departures",
            marker_color="#6A5ACD"
        ))

        # Line: Occupancy
        fig.add_trace(go.Scatter(
            x=ed_df["Hour"],
            y=ed_df["Occupancy"],
            name="Occupancy (%)",
            mode="lines+markers",
            line=dict(color="rgba(255, 193, 7, 1)", width=2),
            marker=dict(size=5),
            yaxis="y2"
        ))


        fig.update_layout(
            title=dict(
                text="Emergency department Activity<br><sub>Last 24 Hours</sub>",
                font=dict(size=18)
            ),
            xaxis=dict(
                title="Hour",
                tickmode='linear',
                dtick=2,
                showgrid=False
            ),
            yaxis=dict(
 #               title="Admissions / Separations",
                showgrid=False
            ),
            yaxis2=dict(
                title="Occupancy (%)",
                overlaying="y",
                side="right",
                showgrid=False
            ),
            barmode="group",  # group bars side by side
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.1,
                xanchor="center",
                x=0.8
            ),
            plot_bgcolor="#272D3A",   # Chart background
            paper_bgcolor="#272D3A",  # Outer background
            font_color="white"  ,      # Text color,
            width=400,    # pixels
            height=280,   # pixels
        )

        st.plotly_chart(fig, use_container_width=True)
        fig = go.Figure()

        # Bar 1: Arrivals
        fig.add_trace(go.Bar(
            x=sas_df["Time"],
            y=sas_df["Arrivals"],
            name="Arrivals",
            marker_color="#6495ED"
        ))

        # Bar 2: Departures
        fig.add_trace(go.Bar(
            x=sas_df["Time"],
            y=sas_df["Departures"],
            name="Departures",
            marker_color="#6A5ACD"
        ))


        fig.update_layout(
            title=dict(
                text="SAAS Activity<br><sub>Last 24 Hours</sub>",
                font=dict(size=18)
            ),
            xaxis=dict(
                title="Hour",
                tickmode='linear',
                dtick=20,
                showgrid=False
            ),
            yaxis=dict(
                
#                title="Admissions / Separations",
                showgrid=False
            ),           
            barmode="group",  # group bars side by side
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.2,
                xanchor="center",
                x=0.9
            ),margin=dict(l=0, r=0, t=0, b=0),
            plot_bgcolor="#272D3A",   # Chart background
            paper_bgcolor="#272D3A",  # Outer background
            font_color="white"  ,      # Text color,
            width=400,    # pixels
            height=280,   # pixels
        )

        st.plotly_chart(fig, use_container_width=True)
        
        
    

        fig = go.Figure()

        # Bar 1: Admissions
        fig.add_trace(go.Bar(
            x=ip_df["Hour"],
            y=ip_df["Admissions"],
            name="Admissions",
            marker_color="#6495ED"
        ))

        # Bar 2: Separations
        fig.add_trace(go.Bar(
            x=ip_df["Hour"],
            y=ip_df["Separations"],
            name="Separations",
            marker_color="#6A5ACD"
        ))


        fig.update_layout(
            title=dict(
                text="Inpatient Activity<br><sub>Last 24 Hours</sub>",
                font=dict(size=18)
            ),
            xaxis=dict(
                title="Hour",
                tickmode='linear',
                dtick=2,
                showgrid=False
            ),
            yaxis=dict(
                
#                title="Admissions / Separations",
                showgrid=False
            ),           
            barmode="group",  # group bars side by side
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.05,
                xanchor="center",
                x=0.5
            ),
            plot_bgcolor="#272D3A",   # Chart background
            paper_bgcolor="#272D3A",  # Outer background
            font_color="white"  ,      # Text color,
            width=400,    # pixels
            height=280,   # pixels
        )

        st.plotly_chart(fig, use_container_width=True)
    

    #     fig = go.Figure()

    #     # Area chart - occupancy
    #     fig.add_trace(go.Scatter(
    #         x=ed_df['Hour'], 
    #         y=ed_df['Occupancy'], 
    #         fill='tozeroy',
    #         mode='none',
    #         name='Occupancy',
    #         fillcolor='rgba(123, 86, 219, 0.6)'
    #     ))
    #     # Line 1 - present
    #     fig.add_trace(go.Scatter(
    #         x=ed_df['Hour'], 
    #         y=ed_df['Presentations'], 
    #         mode='lines',
    #         name='Presentations',
    #         line=dict(color='#50C89F', width=3)
    #     ))

    #     # Line 2 - depart
    #     fig.add_trace(go.Scatter(
    #         x=ed_df['Hour'], 
    #         y=ed_df['Departures'], 
    #         mode='lines',
    #         name='Departures',
    #         line=dict(color='#F0AD4E', width=3)
    #     ))
    # #B163FF
 

    #     fig.update_layout(
    #         title=dict(
    #         text="Emergency department Activity<br><sub>Last 24 Hours</sub>",
    #         #x=0.5  # center align
    #     ),
    #      xaxis=dict(
    #     dtick=5  # show a label every 5 units
    # ),
    #         legend=dict(
    #         orientation="h",
    #         yanchor="top",
    #         y=1.3,
    #         xanchor="center",
    #         x=0.8
    #     ),
    #         xaxis_title="Hours",
    #         #yaxis_title="Values",
    #         template="plotly_white",
    #         plot_bgcolor="#272D3A",   # Chart background
    #         paper_bgcolor="#272D3A",  # Outer background
    #         font_color="white"  ,      # Text color,
    #         width=400,    # pixels
    #         height=300,   # pixels
    #     )
    #     st.plotly_chart(fig, use_container_width=True)
        #st.markdown(f"<br/><br/>", unsafe_allow_html=True)
                

 
    #     fig = go.Figure()

    #     # Admissions Area
    #     fig.add_trace(go.Scatter(
    #         x=ip_df["Hour"],
    #         y=ip_df["Admissions"],
    #         mode='lines',
    #         stackgroup='one',
    #         name='Admissions',
    #         fillcolor='rgba(0, 156, 236, 0.4)',
    #         line=dict(color='rgba(0,0,0,0)') 
    #     ))


    #     # Separations Area
    #     fig.add_trace(go.Scatter(
    #         x=ip_df["Hour"],
    #         y=ip_df["Separations"],            
    #         stackgroup='one',
    #         name='Separations',
    #         fillcolor='rgba(123, 86, 219, 0.6)',  # <-- Different transparency
    #         line=dict(color='rgba(0,0,0,0)') 
    #     ))


    #     fig.update_layout(
    #         title=dict(
    #         text="Inpatient Activity<br><sub>Last 24 Hours</sub>",
    #         #x=0.5  # center align
    #     ),
    #      xaxis=dict(
    #     dtick=5  # show a label every 5 units
    # ),
    #         legend=dict(
    #         orientation="h",
    #         yanchor="top",
    #         y=1.4,
    #         xanchor="center",
    #         x=0.9
    #     ),
    #         xaxis_title="Hours",
    #         #yaxis_title="Values",
    #         template="plotly_white",
    #         plot_bgcolor="#272D3A",   # Chart background
    #         paper_bgcolor="#272D3A",  # Outer background
    #         font_color="white"  ,      # Text color,
    #         width=400,    # pixels
    #         height=350,   # pixels
    #     )

    #     st.plotly_chart(fig, use_container_width=True)