import csv
import re
import pandas as pd


def match_carriers(file_path_1, file_path_2):
    carriers_dict_1 = create_carrier_dict(file_path_1)
    carriers_dict_2 = create_cat_carrier_dict(file_path_2)
    match_carriers_dict = {}

    for carrier1_scac, carrier1_data in carriers_dict_1.items():
        if carrier1_scac == 'SCAC':
            continue
        carrier2_data = carriers_dict_2.get(carrier1_scac)
        if carrier2_data:
            print(carrier1_scac)
            print(carrier1_data[0])
            print(carrier1_scac)
            print(carrier2_data[0])
            match_carriers_dict[carrier1_scac] = (carrier1_data[0], carrier2_data[0])
        print()

    for scac, match_data in match_carriers_dict.items():
        print(scac)
        print(match_data)
        print()

    return match_carriers_dict


def create_carrier_dict(file_path):
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            carriers_dict = {}
            for Carrier in reader:
                # Unpack all the fields from the row
                (ExternalPayeeKey, CompanyName, MCNumber, DOTNumber, SCAC, Addr1, Addr2, City, 
                 State, PostalCode, Country, PhoneNumber, PrimaryEmail, RemitName, RemitAddr1, 
                 RemitAddr2, RemitCity, RemitState, RemitPostalCode, RemitCountry) = Carrier

                # Add the carrier to the dictionary, keyed by SCAC code
                carriers_dict[SCAC] = [ExternalPayeeKey, CompanyName, MCNumber, DOTNumber, 
                                          SCAC, Addr1, Addr2, City, State, PostalCode, 
                                          Country, PhoneNumber, PrimaryEmail, RemitName, 
                                          RemitAddr1, RemitAddr2, RemitCity, RemitState, 
                                          RemitPostalCode, RemitCountry]

            print(f"{len(carriers_dict)} carriers loaded.")
    except FileNotFoundError:
        print('The file name you specified does not exist')
    finally:
        print("Operation completed.")
    return carriers_dict


def create_cat_carrier_dict(file_path):
    try:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            # Attempt to get the header row to count the number of columns
            header = next(reader)
            num_columns = len(header)
            print(f"Detected {num_columns} columns.")

            carriers_dict = {}
            for Carrier in reader:
                # Check if the current row has the same number of elements as the header
                if len(Carrier) != num_columns:
                    print(f"Row has an unexpected number of values: {Carrier}")
                    continue

                CompanyName = Carrier[0]
                DOTNumber = Carrier[1]
                MCNumber = Carrier[2]
                SCAC = Carrier[3]
                MM_code = Carrier[4]

                carriers_dict[SCAC] = [MM_code, CompanyName, MCNumber, DOTNumber]

            print(f"{len(carriers_dict)} carriers loaded.")

    except FileNotFoundError:
        print('The file name you specified does not exist')
    except StopIteration:
        print('CSV file is empty or the header is missing.')
    finally:
        print("Operation completed.")

    return carriers_dict


def write_matches_to_csv(match_carriers_dict, output_file_path):
    with open(output_file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['SCAC', 'OldExternalPayeeKey', 'NewExternalPayeeKey'])

        for scac, match_data in match_carriers_dict.items():
            print(f'{scac, match_data[0], match_data[1]}')
            writer.writerow([scac, match_data[0], match_data[1]])


file_path_1 = '/Users/charlesbryan/Documents/Python_Repo/TriumphPay/cat_carriers_1.csv'
file_path_2 = '/Users/charlesbryan/Documents/Python_Repo/TriumphPay/cat_carriers_2.csv'
match_carriers_dict = match_carriers(file_path_1, file_path_2)

output_file_path = 'cat_matched_carriers.csv'
write_matches_to_csv(match_carriers_dict, output_file_path)
