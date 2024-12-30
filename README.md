# xls to vcard - web
## Deployment
You can also access the deployed version of this application at [https://xlstovcard-web.onrender.com/](https://xlstovcard-web.onrender.com/).

## Description
This project provides a web interface to convert Excel files (.xls or .xlsx) containing contact information into vCard (.vcf) files. It allows users to upload an Excel file, specify the columns for names, phone numbers, emails, and groups, and then download the generated vCard file.

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/xls-to-vcard-web.git
    cd xls-to-vcard-web
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and go to `http://localhost:8050`.

3. Follow the instructions on the web interface to upload your Excel file, specify the columns, and download the vCard file.


## Functionalities
- **Upload Excel File**: Users can upload an Excel file containing contact information.
- **Specify Columns**: Users can specify which columns in the Excel file correspond to names, phone numbers, emails, and groups.
- **Generate vCard**: The application generates a vCard file based on the specified columns and allows users to download it.
- **Custom Labels**: Users can provide custom labels for phone numbers and emails.
- **Group Assignment**: Users can assign contacts to different groups.

## License
This project is licensed under the MIT License.
