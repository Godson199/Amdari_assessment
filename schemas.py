from pydantic import BaseModel

class Transaction(BaseModel):
    amount_usd: float
    fee: float
    fee_ratio: float
    exchange_rate_src_to_dest: float
    ip_risk_score: float
    device_trust_score: float
    corridor_risk: int
    risk_score_internal: float
    account_age_days: int
    cust_txn_count: int
    cust_avg_amount: float
    cust_max_amount: float
    hour: int
    ip_country_mismatch: bool
    txn_velocity_1h: int
    txn_velocity_24h: int
    channel: str
    kyc_tier: str
    source_currency: str
    dest_currency: str
    new_device: bool
    location_mismatch: bool
