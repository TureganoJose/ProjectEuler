import pandas as pd
import math
import numpy as np
#from sklearn

from sklearn.ensemble import RandomForestClassifier
#import fancyimpute as fi

def separe_numeric_categoric(df):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    df_n = df.select_dtypes(include=numerics)
    df_c = df.select_dtypes(exclude=numerics)
    print(f'The DF have {len(list(df_n))} numerical features and {len(list(df_c))} categorical fets')
    return df_n, df_c


def find_missing(df):
    total = df.isnull().sum().sort_values(ascending=False)
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    filter(lambda x: x>=minimum, percent)
    return percent


def count_missing(df):
    missing = find_missing(df)
    total_columns_with_missing = 0
    for i in (missing):
        if i>0:
            total_columns_with_missing += 1
    return total_columns_with_missing


def remove_missing_data(df,minimum=.1):
    percent = find_missing(df)
    number = len(list(filter(lambda x: x>=(1.0-minimum), percent)))
    names = list(percent.keys()[:number])
    df = df.drop(names, 1, errors='ignore')
    print(f'{number} columns exclude because haven`t minimium data.')
    return df

# OneHot Encoding (traditional)
def one_hot(df, cols):
    for each in cols:
        dummies = pd.get_dummies(df[each], prefix=each, drop_first=False)
        df = pd.concat([df, dummies], axis=1)
    df = df.drop(cols, axis=1)
    return df


# OneHot Encoding
# Remove first raw value: 'Numeric Categorical' and it's replaced with one existing value
# so a new column is NOT created.
def onehot_encoding(df, cols):
    df[cols][0] = df[cols][1]
    df[cols] = pd.to_numeric(df[cols])
    dummy_columns = pd.get_dummies(df[cols], prefix=cols)
    df = pd.concat([df, dummy_columns], axis=1)
    df = df.drop(columns=[cols])
    return df

#def impute_missing_data(df,minimium_data=.1):
#    columns_missing = count_missing(df)
#    print(f'Total columns with missing values: {count_missing(df)} of a {len(list(df))} columns in df')
#
#    # remove features without minimium size of information
#    df = remove_missing_data(df,minimium_data)
#
#    numerical_df, categorical_df = separe_numeric_categoric(df)
#
#    # Autocomplete using MICE for numerical features.
#    try:
#        df_numerical_complete = fi.MICE(verbose=False).complete(numerical_df.values)
#        n_missing = count_missing(df)
#        print(f'{columns_missing-n_missing} numerical features imputated')
#
#        # Complete the columns name.
#        temp = pd.DataFrame(columns=numerical_df.columns, data=df_numerical_complete)
#
#        # One-hot encoding categorical data
#
#
#
#        # df temp com os dados numericos completados e os categóricos.
#        df = pd.concat([temp, categorical_df], axis=1)
#
#    except Exception as e:
#        print(e)
#        print('Without Missing data in numerical features')
#
#    missing = find_missing(df)
#    names = missing.keys()
#    n = 0
#    for i, c in enumerate(missing):
#        if c > 0:
#            col = names[i]
#            print(f'Start the prediction of {col}')
#            clf = RandomForestClassifier()
#            le = LabelEncoder()
#            ## inverter a ordem da predição das categóricas pode melhorar a precisao.
#            categorical_train = list(categorical_df.loc[:,categorical_df.columns != col])
#
#            temp = one_hot(df,categorical_train)
#            df1 = temp[temp[col].notnull()]
#            df2 = temp[temp[col].isnull()]
#            df1_x = df1.loc[:, df1.columns != col]
#            df2_x = df2.loc[:, df1.columns != col]
#
#            df1_y = df1[col]
#            le.fit(df1_y)
#            df1_y = le.transform(df1_y)
#            clf.fit(df1_x, df1_y)
#            df2_yHat = clf.predict(df2_x)
#            df2_yHat = le.inverse_transform(df2_yHat)
#            df2_yHat = pd.DataFrame(data=df2_yHat, columns=[col])
#            df1_y = le.inverse_transform(df1_y)
#            df1_y = pd.DataFrame(data=df1_y,columns=[col])
#
#            df2_x.reset_index(inplace=True)
#            result2 = pd.concat([df2_yHat, df2_x], axis=1)
#            try:
#                del result2['index']
#            except:
#                pass
#
#            df1_x.reset_index(inplace=True)
#            result1 = pd.concat([df1_y, df1_x], axis=1)
#            try:
#                del result1['index']
#            except:
#                pass
#
#            result = pd.concat([result1, result2])
#            result = result.set_index(['Id'])
#            df.reset_index()
#            try:
#                df.set_index(['Id'],inplace=True)
#            except:
#                pass
#            df[col] = result[col]
#
#            n += 1
#
#    print(f'Number of columns categorical with missing data solved: {n}')
#
#    return df
#
#
#df = impute_missing_data(df)


