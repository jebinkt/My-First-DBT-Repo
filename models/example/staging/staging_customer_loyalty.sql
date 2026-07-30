
{{ config(materialized='table') }}


select *
from {{source('raw','customer_loyalty')}}

