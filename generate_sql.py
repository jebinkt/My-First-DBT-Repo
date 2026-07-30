import os

# 1. Add all your raw Snowflake table names here
sources = [ 
    "location", 
    "order_detail", 
    "order_header", 
    "truck"
]

# 2. Your source name in sources.yml
source_name = "raw"

# 3. Create a .sql file for each source
for table in sources:
    # This places files inside models/staging_table.sql
    file_path = f"models/staging_{table}.sql"
    
    # Simple base select query using dbt source macro
    sql_content = f"select * from {{{{ source('{source_name}', '{table}') }}}}\n"
    
    with open(file_path, "w") as f:
        f.write(sql_content)
        
    print(f"Created: {file_path}")

print("\nDone! All staging models created successfully.")