ds_Rwanda_Raw = pd.read_csv(r'C:\Users\Jose\Desktop\Claire\Rwanda_data.csv')


#print('Number of NaNs:{}'.format(ds_Rwanda_Raw.isnull().sum()))

relevant_columns = ['emo_violence_dum', 'physical_violence_dum', 'sexual_violence_dum', 'emo_violence_dum_bl',
                    'physical_violence_dum_bl', 'sexual_violence_dum_bl', 'couple_type', 'village_id_m_bl',
                    'village_treatment', 'couple_treat',
                    'd8_age_years_w_bl', 'd5_partner_title1_w_bl',
                    'l3_partner_trust2_m_bl', 'm3_partner_trust2_w_bl', 'dep_score_m', 't1_ptnr_alcl_use_w_bl',
                    't2_ptnr_drink_too_much_w_bl', 'v2_alcohol_excess_m_bl', '', 'gg8_rel_talks_num_m_bl',
                    'gg4_rel_blood_num_m_bl', 'own_gendernorms_w_bl_equit', 'unable_to_work_w_bl', 'sector_id',
                    'Napplicantscat',
                    'q1_beat_neglect_child_w_bl_p', 'q2_beating_refusing_sex_w_bl_p', 'q3_beating_disobey_w_bl_p',
                    'q4_beating_burn_food_w_bl_p', 'q5_beat_suspect_unfaith_w_bl_p', 'own_gendernorms_w_bl',
                    'comm_gendernorms_w_bl', 'own_ipv_justified_w_bl',
                    'own_refusesex_justified_w_bl', 'numb_villagerels_w_bl', 'numb_closefriends_w_bl',
                    'numb_villagerels_m_bl', 'numb_closefriends_m_bl', 'dep_total_score_m_bl', 'become_intimidating_m_bl', 'intent_violence_m_bl', 'trauma_score_m_bl',
                    'own_ipv_justified_m_bl', 'own_refusesex_justified_m_bl', 'e29_education_m_bl_clean',
                    'e11_education_w_bl_clean', 'oo7_sdm7_tokens_give_m_bl', 'dd1_cmty_shame_hsbnd_hhwrk_m_bl',
                    'dd2_cmty_obey_husband_m_bl', 'dd3_cmty_woman_control_man_m_bl', 'dd4_cmty_no_intervene_ipv_m_b',
                    'dd5_cmnty_jealousy_m_bl', 'dd6_cmty_prohibit_visits_m_bl', 'dd7_cmty_beat_wife_m_bl',
                    'dd8_cmty_force_sex_m_bl', 'k6_obey_husband_m_bl', 'k7_woman_control_man_m_bl',
                    'k8_ipv_private_m_bl', 'l1_conflict_resolution_m_bl', 'l2_emotion_sharing_m_bl',
                    'h2_paid_employed_m_bl', 'h3_days_per_week_m_bl',
                    'h4_earnings_per_day_m_bl', 'e15_concubines_m_bl', 'e16_concubines_count_m_bl',
                    'e10_age_years_m_bl', 'e9_household_size_m_bl', 'e3_household_head_m_bl',
                    'll1_sdm7_tokens_give_w_bl', 'dd5_happiness_post_economic_w_bl', 'i1_vsla_ptcp_length_yrs_w_bl',
                    'i2_vsla_ptcp_length_mths_w_bl', 'j1_parents_alive_w_bl', 'j2_parents_in_village_w_bl',
                    'k1_comm_money1_w_bl', 'k2_comm_money2_w_bl', 'k3_comm_maj_purch1_w_bl', 'k4_comm__maj_purch2_w_bl',
                    'k5_comm_edu1_w_bl', 'k6_comm_edu2_w_bl', 'h23_savings_amt_w_bl', 'h18_land_decisions_w_bl',
                    'h16_land_title_w_bl', 'h15_own_land_w_bl', 'h11_employed_w_bl',
                    'g1_meals_skipped_m', 'decision_input_income_m', 'decision_extent_income_m',
                    'decision_input_hh_income_m', 'decision_extent_hh_income_m', 'decision_input_hh_expenses_m',
                    'decision_ideal_hh_expenses_m', 'decision_extent_hh_expenses_m', 'decision_input_childbearing_m',
                    'decision_ideal_childbearing_m', 'decision_extent_hh_childbear_m', 'events_laugh_m',
                    'events_walk_m', 'events_leisure_m', 'respect_partner_m', 'feel_respected_m',
                    'marital_life_satisfied_m', 'l2_emotion_sharing_m', 'l3_partner_trust2_m', 'drink_too_much_m',
                    'stress_confidence_m', 'stress_irritations_m', 'stress_anger_m', 'stress_nervous_m',
                    'anger_calm_down_m', 'q1_beating_neglect_children_m', 'q2_beating_refusing_sex_m',
                    'q3_beating_disobey_m', 'q4_beating_burn_food_m', 'q5_beating_suspect_unfaithful_m',
                    'r1_refuse_know_unfaithful_m', 'r2_refuse_drunk_m', 'r3_refuse_mistreatment_m', 's1_disrespect_m',
                    's3_cheating_m', 's7_control_m', 's9_impt_decision_m', 't1_intim_disrespect_m',
                    't3_intim_flirting_m', 't5_intim_impt_decision_m', 'u2_ptnr_violent_freq_m', 'v2_alcohol_excess_m',
                    'k5_shame_husband_hhwork_m', 'k6_obey_husband_m', 'k8_ipv_private_m', 'dd8_cmty_force_sex_m',
                    'dd7_cmty_beat_wife_m', 'dd6_cmty_prohibit_visits_m', 'overall_happiness_m',
                    'oo7_sdm7_tokens_give_m',
                    'h22_prevent_work_outside_w', 'decision_input_income_w', 'decision_extent_income_w',
                    'decision_input_hh_income_w', 'decision_extent_hh_income_w', 'decision_input_hh_expenses_w',
                    'decision_ideal_hh_expenses_w', 'decision_extent_hh_expenses_w', 'decision_input_childbearing_w',
                    'decision_ideal_childbearing_w', 'decision_extent_childbearing_w',
                    'decision_alone_w',
                    'decision_emergency_w', 'decision_resp_refuse_w', 'decision_resp_money_w',
                    'events_laugh_w', 'events_walk_w', 'events_leisure_w', 'escalate_physical_w', 'spouse_cheat_w',
                    'respect_partner_w', 'feel_respected_w', 'confident_to_disagree_w', 'marital_life_satisfied_w',
                    'l2_emotion_sharing_w', 'l3_partner_trust2_w', 'stress_nervous_w',
                    'q1_beating_neglect_children_w', 'q2_beating_refusing_sex_w', 'q3_beating_disobey_w',
                    'q4_beating_burn_food_w', 'q5_beating_suspect_unfaithful_w', 'r1_refuse_know_unfaithful_w',
                    'r2_refuse_drunk_w', 'r3_refuse_mistreatment_w',
                    'l1_shame_husband_hhwork_w', 'l2_obey_husband_w', 'l4_ipv_private_w', 'z7_cmty_force_sex_w',
                    'knowledge_ipv_w', 'z2_cmty_obey_husband_w', 'z5_cmnty_jealousy_w', 'y1_contraception_use_w',
                    'beliefs_about_self_w', 'll1_sdm7_tokens_give_w', 'oo1_meta1_distress_w']

