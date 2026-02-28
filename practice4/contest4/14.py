from datetime import datetime, timedelta, timezone

def parse_line(line):
    date_part, offset_part = line.split()
    
    dt = datetime.strptime(date_part, "%Y-%m-%d")
    
    sign = 1 if offset_part[3] == '+' else -1
    hours, minutes = map(int, offset_part[4:].split(':'))
    
    offset = timezone(sign * timedelta(hours=hours, minutes=minutes))
    
    dt = dt.replace(tzinfo=offset)
    
    return dt.astimezone(timezone.utc)

line1 = input().strip()
line2 = input().strip()

dt1 = parse_line(line1)
dt2 = parse_line(line2)

diff_days = int(abs((dt2 - dt1).total_seconds()) // 86400)

print(diff_days)