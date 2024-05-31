import streamlit as st
import pandas as pd
import time

def display_selected_columns(df, selected_columns, sort_orders):
    """Displays the user-selected columns from the uploaded DataFrame with chosen sort orders.

    Args:
        df (pd.DataFrame): The uploaded DataFrame containing the data.
        selected_columns (list): A list of column names selected by the user.
        sort_orders (dict): A dictionary mapping column names to their sort orders (ascending or descending).
    """

    if selected_columns:
        sorted_df = df[selected_columns].copy()  # Avoid modifying original DataFrame
        for col, order in sort_orders.items():
            if order == "Ascending":
                sorted_df.sort_values(col, inplace=True, ascending=True)
            elif order == "Descending":
                sorted_df.sort_values(col, inplace=True, ascending=False)
            else:
                st.warning(f"Invalid sort order for '{col}': {order}")
        st.dataframe(sorted_df)
    else:
        st.warning("Please select at least one column to display.")

def show_progress_bar(uploaded_file):
    """Displays a progress bar while the file is uploading."""
    if uploaded_file is not None:
        progress_bar = st.progress(0)
        last_progress = 0
        while not uploaded_file.is_uploaded:
            # Simulate progress for demonstration purposes (replace with actual file size tracking)
            progress = min(100, last_progress + 10)
            progress_bar.progress(progress)
            last_progress = progress
            time.sleep(0.1)  # Add a small delay to reduce CPU usage
        progress_bar.empty()  # Clear the progress bar after upload

def main():
    """Main function to handle file upload, column selection, and sorting."""


    st.set_page_config(page_title="Column Selector App with Sorting")
    st.title("Excel Column Explorer Application")

    # File upload widget with progress bar
    uploaded_file = st.file_uploader("Please Upload Excel File:", type="xlsx")
    show_progress_bar(uploaded_file)

    if uploaded_file is not None:
        try:
          
            df = pd.read_excel(uploaded_file)

          
            column_names = df.columns.tolist()

      
            selected_columns = st.multiselect("Select Columns to Display:", options=column_names, default=column_names)

    
            sort_orders = {col: "Ascending" for col in selected_columns}

   
            for col in selected_columns:
                sort_option = st.radio(f"Sort Order for '{col}'", ("Ascending", "Descending"), key=col)
                sort_orders[col] = sort_option

    
            display_selected_columns(df, selected_columns, sort_orders)

        except Exception as e:
            st.error(f"Error reading the file: {e}")

main()
