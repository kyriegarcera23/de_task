tmo_all_loans = {
    'id':'INT',
    'ach':'INT',
    'hold':'INT',
    'account':'BIGINT',
    'borrower_name':'VARCHAR(50)',
    'by_last_name':'VARCHAR(50)',
    'first_name':'VARCHAR(25)',
    'mi':'VARCHAR(5)',
    'last_name':'VARCHAR(25)',
    'interest_paid_to':'DATE',
    'payment_due_date':'DATE',
    'payment_frequency':'VARCHAR(25)',
    'regular_payment':'DOUBLE',
    'apply_to_p_i':'DOUBLE',
    'apply_to_reserve':'DOUBLE',
    'apply_to_impound':'DOUBLE',
    'apply_to_other':'DOUBLE',
    'maturity_date':'DATE',
    'term_left':'INT',
    'days_late':'INT',
    'paid_off_date':'DATE',
    'note_rate':'DOUBLE',
    'sold_rate':'DOUBLE',
    'loan_priority':'DOUBLE',
    'principal_balance':'DOUBLE',
    'trust_balance':'DOUBLE',
    'impound_balance':'DOUBLE',
    'reserve_balance':'DOUBLE',
    'unpaid_late_charges':'DOUBLE',
    'unpaid_charges':'DOUBLE',
    'unpaid_interest':'DOUBLE',
    'street':'VARCHAR(225)',
    'city':'VARCHAR(25)',
    'state':'VARCHAR(5)',
    'zip_code':'INT',
    'home_phone':'VARCHAR(50)',
    'cell_phone':'VARCHAR(50)',
    'tin':'BIGINT',
    'loan_type':'VARCHAR(50)',
    'rate_type':'VARCHAR(25)',
    'email_address':'VARCHAR(50)',
    'aggregate_appraised_value':'INT',
    'closing_date':'DATE',
    'first_payment_date':'DATE',
    'next_revision':'DATE',
    'original_balance':'DOUBLE',
    'unearned_discount':'INT',
    'loan_code':'BIGINT',
    'aggregate_senior_liens':'INT',
    'dob':'DATE',
    'primary_servicing_associate':'VARCHAR(50)',
    'secondary_servicing_associate':'VARCHAR(50)',
    'last_communication_date':'DATE',
    'annual_percentage_rate':'DOUBLE',
    'total_of_payments':'DOUBLE',
    'original_total_loan_amount':'DOUBLE',
    'original_amount_financed':'DOUBLE',
    'original_initial_finance_charges':'DOUBLE',
    'final_total_amount_funded_to_schools':'DOUBLE',
    'modified_1_total_loan_amount':'DOUBLE',
    'modified_1_amount_financed':'DOUBLE',
    'loan_product':'VARCHAR(25)',
    'loan_owner':'VARCHAR(25)',
    'borrower_fico_score':'DOUBLE',
    'borrower_strata_score':'DOUBLE',
    'borrower_dti':'DOUBLE',
    'borrower_total_monthly_income':'DOUBLE',
    'borrower_total_assets':'DOUBLE',
    'borrower_total_liabilities':'DOUBLE',
    'co_borrower_1_full_name':'VARCHAR(50)',
    'co_borrower_1_fico_score':'DOUBLE',
    'co_borrower_1_strata_score':'DOUBLE',
    'co_borrower_1_dti':'DOUBLE',
    'co_borrower_1_total_monthly_income':'DOUBLE',
    'co_borrower_1_total_assets':'DOUBLE',
    'co_borrower_1_total_liabilities':'DOUBLE',
    'co_borrower_2_full_name':'VARCHAR(50)',
    'co_borrower_2_fico_score':'DOUBLE',
    'co_borrower_2_strata_score':'DOUBLE',
    'co_borrower_2_dti':'DOUBLE',
    'co_borrower_2_total_monthly_income':'DOUBLE',
    'co_borrower_2_total_assets':'DOUBLE',
    'co_borrower_2_total_liabilities':'DOUBLE',
    'co_borrower_3_full_name':'VARCHAR(50)',
    'co_borrower_3_fico_score':'DOUBLE',
    'co_borrower_3_strata_score':'DOUBLE',
    'co_borrower_3_dti':'DOUBLE',
    'co_borrower_3_total_monthly_income':'DOUBLE',
    'co_borrower_3_total_assets':'DOUBLE',
    'co_borrower_3_total_liabilities':'DOUBLE',
    'co_signer_1_full_name':'VARCHAR(50)',
    'co_signer_1_fico_score':'DOUBLE',
    'co_signer_1_strata_score':'DOUBLE',
    'co_signer_1_dti':'DOUBLE',
    'co_signer_1_total_monthly_income':'DOUBLE',
    'co_signer_1_total_assets':'DOUBLE',
    'co_signer_1_total_liabilities':'DOUBLE',
    'co_signer_2_full_name':'VARCHAR(50)',
    'co_signer_2_fico_score':'DOUBLE',
    'co_signer_2_strata_score':'DOUBLE',
    'co_signer_2_dti':'DOUBLE',
    'co_signer_2_total_monthly_income':'DOUBLE',
    'co_signer_2_total_assets':'DOUBLE',
    'co_signer_2_total_liabilities':'DOUBLE',
    'co_signer_3_full_name':'VARCHAR(50)',
    'co_signer_3_fico_score':'DOUBLE',
    'co_signer_3_strata_score':'DOUBLE',
    'co_signer_3_dti':'DOUBLE',
    'co_signer_3_total_monthly_income':'DOUBLE',
    'co_signer_3_total_assets':'DOUBLE',
    'co_signer_3_total_liabilities':'DOUBLE',
    'is_a_citizen':'VARCHAR(5)',
    'is_us_perm_resident_or_greencard_holder':'VARCHAR(5)',
    'is_visa_only':'VARCHAR(5)',
    'modified_1_finance_charges':'DOUBLE',
    'modified_1_date':'DATE',
    'modified_1_reason':'VARCHAR(225)',
    'modified_2_total_loan_amount':'DOUBLE',
    'modified_2_amount_financed':'DOUBLE',
    'forbearance_1_start_date':'DATE',
    'forbearance_1_end_date':'DATE',
    'forbearance_1_amount':'DOUBLE',
    'forbearance_2_start_date':'DATE',
    'forbearance_2_end_date':'DATE',
    'forbearance_2_amount':'DOUBLE',
    'modified_2_finance_charges':'DOUBLE',
    'modified_2_date':'DATE',
    'modified_2_reason':'VARCHAR(225)',
    'loan_sold_date':'DATE',
    'loan_sold_rate':'DOUBLE',
    'declared_bankruptcy':'DOUBLE',
    'bankruptcy_date':'DATE',
    'date_added':'DATE',
    'purchase_date':'DATE',
    'booking_date':'DATE',
    'task_1_start_date':'DATE',
    'task_1_resolution_date':'DATE',
    'task_1_category':'VARCHAR(225)',
    'task_1_status':'VARCHAR(225)',
    'task_1_details':'VARCHAR(225)',
    'task_1_result':'VARCHAR(225)',
    'task_2_start_date':'DATE',
    'task_2_resolution_date':'DATE',
    'task_2_category':'VARCHAR(225)',
    'task_2_status':'VARCHAR(225)',
    'task_2_details':'VARCHAR(225)',
    'task_2_result':'VARCHAR(225)',
    'task_3_start_date':'DATE',
    'task_3_resolution_date':'DATE',
    'task_3_category':'VARCHAR(225)',
    'task_3_status':'VARCHAR(225)',
    'task_3_details':'VARCHAR(225)',
    'task_3_result':'VARCHAR(225)',
    'task_4_start_date':'DATE',
    'task_4_resolution_date':'DATE',
    'task_4_category':'VARCHAR(225)',
    'task_4_status':'VARCHAR(225)',
    'task_4_details':'VARCHAR(225)',
    'task_4_result':'VARCHAR(225)',
    'task_5_start_date':'DATE',
    'task_5_resolution_date':'DATE',
    'task_5_category':'VARCHAR(225)',
    'task_5_status':'VARCHAR(225)',
    'task_5_details':'VARCHAR(225)',
    'task_5_result':'VARCHAR(225)',
    'payoff_request_1_start_date':'DATE',
    'payoff_request_1_completion_date':'DATE',
    'payoff_request_1_status':'VARCHAR(225)',
    'payoff_request_1_date_computation_sent':'DATE',
    'payoff_request_1_details':'VARCHAR(225)',
    'payoff_request_1_result':'VARCHAR(225)',
    'payoff_request_2_start_date':'DATE',
    'payoff_request_2_completion_date':'DATE',
    'payoff_request_2_status':'VARCHAR(225)',
    'payoff_request_2_date_computation_sent':'DATE',
    'payoff_request_2_details':'VARCHAR(225)',
    'payoff_request_2_result':'VARCHAR(225)',
    'first_and_last_name':'VARCHAR(225)',
    'work_phone':'VARCHAR(45)',
    'fax_phone':'VARCHAR(45)',
    'property_description':'VARCHAR(45)',
    'property_street':'VARCHAR(45)',
    'property_city':'VARCHAR(45)',
    'property_state':'VARCHAR(45)',
    'property_zip':'VARCHAR(45)',
    'property_county':'VARCHAR(45)',
    'property_type':'VARCHAR(45)',
    'property_occupancy':'VARCHAR(45)',
    'property_ltv':'VARCHAR(45)',
    'property_apn':'VARCHAR(45)',
    'calculated_ltv':'VARCHAR(45)',
    'appraisal_date':'DATE',
    'loan_officer':'VARCHAR(45)'
}
