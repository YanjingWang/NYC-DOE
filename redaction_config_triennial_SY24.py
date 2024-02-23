TRIENNIAL_REPORTS_CONFIG_SY24 = {
    'Program Delivery': {
        'ranges': [(3, 2, 6, 7)],#Adjust accordingly
        'numeric_percentage_pairs': [(2,3),(4,5),(6,7)], # [(B,C), (D,E), (F,G)]
        '100_percentage_sum' : [(3,5,7)],  # [(C,E,G)]
        'total_by_primarytype': [(1)], # [(A)]
        'PS_flag': True
    },
    'Program Delivery by District': {
        'ranges': [(3, 3, 99, 8)],  # Adjust accordingly
        'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)], # [(C,D), (E,F), (G,H)]
        '100_percentage_sum' : [(4,6,8)],  # [(D,F,H)]
        'mask_by_category': [(2, 3, 4)], # [(B, C, D)]
        'PS_flag': True
    },
    # Add more configurations for other tabs
    "Program Delivery by Supt": {
        "ranges": [ (3, 4, 136, 9)],
        'numeric_percentage_pairs': [(4, 5), (6, 7), (8, 9)], # [(D,E), (F,G), (H,I)]
        '100_percentage_sum' : [(5,7,9)], # [(E,G,I)]
        'mask_by_category': [(3, 4, 5)], # [(C, F, G)]
        'PS_flag': True
    },
    "Program Delivery by School" : {
        "ranges": [(3, 3, 4207, 8)],
        'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)], # [(C,D), (E,F), (G,H)]
        '100_percentage_sum' : [(4,6,8)], # [(D,F,H)]
        'mask_by_category': [(2, 3, 4)], # [(B, C, D)]
        'mask_by_district' : [(1,2,3,4)], # [(SchoolDBN,Primary Program Type, Full Receiving, Percentage)]
        'PS_flag': True
    },
    "Related Service Delivery" : {
        "ranges": [(3, 2, 11, 7)],
        'numeric_percentage_pairs': [(2, 3),(4, 5),(6, 7)], # [(B,C), (D,E), (F,G)]
        '100_percentage_sum' : [(3,5,7)], # [(C,E,G)]
        'total_by_RStype': [(1)], # [(A)]
        # 'PS_flag': True
    },
    "RS Delivery by District": {
        "ranges": [(3, 3, 259, 8)], 
        'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)], # [(C,D), (E,F), (G,H)]
        '100_percentage_sum' : [(4,6,8)], # [(D,F,H)]
        'NA_Partcial_Encounter_Redaction': [(3, 2, 5, 6)], # [(Start_Row, B, E, F)]
        'mask_by_category': [(2, 3, 4)], # [(B, C, D)]
        'mask_RS_bilingual_percent': [ (3, 4), (5, 6), (7, 8)],# [(related services recommendation type, full encounter, percentage, partial encounter, percentage, no encounter, percentage)]
        'RS_flag': True
    },

    "RS Delivery by Supt" : {
        "ranges": [(3, 4, 360, 9)],
        'numeric_percentage_pairs': [(4, 5), (6, 7), (8, 9)], # [(D,E), (F,G), (H,I)]
        '100_percentage_sum' : [(5,7,9)], # [(E,G,I)]
        'NA_Partcial_Encounter_Redaction': [(3, 3, 6, 7)], # [(Start_Row, C, F, G)]
        'mask_by_category': [(3, 4, 5)], # [(C, D, E)]
        'mask_RS_bilingual_percent': [ (4, 5), (6, 7), (8, 9)], # [(related services recommendation type, full encounter, percentage, partial encounter, percentage, no encounter, percentage)]
        'RS_flag': True
    }, 

    "RS Delivery by School" : {
        "ranges": [(3, 3, 8357, 8)],
        'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)], # [(C,D), (E,F), (G,H)]
        '100_percentage_sum' : [(4,6,8)], # [(D,F,H)]
        'NA_Partcial_Encounter_Redaction': [(3, 2, 5, 6)], # [(Start_Row, B, E, F)]
        'mask_by_category': [(2, 3, 4)], # [(B, C, D)]
        'mask_by_district' : [(1,2,3,4)], # [(SchoolDBN,Related Services Recommendation Type, Full Encounter, Percentage)]
        'mask_RS_bilingual_percent': [(3, 4), (5, 6), (7, 8)], # [(related services recommendation type, full encounter, percentage, partial encounter, percentage, no encounter, percentage)]
        'RS_flag': True
    },
    "Transportation by District" : {
        "ranges": [(3, 2, 35, 7)],
        'numeric_percentage_pairs': [(2, 3), (4, 5), (6, 7)], # [(B,C), (D,E), (F,G)]
        '100_percentage_sum' : [(3,5,7)], # [(C,E,G)]
        'PS_flag': True
    },
     "Transportation by School" : {
        "ranges": [(3, 2, 1544, 7)],
        'numeric_percentage_pairs': [(2, 3), (4, 5), (6, 7)], # [(B,C), (D,E), (F,G)]
        '100_percentage_sum' : [(3,5,7)], # [(C,E,G)]
        'PS_flag': True
    },

}
