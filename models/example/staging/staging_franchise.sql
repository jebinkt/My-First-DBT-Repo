
{{ config(materialized='table') }}


select *
from {{source('raw','franchise')}}

