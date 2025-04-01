
import matplotlib.pyplot as py
import tkinter as tk
import tkinter.font as tkfont

py.rcParams['font.sans-serif'] = ['Microsoft JhengHei']

class Calculator(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        f1 = tkfont.Font(size = 24)

        # Get sold price
        def on_entry_click_selprice(event):
            if self.sel_price.get() == "Enter sold price (in thousands)":
                self.sel_price.delete(0, "end")
                self.sel_price.config(fg='black')
        def on_focus_out_selprice(event):
            if self.sel_price.get() == "":
                self.sel_price.insert(0, "Enter sold price (in thousands)")
                self.sel_price.config(fg='grey')
        
        # Get the time period of holding the property
        def on_entry_click_selperiod(event):
            if self.sel_period.get() == "Enter holding period (in months)":
                self.sel_period.delete(0, "end")
                self.sel_period.config(fg='black')
        def on_focus_out_selperiod(event):
            if self.sel_period.get() == "":
                self.sel_period.insert(0, "Enter holding period (in months)")
                self.sel_period.config(fg='grey')

        # Get the purchased price
        def on_entry_click_purc_price(event):
            if self.purc_price.get() == "Enter purchased price (in thousands)":
                self.purc_price.delete(0, "end")
                self.purc_price.config(fg='black')
        def on_focus_out_purc_price(event):
            if self.purc_price.get() == "":
                self.purc_price.insert(0, "Enter purchased price (in thousands)")
                self.purc_price.config(fg='grey')

        # Get monthly miscellaneous expense
        def on_entry_click_mcl_exp(event):
            if self.mcl_exp.get() == "Enter monthly miscellaneous expense":
                self.mcl_exp.delete(0, "end")
                self.mcl_exp.config(fg='black')
        def on_focus_out_mcl_exp(event):
            if self.mcl_exp.get() == "":
                self.mcl_exp.insert(0, "Enter monthly miscellaneous expense")
                self.mcl_exp.config(fg='grey')
        
        # Get outstanding principal 
        def on_entry_click_out_prin(event):
            if self.out_prin.get() == "Enter outstanding principal (in thousands)":
                self.out_prin.delete(0, "end")
                self.out_prin.config(fg='black')
        def on_focus_out_out_prin(event):
            if self.out_prin.get() == "":
                self.out_prin.insert(0, "Enter outstanding principal (in thousands)")
                self.out_prin.config(fg='grey')

        # Get number of installments left
        def on_entry_click_loan_period(event):
            if self.loan_period.get() == "Enter the number of installments on the loan":
                self.loan_period.delete(0, "end")
                self.loan_period.config(fg='black')
        def on_focus_out_loan_period(event):
            if self.loan_period.get() == "":
                self.loan_period.insert(0, "Enter the number of installments on the loan")
                self.loan_period.config(fg='grey')

        # Get interest rate
        def on_entry_click_int_rate(event):
            if self.int_rate.get() == "Enter annual interest rate (in percentage %)":
                self.int_rate.delete(0, "end")
                self.int_rate.config(fg='black')
        def on_focus_out_int_rate(event):
            if self.int_rate.get() == "":
                self.int_rate.insert(0, "Enter annual interest rate (in percentage %)")
                self.int_rate.config(fg='grey')


        self.sel_price = tk.Entry (self, width = 50, font = f1)
        self.sel_price.insert(0, 'Enter sold price (in thousands)')
        self.sel_price.config(fg='grey')
        self.sel_price.bind("<FocusIn>", on_entry_click_selprice)
        self.sel_price.bind("<FocusOut>", on_focus_out_selprice)

        self.sel_period = tk.Entry (self, width = 50, font = f1)
        self.sel_period.insert(0, 'Enter holding period (in months)')
        self.sel_period.config(fg='grey')
        self.sel_period.bind("<FocusIn>", on_entry_click_selperiod)
        self.sel_period.bind("<FocusOut>", on_focus_out_selperiod)

        self.purc_price = tk.Entry (self, width = 50, font = f1)
        self.purc_price.insert(0, 'Enter purchased price (in thousands)')
        self.purc_price.config(fg='grey')
        self.purc_price.bind("<FocusIn>", on_entry_click_purc_price)
        self.purc_price.bind("<FocusOut>", on_focus_out_purc_price)

        self.mcl_exp = tk.Entry (self, width = 50, font = f1)
        self.mcl_exp.insert(0, 'Enter monthly miscellaneous expense')
        self.mcl_exp.config(fg='grey')
        self.mcl_exp.bind("<FocusIn>", on_entry_click_mcl_exp)
        self.mcl_exp.bind("<FocusOut>", on_focus_out_mcl_exp)

        self.out_prin = tk.Entry (self, width = 50, font = f1)
        self.out_prin.insert(0, 'Enter outstanding principal (in thousands)')
        self.out_prin.config(fg='grey')
        self.out_prin.bind("<FocusIn>", on_entry_click_out_prin)
        self.out_prin.bind("<FocusOut>", on_focus_out_out_prin)

        self.loan_period = tk.Entry (self, width = 50, font = f1)
        self.loan_period.insert(0, 'Enter the number of installments on the loan')
        self.loan_period.config(fg='grey')
        self.loan_period.bind("<FocusIn>", on_entry_click_loan_period)
        self.loan_period.bind("<FocusOut>", on_focus_out_loan_period)

        self.int_rate = tk.Entry (self, width = 50, font = f1)
        self.int_rate.insert(0, 'Enter annual interest rate (in percentage %)')
        self.int_rate.config(fg='grey')
        self.int_rate.bind("<FocusIn>", on_entry_click_int_rate)
        self.int_rate.bind("<FocusOut>", on_focus_out_int_rate)

        # Create the layout of the calculator
        self.btn = tk.Button (self, text = "Calculate !", command = self.net_ern, width = 30, font = f1)
        self.erng = tk.Label(self, text = 'Net Earning =', width = 30, font = f1)
        self.ern_ROI = tk.Label(self, text = 'ROI =', width = 30, font = f1)
        self.sel_price.grid(row = 3, column = 0)
        self.sel_period.grid(row = 1, column = 0)
        self.purc_price.grid(row = 0, column = 0)
        self.mcl_exp.grid(row = 2, column = 0)
        self.out_prin.grid(row = 4, column = 0)
        self.loan_period.grid(row = 5, column = 0)
        self.int_rate.grid(row = 6, column = 0)
        self.btn.grid(row = 7, column = 0)
        self.erng.grid(row = 8, column = 0)
        self.ern_ROI.grid(row = 9, column = 0)


    def net_ern(self):
        try:
            selling_price = float(self.sel_price.get()) * 1000 
            sell_of_month = int(self.sel_period.get())
            purchasing_price = float(self.purc_price.get()) * 1000 
            mcl_exp = float(self.mcl_exp.get()) 
            out_prin = float(self.out_prin.get()) * 1000 
            loan_period = int(self.loan_period.get())
            int_rate = float(self.int_rate.get()) / 100 
            if (selling_price >= 0 and 
                sell_of_month >= 0 and 
                purchasing_price >= 0 and 
                mcl_exp >= 0 and 
                out_prin >= 0 and 
                loan_period >= 0 and 
                int_rate >= 0):
                pass
            else:
                raise ValueError("All inputs must be positive numbers or zero.")
        except ValueError as er:
            if "could not convert" in str(er):
                self.erng.config(text="Please enter numbers only.", fg = 'red')
            else:
                self.erng.config(text=str(er), fg = 'red')
        
            self.ern_ROI.config(text='')
            return
        
        # mortgage calculation
        int_rate_monthly = int_rate/12
        PMT = out_prin * ((int_rate_monthly) / (1 - (1 / (1 + int_rate_monthly) ** loan_period)))
        interest_premium = 0

        # Initialize Remaining Principal
        remaining_principal = out_prin
        interest_premium = 0

        # Determine tax rate based on holding period
        if sell_of_month < 24:
            tax_rate = 0.45
        elif 24 <= sell_of_month < 60:
            tax_rate = 0.35
        elif 60 <= sell_of_month < 120:
            tax_rate = 0.20
        else:
            tax_rate = 0.10

        # Calculate total interest paid over the holding period
        for x in range(sell_of_month + 1):  
            if x == 0:  
                # If sold in the first month, assume no interest premium 
                monthly_int_premium = 0  
            else:
                # Interest portion of the monthly payment
                monthly_int_premium = remaining_principal * int_rate_monthly
                
                # Add to total interest paid
                interest_premium += monthly_int_premium
                
                # Reduce the remaining balance by the principal part of the payment
                principal_payment = PMT - monthly_int_premium
                remaining_principal -= principal_payment

        # Calculate expenses
        monthly_expense_total = mcl_exp * sell_of_month
        tax_expense = (selling_price - purchasing_price) * tax_rate 
        total_cost = purchasing_price + monthly_expense_total + interest_premium + tax_expense

        # Final net earnings and ROI
        net_erng = selling_price - total_cost
        net_ern_ROI = (selling_price / total_cost) - 1

        # Format output
        net_erng = '{:,.2f}'.format(net_erng)
        net_ern_ROI = "{:.2%}".format(net_ern_ROI)

        self.erng.config(text='Net Earning = ' + net_erng, fg="black")
        self.ern_ROI.config(text='ROI = ' + net_ern_ROI)
       
        

cal = Calculator()
cal.master.title('Taiwan Real Estate Investing Income Calculator')
cal.mainloop()