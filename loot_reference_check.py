import json
import re

loot_table_f = open('javelindata_loottables.json',)
loot_table = json.load(loot_table_f)

loot_bucket_f = open('javelindata_lootbuckets.json',)
loot_bucket = json.load(loot_bucket_f)

loot_bucket_ids = []

first_row_data = loot_bucket[0]

for item in first_row_data:
    if "LootBucket" in item:
        loot_bucket_ids.append(first_row_data[item])
        
found_loot = []
missing_loot = []

for item in loot_bucket_ids:
    for loot_item in loot_table:
        for loot_condition in loot_item:
            if type(loot_item[loot_condition]) == str:
                if item in loot_item[loot_condition]:
                    found_loot.append(item)

missing_loot = [x for x in loot_bucket_ids if x not in found_loot]

print(missing_loot)

loot_bucket_numbers = []

for item in first_row_data:
    if first_row_data[item] in missing_loot:
        loot_bucket_numbers.append(item.replace("LootBucket", ""))

print(loot_bucket_numbers)

missing_items = []

for i in range(len(loot_bucket_numbers)-1):
    data = {}
    data["bucket_name"] = missing_loot[i]
    
    items_list = []

    for item in loot_bucket:
        if "Item" + loot_bucket_numbers[i] in item:
            items_list.append(item["Item" + loot_bucket_numbers[i]])
    
    data["missing_items"] = items_list
    missing_items.append(data)

json_data = json.dumps(missing_items)

print(json_data)

loot_table_f.close()
loot_bucket_f.close()
