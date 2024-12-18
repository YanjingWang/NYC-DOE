from Report8a import Solution as Report8a
from Report15a import Solution as Report15a
from Report16 import Solution as Report16
# Create instances
report8a_instance = Report8a()
report15a_instance = Report15a()
report16_instance = Report16()

REPORTS_CONFIG_SY24 = {
    'Reports 1-4 = Initials': {
        'ranges': [(5, 3, 37, 13), (41, 3, 46, 13), (50, 3, 52, 13), (56, 3, 59, 13), (63, 3, 65, 13), (69, 3, 74, 13),(79, 3, 92, 13), (99, 3, 101, 13),(107, 3, 109, 13)],#Adjust accordingly
        'secondary_mask': (5, 109),
        'secondary_mask_kwargs': {'groups': [(5, 6, 7), (8, 9, 10), (7, 10, 11)]},
        'third_mask': (5, 109),
        'third_mask_kwargs': {'groups': [(3, 4, 11, 12, 13)]},
        'total_col_indexes': [7, 10, 11, 3],  # Add the index of 'Total' columns G, J, K, C
        'groups':[(5,6,7),(8,9,10),(7,10,11),(3,4,11,12,13)]
    },
    'Reports 5-7 = Reevaluations': {
        'ranges': [(5, 3, 37, 12), (41, 3, 46, 12), (50, 3, 52, 12), (56, 3, 59, 12), (63, 3, 65, 12), (69, 3, 73, 12), (77, 3, 90, 12),(95, 3, 97, 12),(102, 3, 104, 12)],  # Adjust accordingly
        'secondary_mask': (5, 104),
        'secondary_mask_kwargs': {'groups': [(5, 6, 7), (8, 9, 10), (7, 10, 11)]},
        'third_mask': (5, 104),
        'third_mask_kwargs': {'groups': [(3,4,11,12)]},
        'total_col_indexes': [7, 10, 11, 3],  # Add the index of 'Total' columns G, J, K, C
        'groups':[(5,6,7),(8,9,10),(7,10,11),(3,4,11,12)]
    },
    # Add more configurations for other tabs
    "Report 8 = Registers": {
        "ranges": [ (5, 3, 37, 13),(41, 3, 46, 13), (50, 3, 52, 13), (56, 3, 59, 13), (63, 3, 76, 13), (80, 3, 93, 13),(97, 3, 99, 13),(104, 3, 106, 13)],
        'secondary_mask': (5, 106),
        'secondary_mask_kwargs':{"groups": [(3, 4, 5, 6,7), (8, 9, 10, 11,12), (7, 12, 13)]},
        'total_col_indexes': [7, 12, 13],  # Add the index of 'Total' columns G, L, M
        'groups':[(3,4,5,6,7),(8,9,10,11,12),(7,12,13)]
    },
    "Report 8a = SWDs by School" : {
        "ranges": [(4, 3, report8a_instance.lastrow, 3)]
    },
    "Report 9 = Disability class" : {
        "ranges": [(5,  3, 37, 16),(41, 3, 46, 16),(50, 3, 52, 16),(56, 3, 59, 16),(63, 3, 65, 16),(69, 3, 73, 16),(77, 3, 90, 16),(94, 3, 96, 16),(100, 3, 102, 16)],
        'secondary_mask': (5, 102),
        'secondary_mask_kwargs': {'groups': [(3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)]},
        'total_col_indexes': [16],  # Add the index of 'Total' columns P
        'groups':[(3,4,5,6,7,8,9,10,11,12,13,14,15,16)]
    },
    # "Report 10 = IEP Service Recs" : {
    #     "ranges": [(6, 3, 38, 14),(43, 3, 48, 14),(53, 3, 55, 14),(60, 3, 63, 14),(63, 3, 65, 14),(68, 3, 70, 14),(75, 3, 79, 14),(84, 3, 97, 14),(103, 3, 105, 14),(111, 3, 113, 14)],
    # },
    "Report 10 = IEP Service Recs": {
        "ranges": [
            (6, 3, 38, 14),    # C6 to N38
            (43, 3, 48, 14),   # C43 to N48
            (53, 3, 55, 14),   # C53 to N55
            (60, 3, 63, 14),   # C60 to N63
            (68, 3, 70, 14),   # C68 to N70
            (75, 3, 79, 14),   # C75 to N79
            (84, 3, 97, 14),   # C84 to N97
            (103, 3, 116, 14), # C103 to N116
            (122, 3, 124, 14),  # C122 to N124
            (130, 3, 132, 14)  # C130 to N132            
        ],
        'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14)],
        '100_percentage_sum' : [(4,6,8,10,12,14)],
    },
    "Report 11 = Placement" : {
        "ranges": [(6, 3,  38, 3),(42, 3, 47, 3),(51, 3, 53, 3),(57, 3, 60, 3),(64, 3, 66, 3),(70, 3, 74, 3),(78, 3, 91, 3),(96, 3, 98, 3),(103, 3, 105, 3)]
    }, #don't have to redact avg column
    "Report 12 = LRE-MRE" : {
        "ranges": [(6, 3, 38, 6), (42, 3, 47, 6), (51, 3, 53, 6), (57, 3, 60, 6), (64, 3, 66, 6), (70, 3, 74, 6), (78, 3, 91, 6), (96, 3, 98, 6), (103, 3, 105, 6)]
    },
    "Report 13 = 3Yr Reevaluations" : {
    "ranges": [(6, 3, 38, 5),(42, 3, 47, 5),(51, 3, 53, 5),(57, 3, 60, 5),(64, 3, 66, 5),(70, 3, 74, 5),(78, 3, 91, 5),(96, 3, 98, 5),(103, 3, 105, 5)],
    'secondary_mask': (5,105),
    'secondary_mask_kwargs': {'groups': [(3, 4, 5)]},   
    'total_col_indexes': [3],  # Add the index of 'Total' columns C
    },
     "Report 14 = Programs" : {
             "ranges": [
        (5, 3, 8, 8),    # C5 to H8
        (12, 3, 17, 8),  # C12 to H17
        (21, 3, 23, 8),  # C21 to H23
        (27, 3, 30, 8),  # C27 to H30
        (34, 3, 36, 8),  # C34 to H36
        (40, 3, 44, 8),  # C40 to H44
        (48, 3, 61, 8),  # C48 to H61
        (65, 3, 67, 8),  # C65 to H67
        (71, 3, 73, 8),  # C71 to H73
    ],
    'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)],
    '100_percentage_sum' : [(4,6,8)],
    },
    "Report 14a = Bilingual Programs" : {
        "ranges": [(5, 3, 8, 8)],
        'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)],
        '100_percentage_sum' : [(4,6,8)],
    },    
    "Report 15 = Related Services" : {
    "ranges": [
        (5, 3, 13, 8),   # C5 to H13
        (17, 3, 22, 8),  # C17 to H22
        (26, 3, 28, 8),  # C26 to H28
        (32, 3, 35, 8),  # C32 to H35
        (39, 3, 41, 8),  # C39 to H41
        (45, 3, 49, 8),  # C45 to H49
        (53, 3, 66, 8),  # C53 to H66
        (70, 3, 72, 8),  # C70 to H72
        (76, 3, 78, 8),  # C76 to H78
    ],
    'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)],
    '100_percentage_sum' : [(4,6,8)],
    },
    "Report 15a = Transportation" : {
    "ranges": [
        (5, 3, 37, 8),   # C5 to H37
        (41, 3, 46, 8),  # C41 to H46
        (50, 3, 52, 8),  # C50 to H52
        (56, 3, 59, 8),  # C56 to H59
        (63, 3, 65, 8),  # C63 to H65
        (69, 3, 73, 8),  # C69 to H73
        (77, 3, 90, 8),  # C77 to H90
        (94, 3, 96, 8),  # C94 to H96
        (100, 3, 102, 8),# C100 to H102
        (106, 3, report15a_instance.lastrow, 8)# C106 to H1614
    ],
    'numeric_percentage_pairs': [(3, 4), (5, 6), (7, 8)],
    '100_percentage_sum' : [(4,6,8)],
    },
    "Report 16 = BIP" : {
    "ranges": [
        (5, 3, 9, 6),    # C5 to F9
        (13, 3, 45, 6),  # C13 to F45
        (49, 3, 54, 6),  # C49 to F54
        (58, 3, 60, 6),  # C58 to F60
        (64, 3, 67, 6),  # C64 to F67
        (71, 3, 73, 6),  # C71 to F73
        (77, 3, 81, 6),  # C77 to F81
        (85, 3, 98, 6),  # C85 to F98
        (102, 3, 104, 6),# C102 to F104
        (108, 3, 110, 6),# C108 to F110
        (114, 3, report16_instance.lastrow, 6)# C114 to F1717
    ],
        'secondary_mask': (5, report16_instance.lastrow),
        'secondary_mask_kwargs': {'groups': [(3, 5)]},
    # 'numeric_percentage_pairs': [(3, 4), (5, 6)], #don't have to redact percentage 
    # '100_percentage_sum' : [(4,6)],
    },
    "Report 17 = Inclusion" : {
        "ranges": [(5, 3, 8, 4)],
        'numeric_percentage_pairs': [(3, 4)]
    }
}
