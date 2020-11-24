import pandas as pd


SHEETS_NUMS = list(range(1, 9))
USECOLS = "A:C"


def table_to_dataframe(filename):
    sheets = pd.read_excel(filename,
                           sheet_name=SHEETS_NUMS,
                           usecols=USECOLS)

    nontoxic_1 = pd.merge(sheets[1].reset_index(), sheets[2].reset_index(),
                          how="inner",
                          on=["index", "разметка", "текст", "контекст"])
    nontoxic_2 = pd.merge(sheets[3].reset_index(), sheets[4].reset_index(),
                          how="inner",
                          on=["index", "разметка", "текст", "контекст"])
    toxic_1 = pd.merge(sheets[5].reset_index(), sheets[6].reset_index(),
                       how="inner",
                       on=["index", "разметка", "текст", "контекст"])
    toxic_2 = pd.merge(sheets[7].reset_index(), sheets[8].reset_index(),
                       how="inner",
                       on=["index", "разметка", "текст", "контекст"])

    nontoxic_1["community_id"] = 1
    nontoxic_1["community_type"] = "nontoxic"
    
    nontoxic_2["community_id"] = 2
    nontoxic_2["community_type"] = "nontoxic"
    
    toxic_1["community_id"] = 3
    toxic_1["community_type"] = "toxic"
    
    toxic_2["community_id"] = 4
    toxic_2["community_type"] = "toxic"
    
    all_comments = pd.concat([nontoxic_1, nontoxic_2,
                              toxic_1, toxic_2],
                            join="outer",
                            ignore_index=True)
    
    return all_comments
