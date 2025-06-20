import streamlit as st

# App title
st.set_page_config(page_title="How-To Reference App", page_icon="📘")
st.title("📘 How-To Reference Lookup Tool")

st.markdown("Use the dropdowns below to find internal task guidance based on commonly used tools and workflows.")

# Data dictionary structured by category and task
how_to_data = {
    "ArcMap (GIS)": {
        "Get Watershed Shapefiles": [
            "- Go to NJDEP GIS folder",
            "- Navigate to Watershed directory"
        ],
        "Look for HUC14 shapefiles": [
            "- Page 1: “watershed layers are stored…”"
        ],
        "Convert DWG to Shapefile": [
            "- Open ArcMap",
            "- Use 'CAD to Geodatabase' or 'Feature Class to Shapefile' tool",
            "- Define output location",
            "- Page 1: “feature class tool is located…”"
        ],
        "Load NJ 2020 Natural Imagery": [
            "- Open ArcCatalog",
            "- Add GIS Server > WMS"
        ],
        "Use NJOGIS WMS URL": [
            "- Page 1: “use NJOIT imagery service…”"
        ],
        "Have NJ Natural Map 2020": [
            "- Add NJOIT WMS connection"
        ]
    },
    "InRoads": {
        "Open RWK File": [
            "- Launch InRoads",
            "- Go to Surface > Elevation > Preferences",
            "- Load HNTB-EX style",
            "- Page 1: “preferences should be set to…”"
        ],
        "Open DTM and View Spot Elevations": [
            "- File > Open DTM",
            "- Surface > View > Single Point",
            "- Click surface to view spot elevations",
            "- Page 1: “single point tool allows…”"
        ],
        "Open DTM to View Spot and Elevations": [
            "- View > Single Point",
            "- Load DTM and Surface"
        ]
    },
    "MicroStation": {
        "Adjust Line Weights in X-Sections": [
            "- Open Preferences (Workspace > Preferences)",
            "- Under View Options, change Line Weights to 2:1",
            "- Reopen X-sections to view changes",
            "- Page 1: “line weights appear better with…”"
        ],
        "Line Weights in X-Sections": [
            "- Check Line Style Settings",
            "- Reopen Cross Section Views"
        ]
    },
    "NJDOT Tools & Project Info": {
        "Review Inlet Types": [
            "- A: Curb Only, B: Grate Only, D1/D2: Combo Inlets",
            "- Refer to flash cards for spacing/head loss",
            "- Page 1: “inlet types defined…”"
        ],
        "Find DOT Numbers for PM Projects": [
            "- Open PM Portal",
            "- Use 'Project Lookup' tool",
            "- Filter by location, district, or type",
            "- Page 1: “DOT numbers are listed under…”"
        ],
        "See Project Budget": [
            "- Go to eBuilder or project site",
            "- Open 'Financials' tab",
            "- View total budget",
            "- Page 1: “total budget is shown in…”"
        ],
        "View Data Query Sheet": [
            "- Open Excel Tool",
            "- Click Data > Refresh All",
            "- Print/export query page",
            "- Page 1: “data refresh will populate…”"
        ],
        "See How Much Budget in Project": [
            "- Navigate to Financial tab",
            "- Page 1: “project funding amounts…”"
        ]
    },
    "Other Tasks": {
        "Submit an IT Request": [
            "- Open IT Portal",
            "- Select Issue Category",
            "- Page 1: “submit by selecting equipment type…”"
        ],
        "Book Desk in Another Office": [
            "- Go to FlexWork system",
            "- Select building and desk",
            "- Submit confirmation",
            "- Page 1: “select from dropdown menu…”"
        ],
        "Fix Invisible Program Window": [
            "- Use Alt+Tab to focus",
            "- Use Windows+Arrow Keys to move to screen",
            "- Page 1: “invisible windows happen when…”"
        ],
        "Query Data for Print View": [
            "- Open Excel tool",
            "- Refresh and print",
            "- Page 1: “query print page found under…”"
        ]
    }
}

# Dropdown selectors
category = st.selectbox("Select Category", options=list(how_to_data.keys()))
task = st.selectbox("Select Task", options=list(how_to_data[category].keys()))

# Output the instructions
st.markdown("### Instructions")
for step in how_to_data[category][task]:
    st.markdown(f"- {step}")

