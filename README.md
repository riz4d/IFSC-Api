# IFSC Api

Flask Api to retrieve information about a specific bank branch using its IFSC code. This information may include details such as the bank's name, branch name, address, contact information, and more

### Api Homepage

[API Homepage](https://ifsc.rizad.me/)

### Return Data's

- Bank Name.
- Branch Name.
- City.
- District
- State
- Contact Number.
- Address.
- MICR.
- etc..

## API Endpoint

#### Request
- Method: GET
- URL: `http://ifsc.rizad.me/?ifsc=<ifsc_code>`

Replace `<ifsc_code>` with the desired IFSC code.

#### Response

Example Response:
```json
{
"MICR":"123456678",
"BRANCH":"Example Branch",
"ADDRESS":"123 Main Street, City",
"STATE":"Example State",
"CONTACT":"+1234567890",
"UPI":true,
"RTGS":true,
"CITY":"Example City",
"CENTRE":"Example Centre",
"DISTRICT":"Example District",
"NEFT":true,
"IMPS":true,
"SWIFT":null,
"ISO3166":"IN-KL",
"BANK":"Example Bank",
"BANKCODE":"ABC",
"IFSC":"ABCD0123456"
}
```
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/riz4d/IFSC-Api
   cd IFSC-Api
   ```
   
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

   ```bash
   python3 app.py
   ```

5. Access the api in your browser at `http://127.0.0.1/?ifsc=<ifsc-code>`.


### License

This project is licensed under the [MIT License](LICENSE).

