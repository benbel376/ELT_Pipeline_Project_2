

  create  table "warehouse"."warehouse"."dim_types__dbt_tmp"
  as (
    
with source_data as (
    select * from warehouse.warehouse.source
),

final as (
    SELECT distinct
    md5(types) as Id,
    types FROM source_data
)

select * from final
  );