# Get relevant columns
ds_reduced_set_Rwanda_Raw = pd.DataFrame(ds_Rwanda_Raw, columns= relevant_columns)

# Drop columns with all nans
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.dropna(how='all', axis=1)

# Drop columns with less than 1000 actual values
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.dropna(thresh=1000, axis=1)
#print(ds_reduced_set_Rwanda_Raw)

count_empty = 0
count_nan = 0
count_bin = 0
count_numcat = 0
count_num = 0
count_remote = 0
count_cat = 0

# Replace .r, .d, and .a
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.replace('.r', -100)
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.replace('.d', -101)
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.replace('.a', -102)
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.replace('.n', -103)
ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.replace('.o', -104)


print('Total Number of NaNs:{}'.format(ds_Rwanda_Raw.isnull().sum().sum()))
for iVar, Var in enumerate(ds_reduced_set_Rwanda_Raw):
    if ds_reduced_set_Rwanda_Raw[Var].isnull().sum()/2044 > 0.1:
        print( 'Variable {} has more 10% of Nans {}'.format(Var,ds_reduced_set_Rwanda_Raw[Var].isnull().sum()))
        #ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(
        #    ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])
    if ds_reduced_set_Rwanda_Raw[Var][0] == '':
        count_empty = count_empty + 1
        ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(
            ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])
    elif ds_reduced_set_Rwanda_Raw[Var][0] == 'binary':
        count_bin = count_bin + 1
        # Filling nans with more frequent value
        ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])
        ds_reduced_set_Rwanda_Raw[Var][0] = ds_reduced_set_Rwanda_Raw[Var][1]
        ds_reduced_set_Rwanda_Raw[Var] = pd.to_numeric(ds_reduced_set_Rwanda_Raw[Var])

        # Check they are all 0 and 1s
        elements = ds_reduced_set_Rwanda_Raw[Var][1:].unique()
        if any(elements > 1) or any(elements < 0):
            ds_reduced_set_Rwanda_Raw = onehot_encoding(ds_reduced_set_Rwanda_Raw, Var)
    elif ds_reduced_set_Rwanda_Raw[Var][0] == 'Numeric_Categorical':
        count_numcat = count_numcat + 1

        # Filling nans with more frequent value
        ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])

        ds_reduced_set_Rwanda_Raw = onehot_encoding(ds_reduced_set_Rwanda_Raw, Var)

        #ds_reduced_set_Rwanda_Raw[Var][0] = ds_reduced_set_Rwanda_Raw[Var][1]
        #ds_reduced_set_Rwanda_Raw[Var] = pd.to_numeric(ds_reduced_set_Rwanda_Raw[Var])
        #dummy_var = pd.get_dummies(ds_reduced_set_Rwanda_Raw[Var], prefix=Var)
        #ds_reduced_set_Rwanda_Raw = pd.concat([ds_reduced_set_Rwanda_Raw, dummy_var], axis=1)
        #ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.drop(columns=[Var])
        print(Var)
    elif ds_reduced_set_Rwanda_Raw[Var][0] == 'Numerical':
        count_num = count_num + 1
        ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(
            ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])
        #
    elif ds_reduced_set_Rwanda_Raw[Var][0] == 'Remove':
        count_remote = count_remote + 1
        ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(
            ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])
        ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.drop(columns=[Var])
    elif ds_reduced_set_Rwanda_Raw[Var][0] == 'Categorical':
        count_cat = count_cat + 1
        ds_reduced_set_Rwanda_Raw = onehot_encoding(ds_reduced_set_Rwanda_Raw, Var)
    elif math.isnan(ds_reduced_set_Rwanda_Raw[Var][0]):
        count_nan = count_nan + 1
        ds_reduced_set_Rwanda_Raw[Var][0] = ds_reduced_set_Rwanda_Raw[Var][1]
        ds_reduced_set_Rwanda_Raw[Var] = pd.to_numeric(ds_reduced_set_Rwanda_Raw[Var])
        # Filling nans with more frequent value
        ds_reduced_set_Rwanda_Raw[Var][1:] = ds_reduced_set_Rwanda_Raw[Var][1:].fillna(ds_reduced_set_Rwanda_Raw[Var].value_counts().index[0])

        elements = ds_reduced_set_Rwanda_Raw[Var].unique()
        n_elements = ds_reduced_set_Rwanda_Raw[Var].value_counts()
        if n_elements.size < 10:
            ds_reduced_set_Rwanda_Raw = onehot_encoding(ds_reduced_set_Rwanda_Raw, Var)
        #del ds_reduced_set_Rwanda_Raw[Var] # I don't know what kind of variable is that

#print( ds_reduced_set_Rwanda_Raw.apply(lambda x: x.isnull().sum()/2044, axis='columns') )

# Imputation

ds_reduced_set_Rwanda_Raw = ds_reduced_set_Rwanda_Raw.drop([0], axis=0)


print(count_empty)
print(count_nan)
print(count_bin)
print(count_numcat)
print(count_num)
print(count_remote)
print(count_cat)

## Analysis

# Labels are the values we want to predict
labels = np.array(ds_reduced_set_Rwanda_Raw['actual'])
# Remove the labels from the features
# axis 1 refers to the columns
features= ds_reduced_set_Rwanda_Raw.drop('actual', axis = 1)
# Saving feature names for later use
feature_list = list(features.columns)
# Convert to numpy array
features = np.array(features)