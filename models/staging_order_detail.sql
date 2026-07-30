select * from {{ source('raw', 'order_detail') }}
