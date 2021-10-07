"""All the "main" cardinal functionality should go here."""

COLLECTIONS = [
    "obj_pit_collection",
    "subj_pit_collection",
    "calc_obj_tim",
    "calc_obj_team",
    "calc_subj_team",
    "calc_predicted_aim",
    "calc_predicted_team",
    "calc_tba_team",
    "calc_pickability",
    "calc_tba_tim",
    "calc_spr",
    "match_schedule",
    "teams_list"
]


def get_unsent_docs(collection_name: str):
    if collection_name in COLLECTIONS:
        # TODO: get documents from that collection
        # filter through and only return new documents
        return f"Requested data from {collection_name}"

    else:
        return f"The collection '{collection_name}' does not exist. \
To get a list of supported collections, look at /api/supported-collections/"


def get_match_schedule(comp_code: str):
    # TODO: return the match schedule
    return f"competition code '{comp_code}'"


def get_teams_list(comp_code: str):
    # TODO: Get the teams list and return it
    return f"competition code '{comp_code}'"
