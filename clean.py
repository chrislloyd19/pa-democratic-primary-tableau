import csv

READ_FILE = 'P00000001-PA.csv'
WRITE_FILE = 'PA-contributions.csv'

DEMS = ["Sanders, Bernard", "Clinton, Hillary Rodham", "O'Malley, Martin Joseph", 
        "Webb, James Henry Jr.",  "Lessig, Lawrence"]

INDIES = ["McMullin, Evan", "Johnson, Gary", "Stein, Jill"]

FIELDS = ['cand_nm','contbr_zip','contbr_employer','contbr_nm',
          'contbr_city','contbr_occupation','contb_receipt_dt',
          'contbr_st','contb_receipt_amt','election_tp']


with open(READ_FILE, 'r') as csv_read:
  reader = csv.DictReader(csv_read)

  with open(WRITE_FILE, 'wb') as csv_write:
    writer = csv.writer(csv_write, delimiter=',')

    writer.writerow(FIELDS)

    for row in reader:
      vals = []
      for field in FIELDS:
        if field == 'contbr_zip':
          vals.append(row[field][0:5])
        else:
          vals.append(row[field])
      writer.writerow(vals)

