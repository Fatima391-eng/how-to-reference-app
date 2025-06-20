import streamlit as st

# How-To categories and tasks
how_to_data = {
    "ArcMap (GIS)": {
        "Get Watershed Shapefiles": [
            "- Go to NJDEP GIS folder",
            "- Navigate to Watershed directory",
            "- Look for HUC14 shapefiles (Page 1) “watershed layers are stored...”"
        ],
        "Convert DWG to Shapefile": [
            "- Open ArcMap",
            "- Use 'CAD to Geodatabase' or 'Feature Class to Shapefile' tool",
            "- Define output location (Page 1) “feature class tool is located...”"
        ],
        "Load NJ 2020 Natural Imagery": [
            "- Open ArcCatalog",
            "- Add GIS Server > WMS",
            "- Use NJOGIS WMS URL (Page 1) “use NJOIT imagery service...”"
        ]
    },
    "InRoads": {
        "Open RWK File": [
            "- Launch InRoads",
            "- Go to Surface > Elevation > Preferences",
            "- Load HNTB-EX style (Page 1) “preferences should be set to...”"
        ],
        "Open DTM and View Spot Elevations": [
            "- File > Open DTM",
            "- Surface > View > Single Point",
            "- Click surface to view spot elevations (Page 1) “single point tool allows...”"
        ]
    },
    "MicroStation": {
        "Adjust Line Weights in X-Sections": [
            "- Open Preferences (Workspace > Preferences)",
            "- Under View Options, change Line Weights to 2:1",
            "- Reopen X-sections to view changes (Page 1) “line weights appear better with...”"
        ]
    },
    "NJDOT Tools & Project Info": {
        "Review Inlet Types": [
            "- A: Curb Only, B: Grate Only, D1/D2: Combo Inlets",
            "- Refer to flash cards for spacing/head loss (Page 1) “inlet types defined...”"
        ],
        "Find DOT Numbers for PM Projects": [
            "- Open PM Portal",
            "- Use 'Project Lookup' tool",
            "- Filter by location, district, or type (Page 1) “DOT numbers are listed under...”"
        ],
        "See Project Budget": [
            "- Go to eBuilder or project site",
            "- Open 'Financials' tab",
            "- View total budget (Page 1) “total budget is shown in...”"
        ],
        "View Data Query Sheet": [
            "- Open Excel template",
            "- Click Data > Refresh All",
            "- Print/export query page (Page 1) “query sheet auto-updates...”"
        ]
    },
    "IT & Software Help": {
        "Open Program from Taskbar if Not Visible": [
            "- Hold Shift + Right-click on taskbar icon",
            "- Select 'Move' > use arrow keys to reposition (Page 1) “move restores off-screen apps...”"
        ],
        "Submit IT Request": [
            "- Go to IT Service Portal",
            "- Fill in 'Submit New Request'",
            "- Confirm category and submit (Page 1) “ticket is logged in ITSM...”"
        ]
    },
    "Space & Scheduling": {
        "Book a Desk in Another Office": [
            "- Log in to reservation system",
            "- Filter by office and date",
            "- Select desk and time (Page 1) “desk reservation system shows...”"
        ]
    }
}

# Streamlit page setup
st.set_page_config("How-To Reference App", page_icon="📋")
st.title("📋 Internal How-To Reference App")

# Dropdowns
category = st.selectbox("Select Task Category", list(how_to_data.keys()))
task = st.selectbox("Select a Task", list(how_to_data[category].keys()))
steps = how_to_data[category][task]

# Display results
st.subheader(f"📌 Steps for: {task}")
st.text_area("Instructions", "\n".join(steps), height=200, disabled=True)

st.markdown("---")
st.caption("All references are based on page numbers and quote starters for CTRL+F lookup.")
