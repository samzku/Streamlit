import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
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
    
    /* Remove default padding at top */
    .block-container {
        padding-top: 0rem;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- DARK THEME AND STYLING ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@600&display=swap');

[data-testid="stAppViewContainer"] {background-color: #272D3A; color: white;}
div[data-testid="stDataFrameContainer"] table {
    background-color: #1E1E1E !important;  /* Table background */
    color: white;                           /* Text color */
}
div[data-testid="stDataFrameContainer"] th {
    background-color: #333333 !important;  /* Header background */
    color: white;
}   
.block-container {
    max-width: auto;
    margin: auto;
    <!--padding-left: 0rem;
    padding-right: 0rem;-->
}    
   
.tile {
    padding: 10px;
    border-radius: 5px;
    color: white;
    text-align: center;
    box-shadow: 0px 0px 10px #00000050;
    margin-bottom: 2px;
}
.tile h1 {margin: 0; font-size: 45px;}
.tile h2 {margin: 0; font-size: 28px;}
.tile.red {background-color: #D9534F;}
.tile.orange {background-color: #E5804F;}
.tile.green {background-color: #2ca02c;}
.tile.gray {background-color: #3a3a3a;}
.summary-table {
    background-color: #1E1E1E;
    padding: 10px;
    border-radius: 10px;
    color: white;
    height: 120px;
    overflow-y: auto;
}
            .table-container {
    background-color: #333;
    color: white;
    padding: 15px;
    border-radius: 8px;
    width: 100%;
}

.table-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    text-align: center;
}

.custom-table {
    width: 100%;
    border-collapse: collapse;
}

.custom-table th {
    background-color: #555;
    padding: 8px;
    text-align: center;
}

.custom-table td {
    padding: 6px;
    text-align: center;
    border-bottom: 1px solid #777;
}

.custom-table tr:hover {
    background-color: #444;
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
    value_size="28px",
    title_color="#FFFFFF"
):
    st.markdown(f"""
    <div style="
        background-color: {bg};
        text-align: center;
        display: flex; border-radius:8px;
        flex-direction: column;
        justify-content: center;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.2);
    ">
        <div style="font-size: 14px; font-weight: bold; color: {title_color};">{title}</div>
        <div style="font-size: {value_size}; font-weight: bold; color: {value_color};">{value}</div>
    </div>
    """, unsafe_allow_html=True)


def tile_content(title, value, 
         bg="#222", 
         title_color="white", title_size="16px", 
         value_color="white", value_size="32px",
         padding="10x", border_radius="8px"):
    
    return f'<div style="background:{bg};padding:{padding};border-radius:{border_radius};text-align:center;"> <div style="font-size:{title_size}; color:{title_color}; opacity:0.8;">{title}</div> <div style="font-size:{value_size}; color:{value_color}; font-weight:bold;">{value}</div>  </div>'
st.set_page_config(layout="wide")
# ----------------------------
# Page header
# ----------------------------
st.markdown("<h3 style='text-align:center; margin-top:0;border-radius:5px;background-color:#232834; font-size: 28px;'>SALHN CareFlow Board</h3>", unsafe_allow_html=True)
with st.container():
    col1, col2, col3 = st.columns([0.5,2.5,1],gap="small", vertical_alignment="top", border=False, width="stretch") 

    # --- BIG KPI ON LEFT ---
    with col1:    
        tile("Flow Health", "85", bg="#3E475C", value_color="#4CAF50", value_size="45px",title_color="#FFFFFF")
        #st.markdown('<div style="box-shadow: 0px 0px 10px #00000050;display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;">Overall Completion %<h2 style="color:green">85</h></div>', unsafe_allow_html=True)

    # --- TABLE IN THE MIDDLE ---
    with col2:
        st.markdown("""
    <div style="
        background-color:#3E475C; 
        color:white; 
        padding:5px; 
        text-align:left;
        font-weight:bold;
        font-size:14px;
    ">
        Ward Occupancy & Capacity
    </div>
    """, unsafe_allow_html=True)
        #st.markdown('<div class="summary-table"><h2>Ward Occupancy</h2></div>', unsafe_allow_html=True)
        # Example table
        df_table = pd.DataFrame({
            "Division": ["Medicine, Cardiac and Critical Care", "3GOF", "4A", "4D"],
            "Physical": [304, 18, 26, 28],
            "Flex": [13, 0, 2, 2],
            "16:00": ["91%", "101%", "82%", "89%"],
            "15:00": ["91%", "101%", "82%", "89%"],
            "14:00": ["91%", "101%", "82%", "89%"],
            "13:00": ["91%", "101%", "82%", "89%"],
            "12:00": ["91%", "101%", "82%", "89%"],
            "11:00": ["91%", "101%", "82%", "89%"],
            "10:00": ["91%", "101%", "82%", "89%"],
            "09:00": ["91%", "101%", "82%", "89%"],
            "08:00": ["91%", "101%", "82%", "89%"]
            
        })
        gb = GridOptionsBuilder.from_dataframe(df_table)
        #for col in df_table.columns:
        #    gb.configure_column(col, width=100)
        # Set fixed width for columns
   
        #gb.configure_column("Physical", width=120)
        #gb.configure_column("Flex", width=120)
        #gb.configure_columns(["Division"], cellStyle={'color': 'white', 'backgroundColor': '#333'})

      
        gb.configure_grid_options(domLayout='normal')
        gb.configure_default_column(resizable=True, editable=False)
        #gb.configure_column("Division", width=150)        # pixels
        # Style via cellClassRules (optional) or gridTheme
        grid_options = gb.build()
        AgGrid(df_table, gridOptions=grid_options,fit_columns_on_grid_load=True,height=100)
        #st.dataframe(df_table, use_container_width=True)

    # --- SMALL KPI TILES ON RIGHT ---
    small_tiles = [
        ("Critical", 5, "red"),
        ("Medium", 7, "orange"),
        ("Low", 1, "red"),
        ("Normal", 16, "green")
    ]

    with col3:
        st.markdown(f"""
        <div style="
            display: grid;
            grid-template-columns: repeat(2, 65px);  /* 2 columns of 65px */
            grid-template-rows: repeat(2, 65px);     /* 2 rows of 65px */
            gap: 10px;                               /* space between tiles */
        ">
            {tile_content("Critical","7", bg="#3E475C", value_color="#D94446", value_size="30px")}
            {tile_content("Medium","8", bg="#3E475C", value_color="#FFCE1B", value_size="30px")}
            {tile_content("High","1", bg="#3E475C", value_color="#FF7518", value_size="30px")}
            {tile_content("Normal","16", bg="#3E475C", value_color="#3CAE63", value_size="30px")}
        </div>
        """, unsafe_allow_html=True)
# --- CHARTS BELOW ---

ed_data = {
    'Hour': ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"],
    'Occupancy': [52,78,80,73,72,68,72,75,75,85,92,85,96,95,98,100,93,86,84,73,76,80,76,57],
    'Presentations': [5,8,7,7,6,9,5,7,21,23,15,26,20,18,22,20,16,23,13,19,19,16,12,12],
    'Departures':[11,9,13,5,11,5,4,2,5,12,14,13,19,10,20,22,20,16,24,13,9,10,26,12]
}

df = pd.DataFrame(ed_data)

with st.container():
    chart_col1, chart_col2 =  st.columns([1,2],gap="medium") 
    with chart_col1:
        chart_col1.subheader("Emergency Department")
        #st.markdown('<div><h3>Emergency Department</h23</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div style="
            display: grid;
            grid-template-columns: repeat(9, 70px);  /* 9 columns of 80px */
            grid-template-rows: repeat(2, 70px);     /* 2 rows of 80px */
            gap: 5px;                               /* space between tiles */  
        ">
            {tile_content("#Amb on Ramp","14", bg="#F0AD4E", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Hours on Ramp","14hrs", bg="#F0AD4E", value_color="#FFFAFA", value_size="18px",title_size="11px")}
            {tile_content("Longest on Ramp","3hrs 30", bg="#F0AD4E", value_color="#FFFAFA", value_size="18px",title_size="10px")}
            {tile_content("Occupancy","98", bg="#F0AD4E", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Resus Capacity","1", bg="#F0AD4E", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Average Time waiting room","1hr 27", bg="#5CBB5C", value_color="#FFFAFA", value_size="18px",title_size="10px")}
            {tile_content("WFB Total","25", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("RWT to ED Departure","4.7 hrs", bg="#E5804F", value_color="#FFFAFA", value_size="18px",title_size="10px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
            {tile_content("Workforce","10", bg="#5CBB5C", value_color="#FFFAFA", value_size="24px",title_size="11px")}
        </div>
        """, unsafe_allow_html=True)
        
    with chart_col2:
        fig = go.Figure()

        # Line 1 - present
        fig.add_trace(go.Scatter(
            x=df['Hour'], 
            y=df['Presentations'], 
            mode='lines',
            name='Presentations',
            line=dict(color='#50C89F', width=3)
        ))

        # Line 2 - depart
        fig.add_trace(go.Scatter(
            x=df['Hour'], 
            y=df['Departures'], 
            mode='lines',
            name='Departures',
            line=dict(color='#F0AD4E', width=3)
        ))
    #B163FF
        # Area chart - occupancy
        fig.add_trace(go.Scatter(
            x=df['Hour'], 
            y=df['Occupancy'], 
            fill='tozeroy',
            mode='none',
            name='Occupancy',
            fillcolor='rgba(127,0,255, 0.3)'
        ))

        fig.update_layout(
            title=dict(
            text="Emergency department Activity<br><sub>Last 24 Hours</sub>",
            #x=0.5  # center align
        ),
            legend=dict(
            orientation="h",
            yanchor="top",
            y=1.1,
            xanchor="center",
            x=0.5
        ),
            xaxis_title="Hours",
            #yaxis_title="Values",
            template="plotly_white",
            plot_bgcolor="#272D3A",   # Chart background
            paper_bgcolor="#272D3A",  # Outer background
            font_color="white"  ,      # Text color,
            width=300,    # pixels
            height=350,   # pixels
        )
        st.plotly_chart(fig, use_container_width=True)


# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [100, 150, 200, 180, 220, 250],
    'Profit': [40, 60, 80, 70, 100, 120],
    'Forecast': [90, 140, 190, 170, 210, 240]  # This will be the area chart
}

with st.container():
    chart_col1, chart_col2, chart_col3= st.columns([1,1,2]) 

    with chart_col1:
        st.markdown('<div><h3>Inpatient Capacity</h23</div>', unsafe_allow_html=True)
        st.markdown("""
            <div style="
                display: grid;
                grid-template-columns: repeat(2, 90px);  /* 2 columns of 90px */
                grid-template-rows: repeat(2, 90px);     /* 2 rows of 90px */
                gap: 10px;                               /* space between tiles */
            ">
                <div class="tile" style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 1</div>
                <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 2</div>
                <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 3</div>
                <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 4</div>
            </div>
            """, unsafe_allow_html=True)
    with chart_col2:  
        st.markdown('<div><h3>Inpatient Flow</h23</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="
            display: grid;
            grid-template-columns: repeat(2, 90px);  /* 2 columns of 90px */
            grid-template-rows: repeat(2, 90px);     /* 2 rows of 90px */
            gap: 10px;                               /* space between tiles */
        ">
            <div class="tile" style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 1</div>
            <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 2</div>
            <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 3</div>
            <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 4</div>
        </div>
        """, unsafe_allow_html=True)

    with chart_col3:
        df = pd.DataFrame(data)

        # Convert to long format
        df_long = df.melt('Month', var_name='Metric', value_name='Value')

        # Create line and area chart separately
        fig = px.line(df_long[df_long['Metric'].isin(['Sales', 'Profit'])],
                    x='Month', y='Value', color='Metric', markers=True)

        # Add area trace manually
        fig.add_scatter(x=df['Month'], y=df['Forecast'], 
                        fill='tozeroy', 
                        mode='none', 
                        name='Forecast', 
                        opacity=0.2)

        fig.update_layout(title="Sales vs Profit with Forecast Area", template="plotly_white" )
        #st.plotly_chart(fig, use_container_width=True)

