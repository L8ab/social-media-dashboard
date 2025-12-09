def calculate_engagement_rate(likes, shares, comments, followers):
    """Calculate engagement rate"""
    if followers == 0:
        return 0
    total_engagement = likes + shares + comments
    return (total_engagement / followers) * 100

def format_number(num):
    """Format large numbers"""
    if num >= 1000000:
        return f"{num / 1000000:.1f}M"
    elif num >= 1000:
        return f"{num / 1000:.1f}K"
    return str(num)
