from fpdf import FPDF

travel_code = "128"
travel_description="Annual Meetup at Bhuj"
trip_type="Domestic"
emp_code="TU002"
design_code="test data"
company_code = "test data1"
cc_code="100505"
start_date="2023-04-11"
end_date="2023-04-13"
purpose = "Annual Meet"
comment = "test data"
advance_amount="5000"
currency_code="101"
advance_purpose="test dat"
advance_comment ="test data"
hodapprovel="test data"
hod_comment="test data"
account_approvel="test data"
account_comment="test data"
status="test data"
currency_name="INR"

TABLE_DATA = (
    ("travel_code", travel_code),
    ("travel_description", travel_description),
    ("trip_type", trip_type),
    ("emp_code", emp_code),
    ("design_code", design_code),
    ("company_code", company_code),
    ("cc_code", cc_code),
    ("start_date", start_date),
    ("end_date", end_date),
    ("purpose", purpose),
    ("comment", comment),
    ("advance_amount", advance_amount),
    ("currency_code", currency_code),
    ("advance_purpose", advance_purpose),
    ("advance_comment", advance_comment),
    ("hodapprovel", hodapprovel),
    ("hod_comment", hod_comment),
    ("account_approvel", account_approvel),
    ("account_comment", account_comment),
    ("status", status),
    ("currency_name", currency_name)
)


strat_date = "Flight_Data"
end_date="Flight_Data"
from_city="Flight_Data"
to_city="Flight_Data"
remark="test Flight_Data"

Flight_Data = (
    ("strat_date", strat_date),
    ("end_date", end_date),
    ("from_city", from_city),
    ("to_city", to_city),
    ("remark", remark)
)


strat_date = "Train_Data"
id_card="Annual Train_Data"
from_city="Train_Data"
to_city="Train_Data"
remark="test Train_Data"
age="Train_Data"
gender="test Train_Data"

Train_Data = (
    ("strat_date", strat_date),
    ("id_card", id_card),
    ("from_city", from_city),
    ("to_city", to_city),
    ("remark", remark),
    ("age", age),
    ("gender", gender)
)


strat_date = "Bus_Data"
id_card="Annual Bus_Data"
from_city="Bus_Data"
to_city="Bus_Data"
remark="test Bus_Data"
age="Bus_Data"
gender="test Bus_Data"

Bus_Data = (
    ("strat_date", strat_date),
    ("id_card", id_card),
    ("from_city", from_city),
    ("to_city", to_city),
    ("remark", remark),
    ("age", age),
    ("gender", gender)
)


strat_date = "Car_Data"
end_date="Annual Car_Data"
from_city="Car_Data"
to_city="Car_Data"
remark="test Car_Data"

Car_Data = (
    ("strat_date", strat_date),
    ("id_card", id_card),
    ("from_city", from_city),
    ("to_city", to_city),
    ("remark", remark)
)

check_in = "Hotel_Data"
check_out="Annual Hotel_Data"
city="Hotel_Data"
remark="test Hotel_Data"

Hotel_Data = (
    ("check_in", check_in),
    ("check_out", check_out),
    ("city", city),
    ("remark", remark)
)


pdf = FPDF()
pdf.add_page()
pdf.set_font("Times","B", size=16)

pdf.write(0, 'Trip Details')
pdf.ln()
with pdf.table() as table:
    for data_row in TABLE_DATA:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.cell(600, 40, '\n')   
pdf.write(0, 'Flight Details')
pdf.ln()

with pdf.table() as table:
    for data_row in Flight_Data:
        row = table.row()
        for datum in data_row:
            row.cell(datum) 
            
            
pdf.ln()
pdf.write(0, 'Train Details')
pdf.ln()

with pdf.table() as table:
    for data_row in Train_Data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.ln()
pdf.write(0, 'Bus Details')
pdf.ln()
with pdf.table() as table:
    for data_row in Bus_Data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.ln() 
pdf.write(0, 'Car Details')
pdf.ln()
with pdf.table() as table:
    for data_row in Car_Data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.ln() 
pdf.write(0, 'Hotel Details')
pdf.ln()
with pdf.table() as table:
    for data_row in Hotel_Data:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output('table.pdf')