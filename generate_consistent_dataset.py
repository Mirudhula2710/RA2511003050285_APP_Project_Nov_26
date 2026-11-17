import os
import random
import numpy as np
import pandas as pd
from detection.physics_model import compute_expected_drainage

random.seed(42)
np.random.seed(42)

ZONES = [
    ('Hostel Blocks', 1),
    ('Laboratories', 2),
    ('Administration Building', 3),
    ('Canteen', 4)
]

TOTAL_SAMPLES = 4000
samples_per_zone = TOTAL_SAMPLES // len(ZONES)

rows = []

for zone_name, zone_id in ZONES:
    current_level = 100.0
    dt = 5.0 # 5 seconds between readings
    minute_of_day = 0
    hour = 0
    
    # Target counts per zone for 1000 samples:
    # Normal: 650, Warning: 110, Suspected Leak: 110, Critical: 130
    scenarios_pool = (
        ['normal'] * 650 +
        ['warning'] * 110 +
        ['suspected_leak'] * 110 +
        ['critical'] * 130
    )
    random.shuffle(scenarios_pool)
    
    recent_deviations = []

    for i in range(samples_per_zone):
        minute_of_day = (i * 5) % 1440
        hour = minute_of_day // 60
        
        # Tank refills when getting low (< 35 L) to simulate realistic refill cycle back to 100.0 L
        if current_level < 35.0:
            current_level = 100.0
            
        expected_level = compute_expected_drainage(current_level, dt)
        expected_drop = current_level - expected_level
        
        scenario = scenarios_pool[i]
        
        if scenario == 'normal':
            noise = np.random.normal(0, 0.2)
            tank_level = expected_level + noise
            # Ensure deviation_pct is within normal bounds [-4.25%, 4.25%]
            dev_pct = (tank_level - expected_level) / expected_level * 100.0
            if dev_pct < -4.2:
                tank_level = expected_level - 0.04 * expected_level
            elif dev_pct > 4.2:
                tank_level = expected_level + 0.04 * expected_level
            anomaly_type = 'none'
            severity = 'Normal'
            
        elif scenario == 'warning':
            # drop roughly 7.0 L (-4.25% to -10%)
            drop = np.random.uniform(0.05, 0.09) * expected_level
            tank_level = expected_level - drop
            anomaly_type = 'slow_leak'
            severity = 'Warning'
            
        elif scenario == 'suspected_leak':
            # drop roughly 15.0 L (-10% to -20%)
            drop = np.random.uniform(0.11, 0.18) * expected_level
            tank_level = expected_level - drop
            anomaly_type = 'leak_step'
            severity = 'Suspected Leak'
            
        elif scenario == 'critical':
            # drop roughly 25.0 L (<= -20%)
            drop = np.random.uniform(0.22, 0.35) * expected_level
            tank_level = expected_level - drop
            anomaly_type = 'pipe_burst'
            severity = 'Critical'

        tank_level = max(0.0, round(float(tank_level), 3))
        expected_level = round(float(expected_level), 3)
        deviation = round(abs(tank_level - expected_level), 3)
        deviation_pct = round(((tank_level - expected_level) / expected_level * 100.0) if expected_level > 0 else 0.0, 3)
        rate_of_change = round((tank_level - current_level) / dt, 4)
        
        recent_deviations.append(deviation)
        if len(recent_deviations) > 10:
            recent_deviations.pop(0)
            
        rolling_avg_dev = round(float(np.mean(recent_deviations)), 3)
        rolling_std_dev = round(float(np.std(recent_deviations)), 3)
        
        rows.append({
            'zone': zone_name,
            'zone_id': zone_id,
            'reading_index': i,
            'hour': hour,
            'minute_of_day': minute_of_day,
            'tank_level': tank_level,
            'expected_level': expected_level,
            'deviation': deviation,
            'deviation_pct': deviation_pct,
            'rate_of_change': rate_of_change,
            'rolling_avg_deviation': rolling_avg_dev,
            'rolling_std_deviation': rolling_std_dev,
            'minutes_since_last_reading': 5,
            'anomaly_type': anomaly_type,
            'severity': severity
        })
        
        # Advance level for next step (for abnormal steps, advance normally from current expected to maintain realistic time series)
        current_level = expected_level

df = pd.DataFrame(rows)
df.to_csv('data/water_leak_sensor_dataset.csv', index=False)
print("Regenerated data/water_leak_sensor_dataset.csv successfully!")
print(f"Total rows: {len(df)}")
print("Severity distribution:")
print(df['severity'].value_counts())
print("\nTank level range by zone:")
print(df.groupby('zone')['tank_level'].agg(['min', 'mean', 'max']))
