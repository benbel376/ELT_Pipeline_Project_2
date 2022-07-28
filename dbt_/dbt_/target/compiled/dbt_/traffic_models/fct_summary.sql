

with source_data as (
    select * from warehouse.warehouse.source
),

selection as (
    select track_id, md5(types) as type_id, traveled_d, avg_speed from source_data
),

dim_types as (
    select * from "warehouse"."warehouse"."dim_types"
), 

final as (
    select sel.track_id, dim_types.types, sel.traveled_d, sel.avg_speed
    from selection as sel 
    LEFT JOIN dim_types on sel.type_id = dim_types.Id
)

select * from final