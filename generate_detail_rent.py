import random
from datetime import datetime, timedelta

# status
item_status = ['Baik', 'Rusak', 'Kotor']

# File output
with open("item_data.sql", "w") as f:
    for i in range(1, 10):
        status = random.choices(item_status, weights = [0.6, 0.2, 0.2])

        f.write(
            f"INSERT INTO public.items (status) "
            f"VALUES {status};\n"
        )

print('✅ File detail_rent_data.sql berhasil dibuat!')
