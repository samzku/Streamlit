import streamlit as st
import pandas as pd
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder
# --- PAGE CONFIG ---
st.set_page_config(page_title="SALHN Patient CareFlow", layout="wide")

# --- DARK THEME AND STYLING ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {background-color: #232834; color: white;}
.tile {
    padding: 10px;
    border-radius: 5px;
    color: white;
    text-align: center;
    box-shadow: 0px 0px 10px #00000050;
    margin-bottom: 2px;
}
.tile h1 {margin: 0; font-size: 60px;}
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
"""
#MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
"""
# Hide Streamlit default menu and header
hide_streamlit_style = """
    <style>
    
 
    /* Header bar */
    .custom-header {
        background-color: #272D3A; /* Dark header */
        padding: 15px;
        text-align: center;
        color: white;
        font-size: 28px;
        font-weight: bold;
    }

    /* Main content box (Optional if you want a card-like effect) */
    .content-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def tile(title, value, 
         bg="#222", 
         title_color="white", title_size="12px", 
         value_color="white", value_size="32px",
         padding="15px", border_radius="8px"):
    
    st.markdown(f"""
    <div style="
        background:{bg};
        padding:{padding};
        border-radius:{border_radius};
        text-align:center;
    ">
        <div style="font-size:{title_size}; color:{title_color}; opacity:0.8;">{title}</div>
        <div style="font-size:{value_size}; color:{value_color}; font-weight:bold;">{value}</div>
    </div>
    """, unsafe_allow_html=True)

def tile_content(title, value, 
         bg="#222", 
         title_color="white", title_size="16px", 
         value_color="white", value_size="32px",
         padding="10x", border_radius="8px"):
    
    return f'<div style="background:{bg};padding:{padding};border-radius:{border_radius};text-align:center;"> <div style="font-size:{title_size}; color:{title_color}; opacity:0.8;">{title}</div> <div style="font-size:{value_size}; color:{value_color}; font-weight:bold;">{value}</div>  </div>'
# --- HEADER ---

# Centered page title

st.markdown("""<h1 style='text-align: center; color: white; margin-top: 0;'>SALHN Patient Careflow Board</h1>""", unsafe_allow_html=True)

# --- TOP OVERVIEW SECTION ---
col1, col2, col3 = st.columns((1, 3, 2), gap='medium')

# --- BIG KPI ON LEFT ---
with col1:
    tile("Flow Health", "85", bg="#3E475C", value_color="#4CAF50", value_size="45px")
    #st.markdown('<div style="box-shadow: 0px 0px 10px #00000050;display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;">Overall Completion %<h2 style="color:green">85</h></div>', unsafe_allow_html=True)

# --- TABLE IN THE MIDDLE ---
with col2:
    #st.markdown('<div class="summary-table"><h2>Ward Occupancy</h2></div>', unsafe_allow_html=True)
    # Example table
    df_table = pd.DataFrame({
        "Division": ["MCCC", "3GOF", "4A", "4D"],
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
    for col in df_table.columns:
        gb.configure_column(col, width=80)
    # Set fixed width for columns
    gb.configure_column("Division", width=120)        # pixels
    gb.configure_column("Physical", width=100)
    gb.configure_column("Flex", width=100)
    #gb.configure_columns(["Division"], cellStyle={'color': 'white', 'backgroundColor': '#333'})
    grid_options = gb.build()
    st.markdown("""
<div style="
    background-color:#3E475C; 
    color:white; 
    padding:10px; 
    border-radius:8px;
    text-align:center;
    font-weight:bold;
    font-size:18px;
">
    Ward Occupancy & Capacity
</div>
""", unsafe_allow_html=True)
    AgGrid(df_table, gridOptions=grid_options, height=100)
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
        grid-template-columns: repeat(2, 70px);  /* 2 columns of 70px */
        grid-template-rows: repeat(2, 70px);     /* 2 rows of 70px */
        gap: 10px;                               /* space between tiles */
    ">
        {tile_content("Critical","7", bg="#3E475C", value_color="#D94446", value_size="30px")}
        {tile_content("Medium","8", bg="#3E475C", value_color="#FFCE1B", value_size="30px")}
        {tile_content("High","1", bg="#3E475C", value_color="#FF7518", value_size="30px")}
        {tile_content("Normal","16", bg="#3E475C", value_color="#3CAE63", value_size="30px")}
    </div>
    """, unsafe_allow_html=True)
# --- CHARTS BELOW ---

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [100, 150, 200, 180, 220, 250],
    'Profit': [40, 60, 80, 70, 100, 120]
}

df = pd.DataFrame(data)

chart_col1, chart_col2 = st.columns([2,2]) 

with chart_col1:
    st.markdown('<div><h3>Emergency Department</h23</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="
        display: grid;
        grid-template-columns: repeat(8, 90px);  /* 4 columns of 70px */
        grid-template-rows: repeat(2, 90px);     /* 2 rows of 70px */
        gap: 10px;                               /* space between tiles */  
    ">
        {tile_content("#Amb on Ramp","14", bg="#FFCE1B", value_color="#FFFAFA", value_size="20",title_size="12px")}
        <div style='display:flex; background-color: #2ca02c;align-items:center; justify-content:center; border-radius:8px;'>Tile 2</div>
        <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 3</div>
        <div style='display:flex; background-color: #d62728;align-items:center; justify-content:center; border-radius:8px;'>Tile 4</div>
        <div style='display:flex; background-color: #ff7f0e;align-items:center; justify-content:center; border-radius:8px;'>Tile 1</div>
        <div style='display:flex; background-color: #2ca02c;align-items:center; justify-content:center; border-radius:8px;'>Tile 2</div>
        <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 3</div>
        <div style='display:flex; background-color: #d62728;align-items:center; justify-content:center; border-radius:8px;'>Tile 4</div>
        <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 1</div>
        <div style='display:flex; background-color: #2ca02c;align-items:center; justify-content:center; border-radius:8px;'>Tile 2</div>
        <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 3</div>
        <div style='display:flex; background-color: #d62728;align-items:center; justify-content:center; border-radius:8px;'>Tile 4</div>
        <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 1</div>
        <div style='display:flex; background-color: #2ca02c;align-items:center; justify-content:center; border-radius:8px;'>Tile 2</div>
        <div style='display:flex; background-color: #333333;align-items:center; justify-content:center; border-radius:8px;'>Tile 3</div>
        <div style='display:flex; background-color: #ff7f0e;align-items:center; justify-content:center; border-radius:8px;'>Tile 4</div>
    
    </div>
    """, unsafe_allow_html=True)
    
with chart_col2:
    # Reshape data for Plotly Express
    df_long = df.melt('Month', var_name='Metric', value_name='Value')

    # Create chart
    fig = px.line(df_long, x='Month', y='Value', color='Metric', markers=True, title='Sales vs Profit')
    fig.update_layout(
        width=300,   # Set fixed width
        height=340   # Set fixed height
    )
    st.plotly_chart(fig, use_container_width=True)

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [100, 150, 200, 180, 220, 250],
    'Profit': [40, 60, 80, 70, 100, 120],
    'Forecast': [90, 140, 190, 170, 210, 240]  # This will be the area chart
}

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

    fig.update_layout(title="Sales vs Profit with Forecast Area", template="plotly_white",  width=300,  height=200 )
    st.plotly_chart(fig, use_container_width=True)
