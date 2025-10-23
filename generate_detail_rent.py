import random
from datetime import datetime, timedelta

# File output
with open("detail_rent_data.sql", "w") as f:
    for i in range(1, 16):
        rent_id = random.randint(10, 19)
        item_id = random.randint(64, 73)
        qty = random.randint(1, 5)

        f.write(
            f"INSERT INTO public.detail_rent (rent_id, item_id, qty,) "
            f"VALUES ({rent_id}, {item_id}, {qty}, "
        )

print('✅ File detail_rent_data.sql berhasil dibuat!')
