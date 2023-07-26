import csv
import re

try:
    with open('/Users/charlesbryan/Desktop/Python_Repo/TriumphPay/BillingReport2.csv', 'r', newline='') as BillingReport:
        reader = csv.reader(BillingReport)
        Invoice_Dict = {}
        Payees = set()

        for Invoice in reader:
            Uploaded_Date, Approved_Date, Terms, Carrier, MC_Number, DOT_Number, Reference_Number, Carrier_Invoice_Number, Net_Amount_Due, Pay_By, Payment_Status, Invoice_Key, Payee_Key, Invoice_Draft_Id, Applied_To_Key = Invoice
            Invoice_Dict[Invoice_Key] = [Uploaded_Date, Approved_Date, Terms, Carrier, MC_Number, DOT_Number, Reference_Number, Net_Amount_Due, Pay_By, Payment_Status, Invoice_Key, Payee_Key, Invoice_Draft_Id, Applied_To_Key]
            Payees.add(Payee_Key)
            
    def get_invoice(Invoice_Key, Invoice_Dict):
        return Invoice_Dict[Invoice_Key]

    def print_all_payees(Payees):
        for payee in Payees:
            print(payee)
        return None

    def get_invoices_per_payee(Payees, Invoice_Dict):
        payee_invoices = {}
        for payee in Payees:
            
            iterable = (x for x in Invoice_Dict.values())
            for invoice_data in iterable:
                payee_key = invoice_data[11]
                if payee_key == payee:
                    invoice_key = invoice_data[10]
                    if payee not in payee_invoices:
                        payee_invoices[payee] = [invoice_key]
                    else:
                        payee_invoices[payee].append(invoice_key)
        return payee_invoices
    
    def get_all_checks(Invoice_Dict):
        check_list = []
        iterable = (x for x in Invoice_Dict.items())
        for invoice_key, invoice_data in iterable:
            Pay_By = invoice_data[8]
            pattern = r'Check'
            match = re.search(pattern, Pay_By)
            if match:
                check_list.append(invoice_key)
        return check_list
    
    def get_all_ACH(Invoice_Dict):
        ACH_list = []
        iterable = (x for x in Invoice_Dict.items())
        for invoice_key, invoice_data in iterable:
            Pay_By = invoice_data[8]
            pattern = r'ACH'
            match = re.search(pattern, Pay_By)
            if match:
                ACH_list.append(invoice_key)
        return ACH_list
    
    def create_factor_name(Pay_By):
        factor = ''
        char_count = 0
        for char in Pay_By:
            char_count += 1
            if char_count <= 7:
                continue
            factor += char
        return factor
        
    def get_all_factors(Invoice_Dict):
        factors = set()
        iterable = (x for x in Invoice_Dict.items())
        for invoice_key, invoice_data in iterable:
            Pay_By = invoice_data[8]
            match_pattern = r'ACH to'
            match = re.search(match_pattern, Pay_By)
            if match:
                factor = create_factor_name(Pay_By)
                factors.add(factor)
        return factors        

    def get_amount(invoice_data):
        amount = ''
        invalid_char = ['$', ' ', ',', '.']
        iterable = (x for x in invoice_data[7])
        for char in iterable:
            if char not in invalid_char:
                amount += char
        return amount
    
    def get_factor_payouts(Invoice_Dict):
        payouts = {}
        factors = get_all_factors(Invoice_Dict)
        for factor in factors:
            payouts[factor] = 0
        iterable = (x for x in Invoice_Dict.values())
        for invoice_data in iterable:
            Pay_By = invoice_data[8]
            factor = create_factor_name(Pay_By)
            if factor in payouts:
                payouts[factor] = int(get_amount(invoice_data))
        return payouts
    
    def get_min_factor_payout(Invoice_Dict):
        min_payout = float('inf')
        iterable = (x for x in get_factor_payouts(Invoice_Dict).values())
        for amount in iterable:
            if amount < min_payout:
                min_payout = amount
        return min_payout
    
    def get_max_factor_payout(Invoice_Dict):
        max_payout = float('-inf')
        iterable = (x for x in get_factor_payouts(Invoice_Dict).values())
        for amount in iterable:
            if amount > max_payout:
                max_payout = amount
        return max_payout
    
    
            
    # script
    # print(get_invoice("a134P00000GaC9AQAV", Invoice_Dict))
    print(get_invoices_per_payee(Payees, Invoice_Dict))
    print()
    print(get_all_checks(Invoice_Dict))
    print()
    print(get_all_ACH(Invoice_Dict))
    print()
    print(get_all_factors(Invoice_Dict))
    print()
    print(get_factor_payouts(Invoice_Dict))
    print()
    print(f'Min Factor Payout: {get_min_factor_payout(Invoice_Dict)}')
    print()
    print(f'Max Factor Payout: {get_max_factor_payout(Invoice_Dict)}')
    print()

except FileNotFoundError:
    print('The file name you specified does not exist')
finally:
    print()