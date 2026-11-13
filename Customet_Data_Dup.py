#  Customer Data Deduplication

branch_1 = [101, 102, 103, 104, 105]

branch_2 = [103, 104, 106, 107, 108]

all_ids = set(branch_1).union(set(branch_2))

common_ids = set(branch_1).intersection(set(branch_2))

print("All Customer IDs =", all_ids)

print("Common Customer IDs =", common_ids)

print("Total Unique Customers =", len(all_ids))