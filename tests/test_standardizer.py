import pandas as pd
from pyclense.standardizer import Standardizer


def test_standardize_dates_valid():
    df = pd.DataFrame({'Event_Date': ['2023-01-01', '01/02/2023', 'Jan 3, 2023', '2023.04.05']})
    st = Standardizer(df)
    st.standardize_dates(['Event_Date'])
    out = st.get_data()['Event_Date'].astype(str)
    assert out.str.match(r"^\d{2}/\d{2}/\d{4}$").all()


def test_standardize_dates_invalid_na_fill():
    df = pd.DataFrame({'Event_Date': ['not-a-date', '2025-12-08']})
    st = Standardizer(df)
    st.standardize_dates(['Event_Date'], na_fill='')
    out = st.get_data()['Event_Date']
    # first should be empty string (na_fill), second should be formatted
    assert out.iloc[0] == ''
    assert pd.notna(out.iloc[1]) and out.iloc[1].count('/') == 2


def test_standardize_booleans_default_and_coerce():
    df = pd.DataFrame({'flag': ['Yes', 'no', 'maybe', None, '1', '0']})
    st = Standardizer(df)
    # default: unknown -> NaN
    st.standardize_booleans(['flag'])
    out = st.get_data()['flag']
    assert pd.isna(out.iloc[2])
    # now coerce unknowns to False
    df2 = pd.DataFrame({'flag': ['Yes', 'no', 'maybe', None, '1', '0']})
    st2 = Standardizer(df2)
    st2.standardize_booleans(['flag'], coerce_unknown=True)
    out2 = st2.get_data()['flag']
    assert out2.iloc[2] is False
    assert out2.iloc[3] is False
