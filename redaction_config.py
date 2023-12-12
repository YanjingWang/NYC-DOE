REPORTS_CONFIG = {
    'Reports 1-4 = Initials': {
        'ranges': [(5, 3, 37, 13), (41, 3, 46, 13), (50, 3, 52, 13), (56, 3, 58, 13), (62, 3, 64, 13), (68, 3, 73, 13),(78, 3, 91, 13)],  # Adjust accordingly
        'secondary_mask': (5, 91),
        'secondary_mask_kwargs': {'groups': [(5, 6, 7), (8, 9, 10), (7, 10, 11)]},
        'third_mask': (5, 91),
        'third_mask_kwargs': {'groups': [(3, 4, 11, 12, 13)]},
        'total_col_indexes': [7, 10, 11, 3],  # Add the index of 'Total' columns G, J, K, C
        'groups': [(5, 6, 7), (8, 9, 10), (7, 10, 11), (3, 4, 11, 12, 13)]
    },
    'Reports 5-7 = Reevaluations': {
        'ranges': [(5, 3, 37, 12), (41, 3, 46, 12), (50, 3, 52, 12), (56, 3, 58, 12), (62, 3, 64, 12), (68, 3, 72, 12), (76, 3, 89, 12)],  # Adjust accordingly
        'secondary_mask': (5, 89),
        'secondary_mask_kwargs': {'groups': [(5, 6, 7), (8, 9, 10), (7, 10, 11)]},
        'third_mask': (5, 89),
        'third_mask_kwargs': {'groups': [(3,4,11,12)]},
        'total_col_indexes': [7, 10, 11, 3],  # Add the index of 'Total' columns G, J, K, C
        'groups': [(5, 6, 7), (8, 9, 10), (7, 10, 11), (3,4,11,12)]
    },
    # Add more configurations for other tabs
    "Report 8 = Registers": {
        "ranges": [ (5, 3, 37, 13),(41, 3, 46, 13), (50, 3, 52, 13), (56, 3, 58, 13), (62, 3, 75, 13), (79, 3, 92, 13)],
        'secondary_mask': (5, 92),
        'secondary_mask_kwargs':{"groups": [(3, 4, 5, 6,7), (8, 9, 10, 11,12), (7, 12, 13)]},
        'total_col_indexes': [7, 12, 13],  # Add the index of 'Total' columns G, J, K
        'groups': [(3, 4, 5, 6,7), (8, 9, 10, 11,12), (7, 12, 13)]
    },
    "SWDs by School" : {
        "ranges": [(4, 3, 1603, 3)]
    },
    "Report 8a = Disability class" : {
        "ranges": [(5,  3, 38, 16),(42, 3, 46, 16),(50, 3, 52, 16),(56, 3, 58, 16),(62, 3, 64, 16),(68, 3, 72, 16),(76, 3, 89, 16)],
        'secondary_mask': (5, 89),
        'secondary_mask_kwargs': {'groups': [(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)]},
        'total_col_indexes': [16],  # Add the index of 'Total' columns P
        'groups': [(3, 4, 5, 6, 7, 8, 9, 10, 11, 12,13,14,15,16)]
    },
    "Report 9 = Placement" : {
        "ranges": [(6, 3,  37, 4),(42, 3, 47, 4),(51, 3, 53, 4),(57, 3, 59, 4),(63, 3, 65, 4),(69, 3, 73, 4),(77, 3, 90, 4)]
    },
    "Report 10 = LRE-MRE" : {
        "ranges": [(6, 3, 38, 6), (42, 3, 47, 6), (51, 3, 53, 6), (57, 3, 59, 6), (63, 3, 65, 6), (69, 3, 73, 6), (77, 3, 90, 6)]
    },
    "Report 11 = 3Yr Reevaluations" : {
    "ranges": [(6, 3, 38, 5),(42, 3, 47, 5),(51, 3, 53, 5),(57, 3, 59, 5),(63, 3, 65, 5),(69, 3, 73, 5),(77, 3, 90, 5)],
    'secondary_mask': (6, 90),
    'secondary_mask_kwargs': {'groups': [(4, 5, 3)]},
    'total_col_indexes': [3],  # Add the index of 'Total' columns C
    'groups': [(4, 5, 3)]
    },
    "Report 12 = Program Services" : {
        "ranges": [(5, 3, 7, 8)]
    },
    "Report 13 = Related Services" : {  
        "ranges": [(5, 3, 12, 8)]
    },
    "Report 14 = Inclusion" : {
        "ranges": [(5, 3, 7, 4)]
    }
}
