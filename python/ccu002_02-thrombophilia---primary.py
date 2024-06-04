# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"441079006","system":"snomedct"},{"code":"441946009","system":"snomedct"},{"code":"441990004","system":"snomedct"},{"code":"441945008","system":"snomedct"},{"code":"441762006","system":"snomedct"},{"code":"442078001","system":"snomedct"},{"code":"441697004","system":"snomedct"},{"code":"441882000","system":"snomedct"},{"code":"D68.6","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-thrombophilia-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-thrombophilia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-thrombophilia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-thrombophilia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
